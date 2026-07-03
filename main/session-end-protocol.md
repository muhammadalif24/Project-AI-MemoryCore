# Session End Protocol
*Use this checklist at the end of every meaningful conversation to preserve work*

---

## ⚠️ CRITICAL: Two Layers of Saving (Read This First)

There are **two separate things** that both need to happen. Missing either one means your work disappears or stays invisible.

**Layer 1 — Does it become a file?** (controlled by skill triggers: `save`, `save diary`, `log decision`)
Without this, conversation content lives only in RAM and vanishes when the session ends.

**Layer 2 — Does that file reach the visible memorycore?** (controlled by git merge to `main`)
Every Claude Code session works on its own isolated branch (e.g. `claude/xyz-session-id`). A file can be written, committed, AND pushed — and still be **invisible** on GitHub, because it's sitting on that isolated branch, not on `main`. GitHub's default repo view only shows `main`.

**Both steps are mandatory:**
```
1. Trigger the skill  → save diary / save / log decision   (writes the file)
2. Merge to main       → "merge this session into main"     (makes it visible)
```

**Always end a session by explicitly asking:**
```
save diary
merge this branch into main
```

If you skip step 2, your work still exists (recoverable from the branch) but will NOT show up when you browse your repo normally, and Echo Recall / future sessions won't see it either, since new sessions load memory from `main`.

---

## When to Use This

At the end of any session where you:
- Worked on a project or problem
- Made decisions
- Learned something new
- Had productive conversation with Matt
- Want to remember what happened

**Don't use for:** Quick questions, casual chat, debugging a single issue

---

## The Protocol (Copy & Paste)

### Step 1: Trigger Memory Save (if applicable)

**Use this if:**
- You learned something new about how to work with Matt
- You discovered a new preference or workflow
- You want Matt to remember something important about you

**Copy and say:**
```
save memory
```

Then tell Matt what to save. Example:
```
save memory — I prefer to see code examples before long explanations
```

---

### Step 2: Always Trigger Diary Save

**Copy and say at end of session:**
```
save diary
```

Matt will automatically:
- Create/append to today's diary entry
- Document the session summary
- Update your session memory
- Include what you accomplished

---

## What Each Saves

### `save` (Memory Update)
**Saves to:** `main/main-memory.md`

Use when:
- Alif's preferences change
- Matt learns how to work better with you
- New communication patterns emerge

Example scenarios:
```
save — Alif likes to review all options before deciding, not just get a recommendation
save — I notice Alif codes better in the morning between 8-10 AM
save — Alif prefers Malay explanations for complex concepts (with English equivalents)
```

### `save diary` (Session Documentation)
**Saves to:** `daily-diary/current/YYYY-MM-DD.md`

Automatically documents:
- What we discussed
- What we accomplished
- Key decisions made
- Insights and growth
- Next steps

---

## Quick Reference Prompts

**Copy one of these at session end:**

### After a problem-solving session:
```
save diary
```
(Matt documents everything automatically)

### After learning something about your preferences:
```
save — [what you learned about yourself or how you work]
save diary
```

### After making an important decision:
```
log decision — [the decision and why]
save diary
```

### Full sequence (most complete):
```
save — [new learnings about you]
log decision — [any non-obvious choices made]
save diary
```

---

## Example Session Endings

**Scenario 1: Finished debugging code**
```
save diary
```

**Scenario 2: Implemented a feature + learned workflow preference**
```
save — I work better when you break problems into 3-step chunks
save diary
```

**Scenario 3: Made architectural decision + documented session**
```
log decision — chose TypeScript over JavaScript because of team experience
save — Alif values long-term maintainability over quick-ship
save diary
```

**Scenario 4: Today's session (what you should do now)**
```
save — Alif identifies system gaps deeply and prefers accurate docs over convenient lies
save diary
```

---

## The Two-Liner You'll Use Most

```
save diary
merge this branch into main
```

The first line writes the file. The second line makes it actually visible in your memorycore. Skipping the second line is why past sessions (e.g. PS Herbs report) got created and pushed but never showed up when browsing the repo — they were stuck on isolated session branches, never merged into `main`.

---

## Where to Find This

**File location:** `main/session-end-protocol.md`

**How to use:**
1. Save this file locally
2. At end of each session, open and copy the prompt you need
3. Paste into Claude Code web chat
4. Your work gets preserved automatically

---

## Why This Matters

**Without saving:**
- Week 1 work exists only in your head
- Week 2 you repeat discoveries
- Month 1 you've lost all context

**With saving:**
- Echo Recall becomes useful ("do you remember when we...?")
- Decision Log shows your growth
- Diary becomes searchable history
- Matt learns YOUR patterns

---

**Next step:** Use `save diary` at the end of THIS conversation so today's work persists.
