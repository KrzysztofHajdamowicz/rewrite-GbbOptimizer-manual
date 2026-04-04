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
- Locale config uses `locale = "en"` (not the deprecated `languageCode`)
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
- Glossary terms: `{{< glossary "PlantId" >}}` — renders as tooltip link, data from `data/glossary.yaml`
- Glossary key derivation: term is lowercased, non-alphanumeric chars stripped (`PlantId` → `plantid`)

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

## Content structure

```
content/
├── getting-started/     # Welcome, Quick Start, How It Works
├── configuration/       # All optimizer modules (9 pages)
├── integrations/
│   ├── inverters/       # Victron, Deye, Goodwe, Afore, Hinen, Sofar
│   ├── connection-methods/  # Solarman, DeyeCloud, GbbConnect2, DongleDirect
│   ├── home-assistant/  # Mosquitto, SolarAssistant, Automation, Charts
│   └── other/           # Evcc, Tuya, Supla
├── mqtt-api/            # Swagger-like MQTT reference (6 pages)
├── reference/           # Glossary, errors, comparisons, mode mappings
└── advanced/            # IoT procedures, GBB Shunt
```

## Adding new content

1. Create `.md` file in the appropriate section
2. Add front matter: `title` and `weight`
3. Use `{{< glossary "Term" >}}` for key terms (must exist in `data/glossary.yaml`)
4. Use `{{< relref "/path" >}}` for cross-links
5. Use native `> [!NOTE]` / `> [!WARNING]` for callouts
6. For MQTT docs, use `mqtt-endpoint` and `mqtt-topic` shortcodes

## Adding glossary terms

Edit `data/glossary.yaml`:
```yaml
termkey:            # lowercase, no special chars
  term: "TermName"  # display name
  short: "One-line definition for tooltips"
  long: "Extended definition for glossary page"
```

## CI/CD

Push to `main` triggers `.github/workflows/deploy.yml`:
1. Installs Hugo Extended 0.160.0 + Go 1.22
2. Builds with `--gc --minify`
3. Deploys to GitHub Pages

Requires GitHub Pages source set to "GitHub Actions" in repo settings.
