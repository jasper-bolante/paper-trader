import { formatWeight } from '../lib/calc';

export default function ConnectPanel({
  btSupported,
  status,
  deviceName,
  liveKg,
  unit,
  onConnect,
  onDisconnect,
}) {
  if (!btSupported) {
    return (
      <section className="card card--notice">
        <h2 className="card__title">Scale connection unavailable</h2>
        <p>
          This browser doesn&apos;t support Web Bluetooth (Safari and iOS browsers
          don&apos;t). You can still log weigh-ins below by entering them manually.
        </p>
      </section>
    );
  }

  return (
    <section className="card">
      <div className="connect-row">
        <div>
          <h2 className="card__title">Smart scale</h2>
          {status === 'connected' ? (
            <p className="connect-status connect-status--on">
              Connected to {deviceName}
            </p>
          ) : status === 'connecting' ? (
            <p className="connect-status">Connecting…</p>
          ) : (
            <p className="connect-status">Not connected</p>
          )}
        </div>
        {status === 'connected' ? (
          <button type="button" className="btn btn--ghost" onClick={onDisconnect}>
            Disconnect
          </button>
        ) : (
          <button
            type="button"
            className="btn btn--primary"
            onClick={onConnect}
            disabled={status === 'connecting'}
          >
            {status === 'connecting' ? 'Connecting…' : 'Connect Sensor'}
          </button>
        )}
      </div>
      {status === 'connected' && liveKg != null && (
        <p className="live-reading">
          Live reading: <strong>{formatWeight(liveKg, unit)}</strong>
        </p>
      )}
    </section>
  );
}
