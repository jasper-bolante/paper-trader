export default function UnitToggle({ unit, onChange }) {
  return (
    <div className="unit-toggle" role="group" aria-label="Weight unit">
      {['kg', 'lb'].map((u) => (
        <button
          key={u}
          type="button"
          className={unit === u ? 'unit-toggle__btn unit-toggle__btn--active' : 'unit-toggle__btn'}
          aria-pressed={unit === u}
          onClick={() => onChange(u)}
        >
          {u}
        </button>
      ))}
    </div>
  );
}
