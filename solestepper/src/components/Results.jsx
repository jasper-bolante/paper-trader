import { analyzeSession, formatFluidRange, formatWeight } from '../lib/calc';

export default function Results({ pre, post, unit, onSave }) {
  const a = analyzeSession(pre.kg, post.kg);
  const lost = a.changeKg < 0;
  const gained = a.changeKg > 0;

  return (
    <section className="card card--results">
      <h2 className="card__title">Session result</h2>

      <div className="result-hero">
        <span className="big-number">
          {formatWeight(a.changeKg, unit, { signed: true })}
        </span>
        <span className="result-hero__label">
          {lost
            ? `weight lost (${Math.abs(a.percentChange).toFixed(1)}% of body weight)`
            : gained
              ? `weight gained (${a.percentChange.toFixed(1)}% of body weight)`
              : 'no measurable change'}
        </span>
      </div>

      <p className="explain">
        {lost ? (
          <>
            Almost all of this is <strong>fluid lost through sweat</strong>, not
            fat. Real fat or muscle changes happen over weeks, not within a
            single workout — a rapid drop like this should not be read as
            fat loss.
          </>
        ) : gained ? (
          <>
            Weighing more after a workout usually just means you{' '}
            <strong>drank more fluid than you sweated out</strong>. It does not
            mean you gained fat or muscle during the session — body composition
            changes over weeks, not within one workout.
          </>
        ) : (
          <>
            Your weight didn&apos;t measurably change, which suggests your fluid
            intake roughly matched your sweat loss. Nice balance.
          </>
        )}
      </p>

      {a.rehydration && (
        <div className="rehydrate">
          <h3 className="rehydrate__title">Rehydration target</h3>
          <span className="big-number big-number--accent">
            {formatFluidRange(a.rehydration, unit)}
          </span>
          <p className="rehydrate__note">
            Based on ~1.25–1.5 L of fluid per kg lost (~16–24 oz per lb), sipped
            gradually over the next few hours rather than all at once.
          </p>
        </div>
      )}

      {a.excessiveLoss && (
        <div className="caution" role="alert">
          <strong>Heads up: you lost more than 2% of your body weight.</strong>{' '}
          Fluid loss at this level can affect performance and recovery. Consider
          a drink with <strong>electrolytes</strong> (especially sodium) rather
          than plain water only, and go easier on fluids-out next session.
        </div>
      )}

      <p className="disclaimer">
        This is a general guideline, not medical advice. If you have a medical
        condition — for example kidney or heart problems — or you follow a
        fluid-restricted plan, talk to your doctor before using fluid-intake
        targets.
      </p>

      <button type="button" className="btn btn--primary btn--wide" onClick={onSave}>
        Save session &amp; start new
      </button>
    </section>
  );
}
