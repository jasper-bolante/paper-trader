import { useEffect, useMemo, useRef, useState } from 'react';
import { ScaleConnection, isWebBluetoothSupported } from './lib/bluetooth';
import { analyzeSession } from './lib/calc';
import UnitToggle from './components/UnitToggle';
import ConnectPanel from './components/ConnectPanel';
import WeightStep from './components/WeightStep';
import Results from './components/Results';
import History from './components/History';

let nextSessionId = 1;

export default function App() {
  const btSupported = useMemo(isWebBluetoothSupported, []);
  const [unit, setUnit] = useState('kg');
  const [status, setStatus] = useState('disconnected');
  const [deviceName, setDeviceName] = useState(null);
  const [liveKg, setLiveKg] = useState(null);
  const [capturing, setCapturing] = useState(null); // 'pre' | 'post' | null
  const [pre, setPre] = useState(null); // { kg, time, manual }
  const [post, setPost] = useState(null);
  const [history, setHistory] = useState([]);
  const [error, setError] = useState(null);
  const connectionRef = useRef(null);

  useEffect(() => {
    return () => connectionRef.current?.disconnect();
  }, []);

  async function handleConnect() {
    setError(null);
    setStatus('connecting');
    const conn = new ScaleConnection({
      onMeasurement: (kg) => setLiveKg(kg),
      onDisconnect: () => {
        setStatus('disconnected');
        setDeviceName(null);
        setLiveKg(null);
        setCapturing(null);
      },
    });
    try {
      const name = await conn.connect();
      connectionRef.current = conn;
      setDeviceName(name);
      setStatus('connected');
    } catch (err) {
      setStatus('disconnected');
      if (err?.name === 'NotFoundError') return; // user closed the chooser
      setError(err?.message || 'Could not connect to the scale.');
    }
  }

  function handleDisconnect() {
    connectionRef.current?.disconnect();
    connectionRef.current = null;
    setStatus('disconnected');
    setDeviceName(null);
    setLiveKg(null);
    setCapturing(null);
  }

  async function handleCapture(step) {
    const conn = connectionRef.current;
    if (!conn || !conn.isConnected()) {
      setError('Connect a scale first, or enter the weight manually.');
      return;
    }
    setError(null);
    setCapturing(step);
    try {
      const kg = await conn.captureReading();
      const reading = { kg, time: new Date(), manual: false };
      if (step === 'pre') setPre(reading);
      else setPost(reading);
    } catch (err) {
      setError(err?.message || 'Could not read from the scale.');
    } finally {
      setCapturing(null);
    }
  }

  function handleManual(step, kg) {
    setError(null);
    const reading = { kg, time: new Date(), manual: true };
    if (step === 'pre') setPre(reading);
    else setPost(reading);
  }

  function handleSave() {
    if (!pre || !post) return;
    const entry = {
      id: nextSessionId++,
      date: post.time,
      preKg: pre.kg,
      postKg: post.kg,
      analysis: analyzeSession(pre.kg, post.kg),
    };
    setHistory((h) => [entry, ...h]);
    setPre(null);
    setPost(null);
  }

  return (
    <div className="app">
      <header className="app-header">
        <div>
          <h1 className="app-title">SoleStepper</h1>
          <p className="app-tagline">Weigh in, work out, rehydrate right.</p>
        </div>
        <UnitToggle unit={unit} onChange={setUnit} />
      </header>

      <ConnectPanel
        btSupported={btSupported}
        status={status}
        deviceName={deviceName}
        liveKg={liveKg}
        unit={unit}
        onConnect={handleConnect}
        onDisconnect={handleDisconnect}
      />

      {error && (
        <div className="error-banner" role="alert">
          {error}
        </div>
      )}

      <WeightStep
        stepNumber={1}
        title="Log Pre-Workout Weight"
        description="Weigh in before you start, ideally after using the bathroom."
        reading={pre}
        unit={unit}
        disabled={false}
        btSupported={btSupported}
        scaleConnected={status === 'connected'}
        capturing={capturing === 'pre'}
        onCapture={() => handleCapture('pre')}
        onCancelCapture={() => connectionRef.current?.cancelCapture()}
        onManual={(kg) => handleManual('pre', kg)}
        onRedo={() => setPre(null)}
      />

      <WeightStep
        stepNumber={2}
        title="Log Post-Workout Weight"
        description="Weigh in right after your workout, toweled off and in similar clothing."
        reading={post}
        unit={unit}
        disabled={!pre}
        btSupported={btSupported}
        scaleConnected={status === 'connected'}
        capturing={capturing === 'post'}
        onCapture={() => handleCapture('post')}
        onCancelCapture={() => connectionRef.current?.cancelCapture()}
        onManual={(kg) => handleManual('post', kg)}
        onRedo={() => setPost(null)}
      />

      {pre && post && <Results pre={pre} post={post} unit={unit} onSave={handleSave} />}

      <History entries={history} unit={unit} />

      <footer className="app-footer">
        SoleStepper offers general hydration guidance only and is not a medical
        device or medical advice.
      </footer>
    </div>
  );
}
