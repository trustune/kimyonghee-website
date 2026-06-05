---
name: kimyonghee.com
description: A warm, lucid academic portfolio for a media-policy scholar — editorial restraint with a teacher's clarity.
colors:
  ink: "#1a1a1a"
  ink-secondary: "#4a4a4a"
  ink-muted: "oklch(50% 0.012 55)"
  bg: "#ffffff"
  surface: "#f8f6f4"
  border: "#d6d3cf"
  border-light: "#ececea"
  accent: "oklch(50% 0.12 42)"
  accent-hover: "oklch(43% 0.12 40)"
  accent-surface: "oklch(95% 0.022 48)"
  index-amber: "#b45309"
typography:
  display:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "clamp(2.4rem, 1.9rem + 2.5vw, 3.5rem)"
    fontWeight: 400
    lineHeight: 1.3
  headline:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "clamp(1.6rem, 1.35rem + 1.25vw, 2.1rem)"
    fontWeight: 400
    lineHeight: 1.3
  title:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "clamp(1.125rem, 1.05rem + 0.375vw, 1.25rem)"
    fontWeight: 600
    lineHeight: 1.4
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "clamp(1rem, 0.95rem + 0.25vw, 1.0625rem)"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 600
    letterSpacing: "0.08em"
  mono:
    fontFamily: "JetBrains Mono, SF Mono, Consolas, monospace"
    fontSize: "0.9em"
    fontWeight: 400
rounded:
  sharp: "2px"
  soft: "6px"
  pill: "999px"
spacing:
  xs: "0.5rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
  "2xl": "4rem"
components:
  nav-link:
    textColor: "{colors.ink-secondary}"
    typography: "{typography.label}"
  badge:
    backgroundColor: "transparent"
    textColor: "{colors.ink-secondary}"
    rounded: "{rounded.pill}"
    padding: "0.125rem 0.4rem"
  list-card:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg}"
---

# Design System: kimyonghee.com

## 1. Overview

**Creative North Star: "The Reading Room"**

This is a scholar's reading room rendered for the web: a calm, well-lit space where serious media-policy research is made approachable. The system is editorial, not corporate. Serif headlines carry authority while a clean sans body keeps long bilingual reading effortless. Surfaces are quiet and flat; the content — citations, data, findings, weekly intelligence — is the only thing asked to be loud. Warmth comes from the voice and the craft, never from decoration.

It explicitly rejects the look of a generated SaaS product. No purple-to-blue gradients, no identical icon-card grids, no gradient text, no hero-metric template, no marketing-launch theatrics. It also rejects the trap of "warm = beige": warmth is carried by accent, type, and imagery, never by a cream or sand body background. The bar for this brand is distinctiveness with restraint — a site that reads as made by a person who teaches, not assembled by a template.

**Key Characteristics:**
- Editorial serif/sans pairing with a teacher's clarity
- Flat by default; depth lives in typography and whitespace, not shadows
- Bilingual-first (Korean + English are equal citizens)
- Restraint with a pulse: one committed accent, intentional motion, sharp 2px corners
- Substance over hype: data and citations shown plainly

## 2. Colors

A near-monochrome ink-on-white system warmed by a single terracotta accent. The palette is deliberately quiet so content carries the page; the warm accent is a tool of emphasis and wayfinding, used sparingly (the 10% in a 60-30-10 split). The canvas stays true white — warmth lives in the accent and a whisper in the neutrals, never in a tinted background.

### Primary
- **Terracotta** (`oklch(50% 0.12 42)`): The brand accent. Carries warmth where the eye already goes — prose links, link/title hover (`oklch(43% 0.12 40)`), the active nav item, the focus ring, the skip-nav, and the strongest index badges (SSCI / KCI). On dark backgrounds it lifts to a warm terracotta-tan (`oklch(74% 0.11 55)`) for legibility. This is the "warm, approachable" promise made visible without touching the canvas.

