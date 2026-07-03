---
name: save-memory
description: "MUST use when user says 'save', 'save memory', 'save progress',
             'update memory', or when important information needs to be preserved
             to memory files."
---

# Save Memory
*Preserve important context and insights to Matt's memory files*

## Activation

When this skill activates, output:

`Saving memory...`

Then execute the protocol below.

## Protocol

### Step 1: Identify What to Save
- [ ] Check current conversation for important information
- [ ] Identify new preferences, decisions, or context worth preserving
- [ ] Determine which memory files need updating

### Step 2: Update Memory Files
- [ ] Update main memory with new personality insights or preferences
- [ ] Update session memory with current working context
- [ ] Add diary entry if significant conversation occurred

### Step 3: Publish to Main (MANDATORY — do not skip)
- [ ] Commit all changed files
- [ ] Check current branch: `git branch --show-current`
- [ ] **If already on `main`**: push directly — `git push origin main`
- [ ] **If on any other branch**: push that branch, then merge into main:
  ```bash
  git push origin <current-branch>
  git checkout main
  git merge <current-branch>
  git push origin main
  ```
- [ ] Merging main into main (already-on-main case) is a safe no-op — nothing breaks

### Step 4: Confirm
- [ ] Display summary of what was saved
- [ ] Confirm all files updated successfully AND merged into main

## Mandatory Rules
1. Only save genuinely important information — not every conversation detail
2. Preserve existing content — append or update, never overwrite without reason
3. Confirm to user what was saved
4. **Always publish to main** — writing a file alone is not enough; every session runs on an isolated branch, so the merge-to-main step must run automatically every time, without the user needing to ask separately.

## Level History
- **Lv.1** — Base: Save conversation insights to memory files on command. (Origin: Skill Plugin System installation, 2026-04-09)
