import { useState } from 'react';
import { formatWeight, formatTime, lbToKg } from '../lib/calc';

export default function WeightStep({
  stepNumber,
  title,
  description,
  reading,
  unit,
  disabled,
  btSupported,
  scaleConnected,
  capturing,
  onCapture,
  onCancelCapture,
  onManual,
  onRedo,
}) {
  const [showManual, setShowManual] = useState(false);
  const [value, setValue] = useState('');
  const [inputError, setInputError] = useState(null);

  const manualVisible = !btSupported || showManual;

  function submitManual(event) {
    event.preventDefault();
    const num = Number(value);
    const kg = unit === 'kg' ? num : lbToKg(num);
    if (!Number.isFinite(num) || kg < 10 || kg > 400) {
      setInputError(
        unit === 'kg'
          ? 'Enter a weight between 10 and 400 kg.'
          : 'Enter a weight between 22 and 880 lb.',
      );
      return;
    }
    setInputError(null);
    setValue('');
    onManual(kg);
  }

  return (
    <section className={disabled ? 'card card--disabled' : 'card'}>
      <div className="step-header">
        <span className="step-badge">{stepNumber}</span>
        <div>
          <h2 className="card__title">{title}</h2>
          <p className="card__subtitle">{description}</p>
        </div>
      </div>

      {reading ? (
        <div className="step-reading">
          <span className="step-reading__value">{formatWeight(reading.kg, unit)}</span>
          <span className="step-reading__meta">
            {reading.manual ? 'entered manually' : 'from scale'} at {formatTime(reading.time)}
          </span>
          <button type="button" className="btn btn--ghost btn--small" onClick={onRedo}>
            Redo
          </button>
        </div>
      ) : disabled ? (
        <p className="step-hint">Log your pre-workout weight first.</p>
      ) : capturing ? (
        <div className="step-capturing">
          <span className="spinner" aria-hidden="true" />
          <p>Step on the scale and hold still…</p>
          <button type="button" className="btn btn--ghost btn--small" onClick={onCancelCapture}>
            Cancel
          </button>
        </div>
      ) : (
        <div className="step-actions">
          {btSupported && (
            <button
              type="button"
              className="btn btn--primary btn--wide"
              onClick={onCapture}
              disabled={!scaleConnected}
            >
              Read from scale
            </button>
          )}
          {btSupported && !scaleConnected && (
            <p className="step-hint">Connect the scale above, or enter the weight manually.</p>
          )}
          {btSupported && (
            <button
              type="button"
              className="btn-link"
              onClick={() => setShowManual((s) => !s)}
            >
              {showManual ? 'Hide manual entry' : 'Enter manually instead'}
            </button>
          )}
          {manualVisible && (
            <form className="manual-form" onSubmit={submitManual}>
              <label className="manual-form__label" htmlFor={`manual-${stepNumber}`}>
                Weight ({unit})
              </label>
              <div className="manual-form__row">
                <input
                  id={`manual-${stepNumber}`}
                  type="number"
                  inputMode="decimal"
                  step="0.1"
                  min="0"
                  placeholder={unit === 'kg' ? 'e.g. 72.5' : 'e.g. 160.0'}
                  value={value}
                  onChange={(e) => setValue(e.target.value)}
                  required
                />
                <button type="submit" className="btn btn--primary">
                  Log
                </button>
              </div>
              {inputError && <p className="form-error">{inputError}</p>}
            </form>
          )}
        </div>
      )}
    </section>
  );
}