### Secondary
- **Index Amber** (#b45309): The original warm hue in the system, reserved for SCIE publication badges. Kept distinct from the terracotta accent so indexing tiers stay readable as separate signals. Scholarly signal only — never decoration.

### Neutral (whisper-warm)
- **Ink** (#1a1a1a): Primary body and heading text. Dark mode: #e6e3df (warm off-white).
- **Ink Secondary** (#4a4a4a): Supporting copy, nav links, footer text. Dark mode: #a8a39d.
- **Ink Muted** (`oklch(50% 0.012 55)`): Dates, captions, fine print only — a warm gray darkened to clear WCAG AA (the former #8a8a8a failed at ~3.5:1). Dark mode: #8a847c.
- **Background** (#ffffff) / **Surface** (#f8f6f4): The true-white page and its barely-warm raised panels (code, inline chips). Dark mode: #0f0f0f / #1a1815.
- **Border** (#d6d3cf) / **Border Light** (#ececea): Whisper-warm hairline dividers between list rows and sections. Dark mode: #2c2926 / #201e1b.

### Named Rules
**The Content-Is-The-Color Rule.** The surface stays near-monochrome so the research is the loudest thing on screen. Any accent appears on a small fraction of a screen; its rarity is what gives it meaning.

**The No-Beige Rule.** Warmth is forbidden from the body background. The canvas is a true white (or true near-black in dark mode). Warmth enters only through the amber accent, type, and imagery. A cream/sand/parchment background is the AI default and is banned here.

## 3. Typography

**Display Font:** Source Serif 4 (with Georgia, Times New Roman fallback)
**Body Font:** Inter (with system-ui fallback)
**Label / Mono Font:** JetBrains Mono (for code and figures)

**Character:** A classic editorial pairing — a humanist serif for headings gives scholarly authority and warmth, while Inter keeps dense bilingual body text neutral and legible. The contrast axis (serif vs. sans) does the work; weights stay modest. (Note: Inter is a common default; its job here is to disappear behind the content, and the serif carries the brand voice.)

### Hierarchy
- **Display** (Source Serif 4, 400, clamp 2.4–3.5rem, lh 1.3): Page-level hero titles. One per page.
- **Headline** (Source Serif 4, 400, clamp 1.6–2.1rem, lh 1.3): Section headings, article H2.
- **Title** (Source Serif 4, 600, ~1.25rem, lh 1.4): Card / list-row titles.
- **Body** (Inter, 400, ~1.0625rem, lh 1.6): Prose. Capped at the `--measure` of 65ch.
- **Label** (Inter, 600, 0.75rem, letter-spacing 0.08em, uppercase): Footer headings and badges only — short labels, never sentences.

### Named Rules
**The Serif-Carries-Voice Rule.** Headings are always the serif; the brand's character lives there. Body and UI chrome stay in Inter. Never set body copy in the display serif, and never set a heading in Inter.

**The 65ch Rule.** Prose line length is capped at 65ch (`--measure`). Long-form research must stay readable; full-width body text is prohibited.

## 4. Elevation

Flat by default. The system conveys depth through whitespace, hairline borders, and typographic hierarchy — not shadows. There is exactly one shadow in the entire chrome: the mobile navigation drawer, where an overlay genuinely needs to lift off the page.

### Shadow Vocabulary
- **Drawer overlay** (`box-shadow: -4px 0 20px rgba(0,0,0,0.1)`): Mobile slide-in nav only. The single sanctioned shadow.

### Named Rules
**The Flat-By-Default Rule.** Surfaces are flat at rest. Cards do not float. If a shadow appears anywhere other than the mobile drawer or a genuine overlay (modal, popover), it is wrong — use a hairline border or a surface tint instead.

## 5. Components

### Navigation
- **Style:** Text links in a sticky header with a 1px bottom border; no pills, no background fills.
- **Typography:** Inter, 0.875rem, secondary ink, `white-space: nowrap`.
- **States:** Default = ink-secondary; hover = full ink; active = full ink with a 1.5px underline at 0.4em offset.
- **Mobile:** Hamburger toggle opens a 280px fixed right-side drawer (the one place a shadow is allowed). Links become full-width rows divided by `border-light`.

### Badges / Chips
- **Style:** Transparent background, 1px border, uppercase, letter-spacing 0.05em — outline chips, never filled.
- **Shape:** `sharp` (2px), `soft` (6px), or `pill` (999px) per use; tag lists use pill.
- **Variants:** Indexing badges carry color (SSCI/KCI = graphite; SCIE = index amber #b45309); tag/category badges stay neutral and drop the uppercase.

### Cards / Containers (list-row pattern)
- **Corner Style:** None — this system uses list rows, not boxed cards.
- **Background:** Page background; no fill.
- **Border:** A single `border-bottom` hairline (`border-light`) separates rows. No enclosing border, no shadow.
- **Internal Padding:** `lg` (1.5rem).
- **Title:** Serif, 600, with link hover shifting to graphite. Excerpts clamp to 2 lines.

### Inputs / Fields
- **Style:** Pagefind-powered search; quiet field with hairline border and `sharp` (2px) corners on `surface`.
- **Focus:** Inherits the global focus-visible treatment (2px graphite outline, 2px offset).

### Buttons
- **Note:** This is a link-driven site; there is no heavy button vocabulary. Actions read as text links or underlined links. The only bare `<button>` is the mobile menu toggle. If a real button is needed, it should be a solid ink fill with `sharp` corners and a verb+object label — never a gradient.

## 6. Do's and Don'ts

### Do:
- **Do** keep the canvas a true white (#ffffff) / true near-black (#0f0f0f). Carry warmth through the amber accent, type, and imagery.
- **Do** set every heading in Source Serif 4 and every body/UI string in Inter.
- **Do** cap prose at 65ch and respect the 4px spacing scale for rhythm.
- **Do** keep surfaces flat; separate content with hairline borders, not shadows.
- **Do** use color on a small fraction of any screen so it keeps its meaning.
- **Do** honor both languages equally; test every layout in Korean and English.
- **Do** meet WCAG AA: body text >=4.5:1, large text >=3:1, visible focus, `prefers-reduced-motion` alternatives.

### Don't:
- **Don't** use a cream / sand / beige / parchment body background. "Warm" never means a warm-tinted canvas here — that is the AI default and is banned.
- **Don't** ship anything that reads as generated SaaS: no purple-to-blue gradients, no identical icon-card grids, no gradient text (`background-clip: text`), no hero-metric template.
- **Don't** use marketing-launch theatrics or buzzwords (혁신 / 최적화 / streamline / empower / next-generation). This is a scholar's site.
- **Don't** introduce `border-left` / `border-right` greater than 1px as a colored stripe on cards, callouts, or blockquotes (the current blockquote 3px left border is a candidate to revisit).
- **Don't** float surfaces with shadows outside the mobile drawer and genuine overlays.
- **Don't** lighten Ink Muted past its tuned WCAG AA floor (`oklch(50% 0.012 55)`); that value already passes 4.5:1 on white, so going lighter for "elegance" breaks legibility.
- **Don't** let the terracotta accent spread past ~10% of a screen; its meaning comes from rarity. Body and headings stay ink.
