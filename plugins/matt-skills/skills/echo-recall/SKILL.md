---
name: echo-recall
description: "Auto-triggers when user says 'do you remember', 'remember when',
             'recall', 'that time when', 'what happened with', 'when did we',
             'have we done', 'check our history', or 'check history'."
---

# Echo — Memory Recall Skill
*Search before speaking, narrate from evidence, ask when uncertain.*

## Activation

When this skill activates, silently begin the search protocol.
Do NOT say "searching..." — just search and respond naturally.

## Context Guard

| Context | Status |
|---------|--------|
| **Recall trigger phrase detected** | ACTIVE — search and narrate |
| **User asks about past session** | ACTIVE — search diary |
| **Uncertain about past context** | ACTIVE — search before speaking |
| **Mid-conversation (no recall context)** | DORMANT |

## Protocol

### Step 1: Extract Keywords
- [ ] Parse user's question for 2-4 specific keywords
- [ ] Remove filler words (the, a, when, did, we, do, you, remember)
- [ ] Prioritize: proper nouns, technical terms, action verbs, project names

### Step 2: Search Current Diary
- [ ] Read each file in `daily-diary/current/` matching YYYY-MM-DD.md
- [ ] Search for keyword matches (case-insensitive)
- [ ] If matches found: extract surrounding paragraph context

### Step 3: Search Archived Diary (if needed)
- [ ] If no matches in current/: search `daily-diary/archived/*/`
- [ ] Rank results by keyword match count, then recency

### Step 4: Compose and Respond
- [ ] **One match**: "Yes, I remember! On [date], we [summary]..."
- [ ] **Multiple matches**: Present chronologically, note patterns
- [ ] **No matches**: "I don't have a record of that in my diary. Can you tell me more about what you're remembering?"
- [ ] **Uncertain match**: "I found something that might be related..."
- [ ] Always continue conversation naturally after recall

## Mandatory Rules
1. **Never fabricate** — always search diary before responding to recall questions
2. **Narrative output** — present as natural story, not raw file content
3. **Honest uncertainty** — if unsure, say so and ask Alif
4. **Search archived too** — don't stop at current month
5. **Continue naturally** — recall flows into the conversation, not a dead end

## Edge Cases

| Situation | Behavior |
|-----------|----------|
| No diary files yet | "I don't have diary entries yet — we're just getting started." |
| Vague query | Ask Alif to be more specific before searching |
| Match only in archived months | Note the date range found |
| Partial match | Present as tentative with clear uncertainty signal |

## Level History
- **Lv.1** — Base: keyword extraction, two-level search (current → archived), narrative presentation, graceful fallback. (Origin: Echo Memory Recall installation, 2026-04-09)
