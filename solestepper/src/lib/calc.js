export const KG_PER_LB = 0.45359237;

export function kgToLb(kg) {
  return kg / KG_PER_LB;
}

export function lbToKg(lb) {
  return lb * KG_PER_LB;
}

export function formatWeight(kg, unit, { signed = false } = {}) {
  const value = unit === 'kg' ? kg : kgToLb(kg);
  const sign = signed && value > 0 ? '+' : '';
  return `${sign}${value.toFixed(1)} ${unit}`;
}

export function formatPercent(pct, { signed = true } = {}) {
  const sign = signed && pct > 0 ? '+' : '';
  return `${sign}${pct.toFixed(1)}%`;
}

// All weights are stored in kg; changeKg < 0 means weight was lost.
export function analyzeSession(preKg, postKg) {
  const changeKg = postKg - preKg;
  const lossKg = Math.max(0, -changeKg);
  const percentChange = (changeKg / preKg) * 100;
  const lossPercent = (lossKg / preKg) * 100;
  return {
    changeKg,
    lossKg,
    percentChange,
    lossPercent,
    // >2% of body weight lost as fluid is the standard threshold where
    // performance/recovery impact is expected and electrolytes matter.
    excessiveLoss: lossPercent >= 2,
    // Standard sports-science guidance: ~1.25-1.5 L per kg lost
    // (~16-24 oz per lb lost).
    rehydration:
      lossKg > 0
        ? {
            litersLow: lossKg * 1.25,
            litersHigh: lossKg * 1.5,
            ozLow: kgToLb(lossKg) * 16,
            ozHigh: kgToLb(lossKg) * 24,
          }
        : null,
  };
}

export function formatFluidRange(rehydration, unit) {
  if (!rehydration) return null;
  if (unit === 'kg') {
    const digits = rehydration.litersHigh < 1 ? 2 : 1;
    return `${rehydration.litersLow.toFixed(digits)}–${rehydration.litersHigh.toFixed(digits)} L`;
  }
  return `${Math.round(rehydration.ozLow)}–${Math.round(rehydration.ozHigh)} oz`;
}

export function formatTime(date) {
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

export function formatDateTime(date) {
  return `${date.toLocaleDateString([], { month: 'short', day: 'numeric' })} · ${formatTime(date)}`;
}
