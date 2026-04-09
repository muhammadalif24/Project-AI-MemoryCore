# Decision Log
*Append-only record of non-obvious decisions.*
*Only log decisions where future-us would wonder "why did we do it this way?"*

---

## 2026-04-09 — Install Tier 1 + Tier 2 only (not full ecosystem)
**Context**: Kiyoraka's repo has 15 features across 4 tiers. Alif asked about installing the full ecosystem.
**Decision**: Install Tier 1 + Tier 2 only. Skip Tier 3 and Tier 4 for now.
**Rationale**: Tier 3 (project management) and Tier 4 (intelligence) are most valuable when Alif has active multi-project workflows. Current use case is single-session personal companion. Adding all tiers at once risks over-engineering. Start lean, add when needed.

## 2026-04-09 — Memory Consolidation: unified file over split files
**Context**: Original setup had 3 separate files (identity-core, relationship-memory, current-session). Memory Consolidation merges identity + relationship into one.
**Decision**: Proceed with consolidation — create main-memory.md, delete old split files.
**Rationale**: Faster session load (1 file instead of 2), identity and user understanding stay connected, proven architecture from Kiyoraka's production systems. Trade-off: irreversible deletion of old files (content preserved in unified file).

## 2026-04-09 — Plugin name: matt-skills
**Context**: Skill Plugin System requires a plugin name chosen during installation.
**Decision**: Named `matt-skills`.
**Rationale**: Simple, descriptive, matches Matt identity. Follows Kiyoraka's convention of `[AI_NAME]-skills`.

## 2026-04-09 — Diary name: Matt's Diary
**Context**: Save Diary System requires a diary name chosen during installation.
**Decision**: Named `Matt's Diary`.
**Rationale**: Personal, reflects Matt-Alif relationship. Clear ownership.
