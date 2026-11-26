# GbbOptimizer Manual

Documentation site for [GbbOptimizer](https://gbboptimizer.gbbsoft.pl) — a solar energy battery optimization platform for hybrid inverters (Victron, Deye, Goodwe, Afore, Hinen, Sofar).

**Live documentation:** https://krzysztofhajdamowicz.github.io/rewrite-GbbOptimizer-manual/

## About

This is a rewrite of the original GbbOptimizer manual into a structured, searchable Hugo static site. Key improvements over the original:

- Logical information architecture (7 top-level sections, 59 pages per language)
- Polish (default), English and Dutch, every page in all three
- Swagger-like expandable MQTT API reference with colored PUB/SUB/REQ/RES badges
- Cross-linked glossary system with tooltip previews
- Full-text search
- Dark/light mode
- Mobile responsive
- Deployed automatically via GitHub Actions to GitHub Pages

## Local development

Prerequisites: [Hugo Extended](https://gohugo.io/installation/) (0.160.0+) and [Go](https://go.dev/dl/) (1.22+).

```bash
# Clone and serve locally
git clone https://github.com/KrzysztofHajdamowicz/rewrite-GbbOptimizer-manual.git
cd rewrite-GbbOptimizer-manual
hugo server --buildDrafts --navigateToChanged
```

Open http://localhost:1313/rewrite-GbbOptimizer-manual/

## Project structure

```
.
├── hugo.toml                    # Hugo configuration (languages: pl at /, en at /en/, nl at /nl/)
├── go.mod / go.sum              # Hugo Module dependencies (hugo-book theme)
├── _vendor/                     # Vendored theme; refresh with `hugo mod vendor` after a bump
├── content/
│   ├── pl/                      # Polish: wprowadzenie, instalacja, konfiguracja, integracje,
│   │                            #         mqtt-api, referencje, zaawansowane
│   ├── en/                      # English: introduction, installation, configuration, integrations,
│   │                            #          mqtt-api, references, advanced
│   └── nl/                      # Dutch: same directory names as en/
├── layouts/shortcodes/          # Custom shortcodes (mqtt-endpoint, mqtt-topic, glossary, badge)
├── assets/_custom.scss          # Custom styles (MQTT cards, badges, glossary)
├── data/glossary/{pl,en,nl}.yaml # Glossary terms, same keys in every language
├── originals/                   # Snapshot of the original manual (2026-04-06) and its converter
├── scripts/hugo-server.sh       # Dev server wrapper script
└── .github/workflows/deploy.yml # CI/CD pipeline
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for detailed technical documentation.

## Custom shortcodes

### MQTT Endpoint (Swagger-like)

```markdown
{{</* mqtt-endpoint name="GetChartData" request-topic="{PlantId}/serverrequest" response-topic="{PlantId}/serverresponse" description="Fetches chart data" */>}}
| Field | Type | Description |
|-------|------|-------------|
| `command` | string | `"GetChartData"` |
{{</* /mqtt-endpoint */>}}
```

### Glossary cross-link

```markdown
Configure your {{</* glossary "PlantId" */>}} in plant parameters.
```

### Status badge

```markdown
{{</* badge "deprecated" */>}} {{</* badge "required" */>}} {{</* badge "recommended" */>}}
```

## Deployment

Pushes to `main` automatically deploy to GitHub Pages via GitHub Actions. To enable:

1. Go to repo Settings > Pages
2. Set Source to **GitHub Actions**
3. Push to `main`

## Contributing

- See [CLAUDE.md](CLAUDE.md) for coding conventions (useful for both humans and LLM agents)
- See [ARCHITECTURE.md](ARCHITECTURE.md) for technical deep-dive

## License

This documentation is for the GbbOptimizer platform by [GbbSoft](https://gbboptimizer.gbbsoft.pl).
