/**
 * Chart.js helper utilities for the textbook.
 * Provides consistent theming, factory functions, and dynamic loading.
 */

/** Categorical chart palette — warm, brand-leaning, kept perceptually separable
   for color-vision-deficiency (terracotta primary + a teal-earth and gold anchor,
   not bright SaaS primaries). Lead series is the brand terracotta. */
export const COLORS = {
  blue: '#a85a38',   // terracotta — primary series (brand accent)
  red: '#d6453a',    // warm red
  green: '#3f8f5a',  // earthy green
  amber: '#c9882f',  // gold
  purple: '#834f63', // warm plum
  cyan: '#2f7d72',   // teal-earth
  pink: '#b0617a',   // warm rose
  gray: '#6f6963',   // warm gray
} as const;

/** Ordered array for multi-series charts */
export const PALETTE = [
  COLORS.blue, COLORS.red, COLORS.green, COLORS.amber,
  COLORS.purple, COLORS.cyan, COLORS.pink, COLORS.gray,
];

/** Lotto ball color by number range */
export function ballColor(n: number): string {
  if (n <= 10) return '#f59e0b';
  if (n <= 20) return '#2563eb';
  if (n <= 30) return '#ef4444';
  if (n <= 40) return '#64748b';
  return '#22c55e';
}

/** Lotto ball CSS class by number range */
export function ballClass(n: number): string {
  if (n <= 10) return 'ball-yellow';
  if (n <= 20) return 'ball-blue';
  if (n <= 30) return 'ball-red';
  if (n <= 40) return 'ball-gray';
  return 'ball-green';
}

/** Default Chart.js options for textbook charts */
export const defaultChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  animation: false,
  plugins: {
    legend: { position: 'top' as const },
  },
} as const;

/** Dashed line dataset config (for theoretical reference lines) */
export function theoryLine(label: string, value: number, count: number) {
  return {
    label,
    data: new Array(count).fill(value),
    type: 'line' as const,
    borderColor: '#000',
    borderDash: [6, 4],
    borderWidth: 2,
    pointRadius: 0,
    fill: false,
  };
}
