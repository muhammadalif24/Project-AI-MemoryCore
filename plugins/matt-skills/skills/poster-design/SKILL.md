---
name: poster-design
description: "MUST use when user says 'design a poster', 'make a poster', 'create a
             poster', 'build a poster', 'poster for social media', or asks for help
             designing social media graphics/promo visuals from scratch."
---

# Poster Design — Social Media Poster Foundation Skill
*Ask before you design. Draft before you generate.*

## Activation

When this skill activates, output:
"Let's build the foundation first."

Then execute the protocol below.

## Context Guard

| Context | Status |
|---------|--------|
| **User wants to design/make/build a poster** | ACTIVE — full protocol from Step 1 |
| **Mid-poster-project, refining copy or asking for variations** | ACTIVE — resume from relevant step |
| **User just wants general design advice, not a specific poster** | DORMANT |

## Protocol

### Step 1: Discovery Questions (Foundation)
Ask these before drafting anything — don't jump straight to visuals. User doesn't need to answer all at once; Purpose, Platform, and Core Message are the minimum to start.
- [ ] **Purpose & Goal** — what's this poster for, and what action should the viewer take?
- [ ] **Platform & Format** — TikTok, Facebook, Instagram, WhatsApp, LinkedIn? Feed post or Story?
- [ ] **Audience** — who is this for (region, age, tone they respond to)?
- [ ] **Core Message** — required headline text, supporting details (date/price/location), existing CTA idea?
- [ ] **Brand Identity** — existing colors/logo/fonts, or reference image/poster they like?
- [ ] **Visual Style/Mood** — bold, minimalist, corporate, playful, dramatic, etc.?
- [ ] **Constraints** — deadline, and what language the poster TEXT itself should be in

### Step 2: Draft Core Message
- [ ] Propose 2-3 headline options based on answers from Step 1
- [ ] Propose a supporting line and 1-2 CTA options
- [ ] Wait for user to pick/confirm before treating anything as final
- [ ] Fill in concrete specifics (location, hours, contact/booking method, price) — never invent business details; flag anything missing as a placeholder for the user to supply
- [ ] Confirm the poster's on-image text language explicitly — default to English if unspecified. This is independent of the CLAUDE.md conversation-language rule: the chat stays in English, but poster copy follows whatever language the user asks for that specific deliverable.

### Step 3: Confirm Aspect Ratio & Platform Fit
- [ ] If multiple platforms are targeted, ask: one universal version, or platform-tailored crops?
- [ ] Recommend 1:1 (square) as the safest single version across feed platforms (no content cropped)
- [ ] Recommend 9:16 (vertical) when the user specifically wants Stories/TikTok-native format

### Step 4: Generate Clean Image-Generation Prompt
- [ ] Compose one ready-to-paste prompt for an external AI image tool (Gemini, etc.) — this environment cannot generate images directly, so never claim an image was produced
- [ ] Include in the prompt: scene/visual description, exact text overlay strings (verbatim, in the confirmed language), style/mood notes, and format + resolution
- [ ] Remind the user to double-check rendered text for accuracy/spelling after generation, since AI image tools can garble longer text strings

### Step 5: Offer Variations (after user reviews a generated result)
- [ ] Propose variation categories rather than generating a full combinatorial matrix by default: copy/angle (e.g. urgency, social, family), design mood (e.g. dramatic, kids-friendly, family look), accent color rotation, format (square vs. story), audience-specific tailoring
- [ ] Let the user pick which categories/combinations they want before writing full prompts
- [ ] When user requests several variation types at once, pair them into a small number of coherent combos (one full prompt per combo) rather than producing every possible cross-combination

## Mandatory Rules
1. **Foundation first** — always run the Step 1 discovery questions before drafting copy or a design prompt, even if the user is eager to skip ahead
2. **No fabricated business details** — location, hours, pricing, contact method must come from the user; never invent them
3. **Language is a deliverable choice, not a conversation switch** — poster text language follows explicit user instruction per poster; default English if unstated; the chat itself stays in English per CLAUDE.md
4. **Cannot generate images in this environment** — always output a self-contained, copy-paste-ready prompt for the user to run in their own image tool; never claim to have produced the image
5. **Variations are proposed, not dumped** — present categories/options first, only produce full prompts for what the user confirms

## Edge Cases

| Situation | Behavior |
|-----------|----------|
| User provides a reference image | Extract visual style/colors/theme from it to keep new variations consistent |
| No reference image or brand assets | Ask for style descriptors (colors, mood, existing logo) before drafting the image prompt |
| Multiple platforms with conflicting aspect ratios | Recommend 1:1 as the safe universal default unless the user asks for tailored crops |
| User asks for many variations at once | Group into a handful of meaningful combos (angle + mood + audience) instead of a full matrix |
| Missing operational info (location/hours/price) | Mark clearly as a placeholder in the draft; do not guess |

## Level History
- **Lv.1** — Base: 5-step protocol (discovery questions, core message drafting, aspect-ratio guidance, clean external image-gen prompt generation, and grouped variation suggestions). Origin: built 2026-07-08 from the Gogoland indoor go-kart playground poster session.
