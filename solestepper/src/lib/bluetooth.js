// Web Bluetooth integration for GATT Weight Scale Service (0x181D).
//
// Readings arrive as indications on the Weight Measurement characteristic
// (0x2A9D). Per the GATT spec the payload is:
//   byte 0        flags (bit 0: 0 = SI/kg, 1 = imperial/lb; bit 1: timestamp
//                 present; bit 2: user ID present; bit 3: BMI/height present)
//   bytes 1-2     weight, uint16 little-endian
//                 resolution 0.005 kg (SI) or 0.01 lb (imperial)
// We only need the flags + weight field; optional trailing fields are ignored.

const WEIGHT_SCALE_SERVICE = 0x181d;
const WEIGHT_MEASUREMENT_CHARACTERISTIC = 0x2a9d;

export function isWebBluetoothSupported() {
  return typeof navigator !== 'undefined' && 'bluetooth' in navigator;
}

// Returns the weight in kg, or null if the packet is not a usable measurement.
export function parseWeightMeasurement(view) {
  if (!view || view.byteLength < 3) return null;
  const flags = view.getUint8(0);
  const imperial = (flags & 0x01) !== 0;
  const raw = view.getUint16(1, true);
  if (raw === 0xffff) return null; // spec sentinel: "measurement unsuccessful"
  return imperial ? raw * 0.01 * 0.45359237 : raw * 0.005;
}

export class ScaleConnection {
  constructor({ onMeasurement, onDisconnect } = {}) {
    this.onMeasurement = onMeasurement;
    this.onDisconnect = onDisconnect;
    this.device = null;
    this.characteristic = null;
    this._capture = null;
    this._handleValue = this._handleValue.bind(this);
    this._handleDisconnect = this._handleDisconnect.bind(this);
  }

  isConnected() {
    return Boolean(this.device && this.device.gatt && this.device.gatt.connected);
  }

  async connect() {
    const device = await navigator.bluetooth.requestDevice({
      filters: [{ services: [WEIGHT_SCALE_SERVICE] }],
    });
    device.addEventListener('gattserverdisconnected', this._handleDisconnect);
    const server = await device.gatt.connect();
    const service = await server.getPrimaryService(WEIGHT_SCALE_SERVICE);
    const characteristic = await service.getCharacteristic(
      WEIGHT_MEASUREMENT_CHARACTERISTIC,
    );
    await characteristic.startNotifications();
    characteristic.addEventListener('characteristicvaluechanged', this._handleValue);
    this.device = device;
    this.characteristic = characteristic;
    return device.name || 'Weight scale';
  }

  disconnect() {
    if (this.characteristic) {
      this.characteristic.removeEventListener(
        'characteristicvaluechanged',
        this._handleValue,
      );
    }
    if (this.device) {
      this.device.removeEventListener('gattserverdisconnected', this._handleDisconnect);
      if (this.device.gatt.connected) this.device.gatt.disconnect();
    }
    this.cancelCapture(new Error('The scale was disconnected.'));
    this.device = null;
    this.characteristic = null;
  }

  // Waits for a stable reading: resolves once two consecutive measurements
  // agree within 50 g. Scales re-send the settled weight, so this converges
  // quickly; if it never does, the last reading received wins at timeout.
  captureReading({ timeoutMs = 30000 } = {}) {
    return new Promise((resolve, reject) => {
      if (!this.isConnected()) {
        reject(new Error('No scale connected.'));
        return;
      }
      if (this._capture) {
        reject(new Error('A reading is already in progress.'));
        return;
      }
      const readings = [];
      const finish = (settle, value) => {
        clearTimeout(timer);
        this._capture = null;
        settle(value);
      };
      const timer = setTimeout(() => {
        if (readings.length > 0) {
          finish(resolve, readings[readings.length - 1]);
        } else {
          finish(
            reject,
            new Error('No reading received. Step on the scale and try again.'),
          );
        }
      }, timeoutMs);
      this._capture = {
        cancel: (err) => finish(reject, err || new Error('Reading cancelled.')),
        onReading: (kg) => {
          readings.push(kg);
          const n = readings.length;
          if (n >= 2 && Math.abs(readings[n - 1] - readings[n - 2]) <= 0.05) {
            finish(resolve, readings[n - 1]);
          }
        },
      };
    });
  }

  cancelCapture(err) {
    if (this._capture) this._capture.cancel(err);
  }

  _handleValue(event) {
    const kg = parseWeightMeasurement(event.target.value);
    if (kg == null) return;
    if (this.onMeasurement) this.onMeasurement(kg);
    if (this._capture) this._capture.onReading(kg);
  }

  _handleDisconnect() {
    this.cancelCapture(new Error('The scale disconnected mid-reading.'));
    this.device = null;
    this.characteristic = null;
    if (this.onDisconnect) this.onDisconnect();
  }
}
