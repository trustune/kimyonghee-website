/**
 * Shared statistical utility functions.
 * Extracted and generalized from the lotto page's inline computations.
 */

/** Error function approximation (Horner form) */
export function erf(x: number): number {
  const a1 = 0.254829592, a2 = -0.284496736, a3 = 1.421413741;
  const a4 = -1.453152027, a5 = 1.061405429, p = 0.3275911;
  const sign = x < 0 ? -1 : 1;
  x = Math.abs(x);
  const t = 1 / (1 + p * x);
  return sign * (1 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-x * x));
}

/** Standard normal CDF */
export function normCDF(x: number): number {
  return 0.5 * (1 + erf(x / Math.SQRT2));
}

/** Chi-squared survival function (1 - CDF) using Wilson-Hilferty approx */
export function chiSurv(x: number, df: number): number {
  const z = Math.pow(x / df, 1 / 3) - (1 - 2 / (9 * df));
  const se = Math.sqrt(2 / (9 * df));
  return Math.min(1, Math.max(0, 1 - normCDF(z / se)));
}

/**
 * Chi-squared goodness-of-fit test.
 * @param observed - observed frequency counts
 * @param expected - expected count per cell (uniform)
 * @returns { chi: test statistic, p: p-value }
 */
export function chiSquaredTest(observed: number[], expected: number): { chi: number; p: number } {
  let chi = 0;
  for (let i = 0; i < observed.length; i++) {
    chi += Math.pow(observed[i] - expected, 2) / expected;
  }
  const df = observed.length - 1;
  const z = Math.pow(chi / df, 1 / 3) - (1 - 2 / (9 * df));
  const se = Math.sqrt(2 / (9 * df));
  const p = Math.min(1, Math.max(0, 0.5 * (1 + erf(-z / se / Math.SQRT2))));
  return { chi, p };
}

/** Mean of an array */
export function mean(arr: number[]): number {
  return arr.reduce((a, b) => a + b, 0) / arr.length;
}

/** Variance (population) */
export function variance(arr: number[]): number {
  const m = mean(arr);
  return arr.reduce((a, x) => a + (x - m) ** 2, 0) / arr.length;
}

/** Standard deviation (population) */
export function stdDev(arr: number[]): number {
  return Math.sqrt(variance(arr));
}

/** Sample variance (Bessel's correction) */
export function sampleVariance(arr: number[]): number {
  const m = mean(arr);
  return arr.reduce((a, x) => a + (x - m) ** 2, 0) / (arr.length - 1);
}

/** Pearson correlation coefficient */
export function correlation(x: number[], y: number[]): number {
  const n = x.length;
  const mx = mean(x), my = mean(y);
  let num = 0, dx = 0, dy = 0;
  for (let i = 0; i < n; i++) {
    num += (x[i] - mx) * (y[i] - my);
    dx += (x[i] - mx) ** 2;
    dy += (y[i] - my) ** 2;
  }
  return dx === 0 || dy === 0 ? 0 : num / Math.sqrt(dx * dy);
}

/**
 * Autocorrelation function (ACF).
 * @param series - binary or numeric series
 * @param maxLag - maximum lag
 */
export function computeACF(series: number[], maxLag: number): number[] {
  const n = series.length;
  const mu = mean(series);
  const v = series.reduce((a, x) => a + (x - mu) ** 2, 0) / n;
  if (v === 0) return new Array(maxLag + 1).fill(0);
  const acf = [1];
  for (let k = 1; k <= maxLag; k++) {
    let sum = 0;
    for (let t = 0; t < n - k; t++) {
      sum += (series[t] - mu) * (series[t + k] - mu);
    }
    acf.push(sum / (n * v));
  }
  return acf;
}

/**
 * Ljung-Box test for autocorrelation.
 * @returns { Q: test statistic, df: degrees of freedom, p: p-value }
 */
export function ljungBox(acf: number[], N: number, h: number): { Q: number; df: number; p: number } {
  let Q = 0;
  for (let k = 1; k <= h; k++) {
    Q += acf[k] ** 2 / (N - k);
  }
  Q *= N * (N + 2);
  return { Q, df: h, p: chiSurv(Q, h) };
}

/**
 * Simple linear regression (OLS).
 * @returns { slope, intercept, rSquared, residuals }
 */
export function linearRegression(x: number[], y: number[]) {
  const n = x.length;
  const mx = mean(x), my = mean(y);
  let ssxy = 0, ssxx = 0, ssyy = 0;
  for (let i = 0; i < n; i++) {
    ssxy += (x[i] - mx) * (y[i] - my);
    ssxx += (x[i] - mx) ** 2;
    ssyy += (y[i] - my) ** 2;
  }
  const slope = ssxx === 0 ? 0 : ssxy / ssxx;
  const intercept = my - slope * mx;
  const rSquared = ssyy === 0 ? 0 : (ssxy ** 2) / (ssxx * ssyy);
  const residuals = y.map((yi, i) => yi - (slope * x[i] + intercept));
  return { slope, intercept, rSquared, residuals };
}
