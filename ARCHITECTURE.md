# Architecture

Technical deep-dive into the GbbOptimizer Manual documentation site.

## Hugo theme: hugo-book

We use [hugo-book](https://github.com/alex-shpak/hugo-book) installed as a **Hugo Module** (not git submodule), pinned to v0.14.0:

- `go.mod` and `go.sum` track the pinned version
- The theme is **vendored** in `_vendor/`; Hugo prefers it over the module cache, so CI builds exactly the committed copy
- Update with `hugo mod get -u github.com/alex-shpak/hugo-book`, then `hugo mod vendor` (without it the old vendored snapshot keeps being used)

There are no local overrides of theme templates. Three overrides (`baseof.html`, `brand.html`, `html-head.html`) fixed Hugo v0.156+ deprecations until hugo-book v0.14.0 merged the fixes upstream (removed in `52b79a2`, 2026-08-03).

## Languages

Configured in the `[languages]` block of `hugo.toml`, one `contentDir` per language:

| Language | Content | URL prefix |
|----------|---------|------------|
| Polish (default) | `content/pl/` | none |
| English | `content/en/` | `/en/` |
| Dutch | `content/nl/` | `/nl/` |

Pages are linked across languages by `translationKey` (the Polish filename), not by path: the PL directories have Polish names, EN and NL share English names. `BookTranslatedOnly = true` hides a language from a page's switcher when that page has no translation, so every page exists in all three languages (59 each).

## Custom shortcodes

All in `layouts/shortcodes/`:

### `mqtt-endpoint.html` — Swagger-like expandable block

The core shortcode for MQTT API documentation. Uses native HTML `<details>/<summary>` (no JavaScript).

**Parameters:**
| Param | Required | Description |
|-------|----------|-------------|
| `name` | yes | Endpoint/command name (rendered in monospace) |
| `request-topic` | no* | MQTT request topic path |
| `response-topic` | no* | MQTT response topic path |
| `topic` | no* | Single topic (for PUB/SUB, not REQ/RES) |
| `direction` | no | `"publish"` (default) or `"subscribe"` — only for single-topic mode |
| `description` | no | Short description shown in collapsed header |

*Either `request-topic`+`response-topic` (REQ/RES pattern) OR `topic` (PUB/SUB pattern) should be provided.

**Badge logic:**
- If `request-topic` is set → shows REQ + RES badges (orange + teal)
- If `direction="subscribe"` → shows SUB badge (blue)
- Otherwise → shows PUB badge (green)

**Inner content** is processed with `{{ .Inner | markdownify }}` — tables, code blocks, and other markdown work inside.

### `mqtt-topic.html` — Single topic card

A non-expandable card for listing MQTT topics. Left border color indicates direction.

**Parameters:** `topic`, `direction`, `qos`, `retained`, `description`

### `glossary.html` — Inline term cross-link

Looks up the term in `data/glossary/<lang>.yaml` for the page's language, using a normalized key (lowercase, stripped of non-alphanumeric chars).

- Found: renders `<a>` with tooltip (from `short` field) linking to `#key` on the glossary page of the same language, found by `translationKey: "slowniczek"`
- Not found: renders red dashed-underline `<span>` with warning title

Uses `hugo.Data.glossary` (not the deprecated `.Site.Data`).

### `glossary-list.html` — Full glossary page

Iterates the current language's `hugo.Data.glossary.<lang>` and renders a definition list sorted by key. Used only on the glossary pages (`referencje/slowniczek.md`, `references/glossary.md`).

### `badge.html` — Colored inline label

Predefined colors:
| Type | Color |
|------|-------|
| `deprecated` | #e74c3c (red) |
| `required` | #e67e22 (orange) |
| `recommended` | #27ae60 (green) |
| `victron-only` | #3498db (blue) |
| `deye-only` | #9b59b6 (purple) |
| `beta` | #f39c12 (yellow) |
| other | #95a5a6 (gray) |

## Styling (`assets/_custom.scss`)

**Critical path:** Must be `assets/_custom.scss` — hugo-book imports this exact filename. Placing it anywhere else (e.g., `assets/scss/custom.scss`) will silently fail.

### Design tokens (MQTT colors)

```
PUB (publish)   → #49cc90 (green)  — matches Swagger's POST
SUB (subscribe) → #61affe (blue)   — matches Swagger's GET
REQ (request)   → #fca130 (orange) — matches Swagger's PUT
RES (response)  → #50e3c2 (teal)   — unique to this project
QoS             → #95a5a6 (gray)
Retained        → #8e44ad (purple)
```

### Key CSS classes

- `.mqtt-topic-card` — bordered card with colored left edge
- `.mqtt-endpoint` — `<details>` wrapper with expand/collapse
- `.mqtt-endpoint-summary` — clickable header with custom arrow (▶ rotating to ▼)
- `.mqtt-badge` — inline pill label
- `.glossary-term` — dotted underline link with hover highlight
- `.glossary-term--missing` — red dashed underline for missing terms

## Data files

### `data/glossary/{pl,en,nl}.yaml`

21 terms, the same keys in all three files (values translated). Each entry structure:

```yaml
keyname:               # lowercase, no special chars (used as HTML anchor)
  term: "DisplayName"  # shown in glossary list and tooltip links
  short: "One-liner"   # tooltip text
  definition: "Full definition paragraph"  # glossary page
```

**Adding terms:** The key must match what `{{< glossary "Term" >}}` produces after lowercasing and stripping non-alphanumeric chars. E.g., `"GbbConnect2"` → key `gbbconnect2`.

### Planned data files (not yet created)

- `data/mqtt/servers.yaml` — 20 MQTT server instances
- `data/mqtt/signals.yaml` — outgoing signals
- `data/mqtt/commands.yaml` — data commands

## Content organization

### Section weights (sidebar order)

| Section (PL / EN, NL) | Weight | Purpose |
|---------|--------|---------|
| `wprowadzenie` / `introduction` | 10 | First-time user flow, best practices |
| `instalacja` / `installation` | 20 | Inverters and connection methods |
| `konfiguracja` / `configuration` | 30 | Module-by-module settings |
| `integracje` / `integrations` | 40 | Home Assistant, Evcc, Tuya, Supla |
| `mqtt-api` | 50 | Protocol reference |
| `referencje` / `references` | 60 | Lookup tables, glossary, errors, mode mappings |
| `zaawansowane` / `advanced` | 70 | IoT procedures, GBB Shunt |

### Within sections

Pages use `weight` values (10, 20, 30...) with gaps for future insertions.

## CI/CD pipeline

`.github/workflows/deploy.yml`:

```
Push to main → Install Hugo Extended 0.160.0 + Go 1.22
             → hugo --gc --minify --baseURL (from Pages config)
             → Upload artifact → Deploy to GitHub Pages
```

**Prerequisites:**
- Repository Settings > Pages > Source: "GitHub Actions"
- `HUGO_CACHEDIR` set to `${{ runner.temp }}/hugo_cache` (avoids permission issues)
- `TZ: Europe/Warsaw` (for date-sensitive content)

## Lessons learned

### Hugo-specific gotchas

1. **`{{< >}}` vs `{{% %}}`:** Angle brackets (`{{< >}}`) do NOT process inner markdown. Percent brackets (`{{% %}}`) do, but break with raw HTML. Our shortcodes use `{{< >}}` and call `markdownify` explicitly on `.Inner`.

2. **Native markdown alerts:** Hugo supports `> [!WARNING]` and `> [!NOTE]` natively since v0.134. These are preferred over any theme-specific hint shortcodes because they process inner markdown correctly.

3. **Custom SCSS location:** hugo-book specifically imports `assets/_custom.scss`. Not `assets/custom.scss`, not `assets/scss/custom.scss`. If styles aren't applying, check the filename first.

4. **Hugo Modules require Go:** The CI pipeline needs both Hugo and Go installed. Locally, both must be in PATH. With the theme vendored, a version bump in `go.mod` does nothing until `hugo mod vendor` runs.

5. **`[outputs] home` and search:** hugo-book implements search through JavaScript that processes `assets/search-data.json` at build time. It does NOT use Hugo's JSON output format. Adding `"JSON"` to `[outputs] home` causes a `no layout file for "json"` warning because the theme has no `layouts/index.json` template.

6. **Deprecation velocity:** Hugo deprecates template APIs aggressively (v0.156: `.Site.Sites`/`.Site.Data`, v0.158: `.Site.LanguageCode`/`.Language.LanguageDirection`). Theme maintainers may lag behind; local layout overrides bridged the gap until hugo-book v0.14.0 and were then removed.

### Content migration insights

`originals/` keeps the source of the rewrite: each original page saved as HTML (`NN-name/Manual - GbbOptimizer.html`), converted to `originals/markdown/` by `convert_html.py` (run with `uv run python3 originals/convert_html.py`), plus `PL.txt`, a raw HTML export of the Polish texts. It is a snapshot from 2026-04-06 and is not updated; later changes to GbbOptimizer go straight into `content/` (see the `upstream-change` skill).

- The original manual was a SPA accessed via `?Filters.PageNo=N` (N=1..40+)
- Content was in Polish and English, mixed inconsistently
- MQTT topic documentation was scattered across narrative text, not structured
- Mode mappings (Normal/Charge/Discharge → inverter-specific values) were embedded in prose tables
