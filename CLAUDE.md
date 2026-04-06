# CLAUDE.md — Project conventions for LLM agents

## What is this project?

A Hugo static site rewriting the GbbOptimizer user manual (solar energy battery optimizer). The original docs at `gbboptimizer.gbbsoft.pl/Manual` were a chaotic ~40-page SPA. This repo reorganizes them into a structured, cross-linked documentation site with Swagger-like MQTT API reference.

**Live site:** https://krzysztofahajdamowicz.github.io/rewrite-GbbOptimizer-manual/

## Tech stack

- **Hugo** (Extended) with **hugo-book** theme (installed as Hugo Module, not git submodule)
- **Go modules** for theme dependency (`go.mod` / `go.sum`)
- **GitHub Actions** deploys to **GitHub Pages** on push to `main`
- Custom **SCSS** at `assets/_custom.scss`
- Data files in `data/` (YAML)

## Key conventions

### Hugo specifics

- Theme: `github.com/alex-shpak/hugo-book` — Wiki-style sidebar, collapsible sections, built-in search
- Custom SCSS **must** be at `assets/_custom.scss` (not `assets/scss/custom.scss`) — this is where hugo-book imports it
- `markup.goldmark.renderer.unsafe = true` in `hugo.toml` — required for shortcode HTML output
- **Multilingual**: configured via `[languages]` block in `hugo.toml`. Polish is the default language (`defaultContentLanguage = "pl"`, no URL prefix). English lives under `/en/` prefix.
- `BookTranslatedOnly = true` — language switcher only shows links for pages that have a translation
- Do NOT add `"JSON"` to `[outputs] home` — hugo-book search uses `assets/search-data.json` via JS, not Hugo's JSON output format

### Markdown alerts (not shortcodes)

Use native markdown alerts, NOT `{{< hint >}}`:

```markdown
> [!WARNING]
> Warning text with **bold** and other markdown.

> [!NOTE]
> Info text here.
```

The `{{< >}}` angle-bracket shortcode syntax does NOT process inner markdown — this is why we use native alerts.

### Deprecation overrides

Three layout files override hugo-book templates to fix Hugo v0.156+ deprecations:

| File | What it fixes |
|------|--------------|
| `layouts/baseof.html` | `.Site.LanguageCode` → `.Site.Language.Lang`, `.Language.LanguageDirection` → `.Language.Direction` |
| `layouts/_partials/docs/html-head.html` | `.Site.LanguageCode` → `.Language.Lang` in `hreflang` |
| `layouts/_partials/docs/brand.html` | `.Sites.Default` → `(index hugo.Sites 0)` |

When updating the hugo-book theme, check if these fixes were merged upstream and remove the local overrides if so.

### Cross-linking

- Between pages: `{{< relref "/path/to/page" >}}`
- Glossary terms: `{{< glossary "PlantId" >}}` — renders as tooltip link, data from `data/glossary/<lang>.yaml`
- Glossary key derivation: term is lowercased, non-alphanumeric chars stripped (`PlantId` → `plantid`)
- Glossary shortcode automatically resolves the correct language's data and glossary page via `translationKey`

### MQTT API documentation shortcodes

**`mqtt-endpoint`** — Swagger-like expandable block (`<details>/<summary>`):
```markdown
{{< mqtt-endpoint
  name="CommandName"
  request-topic="{PlantId}/ha_gbb/dataserver/serverrequest"
  response-topic="{PlantId}/ha_gbb/dataserver/serverresponse"
  description="Short description"
>}}
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `command` | string | yes | `"CommandName"` |
{{< /mqtt-endpoint >}}
```

For publish/subscribe (not request/response):
```markdown
{{< mqtt-endpoint name="SignalName" topic="{PlantId}/some/topic" direction="publish" description="Description" >}}
...
{{< /mqtt-endpoint >}}
```

**`mqtt-topic`** — Single topic card (no expandable body):
```markdown
{{< mqtt-topic topic="{PlantId}/path" direction="publish" qos="1" retained="true" description="Description" >}}
```

**`badge`** — Inline colored label:
```markdown
{{< badge "deprecated" >}}  {{< badge "required" >}}  {{< badge "recommended" >}}
{{< badge "victron-only" >}}  {{< badge "deye-only" >}}  {{< badge "beta" >}}
```

### Content weight ordering

Pages use `weight` in front matter to control sidebar order. Lower = higher in sidebar. Section `_index.md` files also have weights.

## Local development

```bash
# Hugo and Go must be in PATH (Homebrew: /opt/homebrew/bin/)
hugo server --buildDrafts --navigateToChanged

# Or use the wrapper script (for environments where PATH isn't set):
./scripts/hugo-server.sh --buildDrafts --navigateToChanged
```

Site serves at `http://localhost:1313/rewrite-GbbOptimizer-manual/`

### Python scripts (uv)

Python scripts (e.g. `originals/convert_html.py`) use **uv** for dependency management. Dependencies are declared in `pyproject.toml`.

```bash
# Run a Python script (uv auto-uses the .venv in the repo root):
uv run python3 originals/convert_html.py

# Add a new dependency:
uv add <package>
```

## Content structure

Content is organized per language using Hugo's `contentDir` approach:

```
content/
├── pl/                        # Polish (default, no URL prefix)
│   ├── wprowadzenie/          # Introduction
│   ├── instalacja/            # Installation (inverters, connection methods)
│   ├── konfiguracja/          # Configuration (9 pages)
│   ├── integracje/            # Integrations (HA, Evcc, Tuya, Supla)
│   ├── mqtt-api/              # MQTT API reference (6 pages)
│   ├── referencje/            # References (glossary, errors, mode mappings)
│   └── zaawansowane/          # Advanced (IoT procedures, GBB Shunt)
└── en/                        # English (URL prefix: /en/)
    ├── introduction/
    ├── installation/
    ├── configuration/
    ├── integrations/
    ├── mqtt-api/
    ├── references/
    └── advanced/
```

### Multilingual conventions

- Each content file **must** have a `translationKey` in front matter to link PL↔EN pages
- Convention: use the Polish filename (without `.md`) as the key, or directory name for `_index.md`
- Example: `translationKey: "szybki-start"` in both `content/pl/wprowadzenie/szybki-start.md` and `content/en/introduction/quick-start.md`
- Glossary data lives in `data/glossary/pl.yaml` and `data/glossary/en.yaml` (same keys, translated values)

## Adding new content

1. Create `.md` file in the appropriate language's content directory (`content/pl/` or `content/en/`)
2. Add front matter: `title`, `weight`, and `translationKey`
3. If adding a translation, use the **same `translationKey`** as the existing page in the other language
4. Use `{{< glossary "Term" >}}` for key terms (must exist in `data/glossary/<lang>.yaml`)
5. Use `{{< relref "/path" >}}` for cross-links
6. Use native `> [!NOTE]` / `> [!WARNING]` for callouts
7. For MQTT docs, use `mqtt-endpoint` and `mqtt-topic` shortcodes

## Adding glossary terms

Edit both `data/glossary/pl.yaml` and `data/glossary/en.yaml`:
```yaml
termkey:            # lowercase, no special chars — must be the same in both files
  term: "TermName"  # display name (usually not translated for technical terms)
  short: "One-line definition for tooltips"
  definition: "Extended definition for glossary page"
```

## CI/CD

Push to `main` triggers `.github/workflows/deploy.yml`:
1. Installs Hugo Extended 0.160.0 + Go 1.22
2. Builds with `--gc --minify`
3. Deploys to GitHub Pages

Requires GitHub Pages source set to "GitHub Actions" in repo settings.
