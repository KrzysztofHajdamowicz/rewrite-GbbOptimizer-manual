---
name: upstream-change
description: Use when documenting something new or changed in GbbOptimizer in this manual — a new MQTT command or signal, a changed setting, a new integration, or a page of the official manual (gbboptimizer.gbbsoft.pl/Manual) that changed since the rewrite.
---

# Documenting a change in GbbOptimizer

This site is an unofficial rewrite; GbbOptimizer and its official manual
belong to Gbbsoft. `originals/` is a frozen snapshot of the official manual
from 2026-04-06 and is never updated. Every later change goes straight into
`content/`, one feature per PR, in all three languages.

## Before writing

1. Get the source. A fact about GbbOptimizer's behaviour comes from the
   official manual, Gbbsoft (relayed by Krzysztof) or Krzysztof himself. If
   the request doesn't say where the change comes from, ask; don't infer
   payloads, topics or defaults from similar commands. Put the source in the
   PR description.
2. Find where it belongs. The structure differs from the original's page
   numbering:
   - MQTT data commands → `mqtt-api/komendy-danych.md` (PL) and
     `mqtt-api/data-commands.md` (EN, NL)
   - MQTT signals → `mqtt-api/sygnaly.md` / `mqtt-api/signals.md`
   - settings → `konfiguracja/` / `configuration/`
   - integrations → `integracje/` / `integrations/`

   `grep -rln '<related term>' content/pl` finds the PL page; its
   `translationKey` finds the EN and NL twins.
3. Read the neighbouring entries on that page and copy their shape (the
   field table, the example, the `mqtt-endpoint` parameters).

## Writing

- **PL, EN and NL in the same PR.** A page missing in one language
  disappears from that language's switcher. The first SetAutoCharging
  commit covered only PL and EN, and NL followed in a second one; check all
  three with `git diff --stat` before committing.
- MQTT entries use the `mqtt-endpoint` / `mqtt-topic` shortcodes (see
  `CLAUDE.md`); topic placeholders stay `{PlantId}`. Field names, topic paths
  and JSON examples are identical in all three languages; only the prose is
  translated.
- New terms go into `data/glossary/{pl,en,nl}.yaml` with the same key.
- Callouts are native `> [!NOTE]` / `> [!WARNING]`, never `{{< hint >}}`.
- If the change also affects a narrative page (as SetPVForecast did for the
  best-practices page), update that page too, in all three languages.
- Never put a real PlantId, Plant Token or any other credential in an
  example.

## Verification

```sh
hugo --gc --minify          # must build without errors or warnings
hugo server --buildDrafts --navigateToChanged
```

Open the changed page in all three languages
(`http://localhost:1313/rewrite-GbbOptimizer-manual/`, `/en/…`, `/nl/…`),
check that the language switcher links them and that expandable MQTT blocks
render.

## After merge

Pushing to `main` deploys GitHub Pages. GbbSupportBot reads `content/pl` and
`content/en` from `origin/main` at its next hourly corpus build, so the bot
can answer from the change within the hour (NL is not in its corpus).
