/**
 * Random number generation and sampling utilities.
 */

/** Draw `count` unique integers from 1..max (sorted). */
export function sampleWithoutReplacement(count: number, max: number): number[] {
  const set = new Set<number>();
  while (set.size < count) {
    set.add(Math.floor(Math.random() * max) + 1);
  }
  return [...set].sort((a, b) => a - b);
}

/** Fisher-Yates shuffle (in-place, returns same array). */
export function shuffle<T>(arr: T[]): T[] {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/** Sample `n` items from `arr` with replacement. */
export function sampleWithReplacement<T>(arr: T[], n: number): T[] {
  const result: T[] = [];
  for (let i = 0; i < n; i++) {
    result.push(arr[Math.floor(Math.random() * arr.length)]);
  }
  return result;
}

/** Generate `n` random values from Normal(mean, sd) using Box-Muller. */
export function randomNormal(n: number, mean = 0, sd = 1): number[] {
  const result: number[] = [];
  for (let i = 0; i < n; i += 2) {
    const u1 = Math.random();
    const u2 = Math.random();
    const z0 = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
    const z1 = Math.sqrt(-2 * Math.log(u1)) * Math.sin(2 * Math.PI * u2);
    result.push(z0 * sd + mean);
    if (i + 1 < n) result.push(z1 * sd + mean);
  }
  return result;
}

/** Generate `n` random values from Uniform(min, max). */
export function randomUniform(n: number, min = 0, max = 1): number[] {
  return Array.from({ length: n }, () => min + Math.random() * (max - min));
}

/** Count matches between two sorted arrays. */
export function matchCount(a: number[], b: number[]): number {
  const set = new Set(b);
  return a.filter(n => set.has(n)).length;
}
