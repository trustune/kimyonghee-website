/**
 * Chart.js helper utilities for the textbook.
 * Provides consistent theming, factory functions, and dynamic loading.
 */

/** Categorical color palette (color-blind safe) */
export const COLORS = {
  blue: '#2563eb',
  red: '#ef4444',
  green: '#22c55e',
  amber: '#f59e0b',
  purple: '#7c3aed',
  cyan: '#06b6d4',
  pink: '#ec4899',
  gray: '#64748b',
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
