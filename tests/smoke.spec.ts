import { expect, test, type Page } from '@playwright/test';

const coreRoutes = [
  '/',
  '/projects',
  '/projects/broadcasting-revenue-2015-2024',
  '/research/publications',
  '/research/kim2024-efficiency',
  '/writing',
  '/writing/starting-this-blog',
  '/about',
  '/teaching',
  '/search',
];

async function visitAndAssertNoRuntimeErrors(page: Page, route: string) {
  const pageErrors: string[] = [];
  const consoleErrors: string[] = [];

  const onPageError = (err: Error) => pageErrors.push(err.message);
  const onConsole = (msg: { type(): string; text(): string }) => {
    if (msg.type() === 'error') {
      const text = msg.text();
      if (!text.includes('favicon')) {
        consoleErrors.push(text);
      }
    }
  };

  page.on('pageerror', onPageError);
  page.on('console', onConsole);

  const response = await page.goto(route, { waitUntil: 'networkidle' });
  await expect(response, `No response for ${route}`).not.toBeNull();
  expect(response?.status(), `Unexpected status for ${route}`).toBe(200);

  // Allow deferred scripts/widgets to run and surface console errors.
  await page.waitForTimeout(500);

  page.off('pageerror', onPageError);
  page.off('console', onConsole);

  expect(pageErrors, `pageerror on ${route}`).toEqual([]);
  expect(consoleErrors, `console.error on ${route}`).toEqual([]);
}

test.describe('Major pages smoke', () => {
  for (const route of coreRoutes) {
    test(`loads ${route} without runtime errors`, async ({ page }) => {
      await visitAndAssertNoRuntimeErrors(page, route);
    });
  }
});

test.describe('Key interactions', () => {
  test('projects list filter works', async ({ page }) => {
    await visitAndAssertNoRuntimeErrors(page, '/projects');

    const searchInput = page.locator('#searchInput');
    await expect(searchInput).toBeVisible();
    await searchInput.fill('broadcasting');

    const visibleCards = page.locator('.project-item:visible');
    await expect(visibleCards.first()).toBeVisible();
  });

  test('writing search works', async ({ page }) => {
    await visitAndAssertNoRuntimeErrors(page, '/writing');

    const searchInput = page.locator('#searchInput');
    await expect(searchInput).toBeVisible();
    await searchInput.fill('policy');

    const visibleCards = page.locator('.writing-card:visible');
    await expect(visibleCards.first()).toBeVisible();
  });

  test('research sort buttons are interactive', async ({ page }) => {
    await visitAndAssertNoRuntimeErrors(page, '/research/publications');

    const citationsSort = page.locator('.sort-button[data-sort="citations"]');
    await expect(citationsSort).toBeVisible();
    await citationsSort.click();
    await expect(citationsSort).toHaveClass(/active/);
  });

  test('project detail chart canvases render containers', async ({ page }) => {
    await visitAndAssertNoRuntimeErrors(page, '/projects/broadcasting-revenue-2015-2024');

    const revenueChart = page.locator('#revenueChart');
    const compositionChart = page.locator('#compositionChart');

    await expect(revenueChart).toBeVisible();
    await expect(compositionChart).toBeVisible();
  });

  test('theme toggle switches mode and persists after navigation', async ({ page }) => {
    await visitAndAssertNoRuntimeErrors(page, '/');

    const themeToggle = page.locator('#theme-toggle');
    await expect(themeToggle).toBeVisible();

    const initialDark = await page.evaluate(() => document.documentElement.classList.contains('dark'));
    await themeToggle.click();
    await page.waitForTimeout(150);

    const afterClick = await page.evaluate(() => ({
      dark: document.documentElement.classList.contains('dark'),
      stored: localStorage.getItem('theme'),
    }));

    expect(afterClick.dark).toBe(!initialDark);
    expect(afterClick.stored).toBe(!initialDark ? 'dark' : 'light');

    await page.goto('/about', { waitUntil: 'networkidle' });
    const afterNav = await page.evaluate(() => ({
      dark: document.documentElement.classList.contains('dark'),
      stored: localStorage.getItem('theme'),
    }));

    expect(afterNav.dark).toBe(afterClick.dark);
    expect(afterNav.stored).toBe(afterClick.stored);
  });
});
