# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static project website for an IJCAI-ECAI 2026 survey paper on adversarial robustness in embodied AI. Deployed to GitHub Pages via `deploy.sh`. Single-file, no build step.

## Repository Structure

- `index.html` — Single-page website. All CSS inlined in `<style>`, search/filter logic in a `<script>` at the end. No external dependencies.
- `framework_01.png` — Framework diagram image embedded in the page.
- `deploy.sh` — Pushes `main` branch to GitHub Pages remote. Run from repo root: `bash deploy.sh`.
- `example_project/` — Reference example (saved webpage from ai45lab.github.io). Vue + Vuetify based; styles were referenced from here.

## index.html — Page Sections (top to bottom)

1. **Header** — Title, author list with affiliation superscripts, affiliation names, Paper / Project Page buttons (pill-shaped).
2. **Abstract** (`section.section-abstract`) — Has a blue-to-purple gradient border (CSS `padding-box` / `border-box` trick). Contains the survey abstract.
3. **Framework Overview** — Embeds `framework_01.png` with a caption.
4. **Key Contributions** — 3-column card grid (`highlights` / `highlight-card`). Each card has a title and description.
5. **Surveyed Papers** — Searchable, filterable paper list (details below).
6. **Contact** — Email links for the two contact authors.
7. **Footer** — Copyright line.

## Surveyed Papers Section — How It Works

### Structure
- **Search box** — filters cards in real time by matching against all visible text (title, author, tags).
- **Filter buttons** — `All / Perception / Decision & Planning / Execution`. Filters by the functional stage of each paper. Uses `data-tags` attribute on each `<article class="paper-card">`.
- **Legend** — 3 color categories explained (see below).
- **Paper cards** — Each card is an `<article class="paper-card" data-tags="...">` containing:
  - `.paper-top` — title link + tag pills (side by side on desktop, stacked on mobile).
  - `.paper-foot` — first author, date pill, external-link icon.

### Tag Color System (3 categories, matching example project)

| Color  | CSS classes                              | Meaning             |
|--------|------------------------------------------|---------------------|
| Blue   | `.pill-perception` `.pill-decision` `.pill-execution` | Stage (functional layer) |
| Purple | `.pill-attack` `.pill-defense`           | Type (attack or defense) |
| Green  | `.pill-physical` `.pill-benchmark`       | Context             |

### Adding or Editing a Paper

Copy an existing `<article>` block and update:
1. `data-tags` — space-separated stage keywords: `perception`, `decision`, `execution`. Include all that apply (a paper can span multiple stages).
2. `.paper-title` `href` — link to the paper (e.g. arXiv).
3. Tag pills — pick from the 3-color system above.
4. `.paper-author` — first author + "et al."
5. `.paper-date` — `YYYY.MM` format.
6. Update the paper count text in `<span id="paper-count">` if needed (auto-updates on filter/search, but the initial value is hardcoded).

### Search / Filter JS Logic

Located in the `<script>` block at the bottom of `<body>`. No framework; plain `addEventListener`.
- `searchInput` event → checks `card.textContent.toLowerCase().includes(query)`.
- `filterBtn` click → checks `card.dataset.tags.includes(activeFilter)`.
- Both conditions must be true for a card to be visible. The `#paper-count` span updates automatically.

## Key CSS Patterns Used

- **Pill buttons**: `border-radius: 50px` (from example's `.action-btn`).
- **Gradient border**: `background: linear-gradient(...) padding-box, linear-gradient(...) border-box` + `border: 2px solid transparent` (from example's `.abs-wrap`). Used on the Abstract section.
- **Responsive title**: `font-size: clamp(1.8em, 4vw, 2.5em)` auto-scales with viewport.
- **Card hover lift**: `transform: translateY(-3px)` + deeper `box-shadow` on `:hover`.
- **Responsive breakpoint**: `@media (max-width: 768px)` — stacks affiliations, toolbar, and paper card internals vertically; title text wraps.

## Placeholder Links

- Paper button → `ijcai26.pdf` (not yet in repo).
- Project Page button → `https://dyamik.github.io/IJCAI-ECAI-26/`.
- All paper card `href` values are currently `#` — replace with real arXiv links.
- Paper titles and authors in the list are placeholder entries matching the survey's taxonomy; replace with actual cited works.

## Deployment

```bash
bash deploy.sh   # commits everything and pushes to origin/main (GitHub Pages)
```

Preview locally: open `index.html` directly in a browser, or `python3 -m http.server`.

