/**
 * localStorage-based progress tracking for the textbook.
 */

const STORAGE_KEY = 'textbook-progress';

interface ChapterProgress {
  visited: boolean;
  lastVisit: string;
}

interface TextbookProgress {
  chapters: Record<string, ChapterProgress>;
}

function getProgress(): TextbookProgress {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : { chapters: {} };
  } catch {
    return { chapters: {} };
  }
}

function saveProgress(data: TextbookProgress): void {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  } catch {
    // localStorage unavailable or full
  }
}

/** Mark a chapter as visited */
export function markVisited(chapterSlug: string): void {
  const data = getProgress();
  data.chapters[chapterSlug] = {
    visited: true,
    lastVisit: new Date().toISOString().slice(0, 10),
  };
  saveProgress(data);
}

/** Check if a chapter has been visited */
export function isVisited(chapterSlug: string): boolean {
  return getProgress().chapters[chapterSlug]?.visited ?? false;
}

/** Get count of visited chapters */
export function getVisitedCount(): number {
  return Object.values(getProgress().chapters).filter(c => c.visited).length;
}

/** Get all visited chapter slugs */
export function getVisitedSlugs(): string[] {
  const data = getProgress();
  return Object.entries(data.chapters)
    .filter(([, v]) => v.visited)
    .map(([k]) => k);
}
