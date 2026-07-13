import { formatDateTime, formatFluidRange, formatPercent, formatWeight } from '../lib/calc';

export default function History({ entries, unit }) {
  return (
    <section className="card">
      <h2 className="card__title">Session history</h2>
      {entries.length === 0 ? (
        <p className="step-hint">No sessions saved yet. Complete a pre/post weigh-in to start tracking trends.</p>
      ) : (
        <ul className="history-list">
          {entries.map((entry) => (
            <li key={entry.id} className="history-item">
              <div className="history-item__top">
                <span className="history-item__date">{formatDateTime(entry.date)}</span>
                <span
                  className={
                    entry.analysis.changeKg < 0
                      ? 'history-item__change history-item__change--loss'
                      : 'history-item__change'
                  }
                >
                  {formatWeight(entry.analysis.changeKg, unit, { signed: true })} (
                  {formatPercent(entry.analysis.percentChange)})
                </span>
              </div>
              <div className="history-item__detail">
                {formatWeight(entry.preKg, unit)} → {formatWeight(entry.postKg, unit)}
                {entry.analysis.rehydration && (
                  <> · drink {formatFluidRange(entry.analysis.rehydration, unit)}</>
                )}
              </div>
            </li>
          ))}
        </ul>
      )}
      <p className="history-note">
        History is kept in memory for this visit only and clears when the page reloads.
      </p>
    </section>
  );
}
