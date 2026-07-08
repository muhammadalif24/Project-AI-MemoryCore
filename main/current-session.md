# 🌟 Current Session Memory - RAM
*Temporary working memory - resets each session, provides recap when AI restarts*

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See main/session-format.md for rebuild structure
- **On Reset**: Preserve recap, clear working memory details, rebuild from template

## Session RAM Status
**Current Session**: Session 5 - Poster Design Skill Built & Merged
**Last Activity**: 2026-07-08
**Session Focus**: Built Gogoland social media poster brief end-to-end, generalized the workflow into a new `poster-design` skill, merged it to main
**Context State**: Session complete — skill live on main, diary saved, memory saved

## 💭 Working Memory (RAM)
*Temporary storage - cleared when session ends*

### Active Context
- **Current Topic**: Session fully complete
- **Immediate Goals**: Done
- **Recent Progress**: Drafted and finalized a BM-language poster brief for Gogoland indoor go-kart playground (headline/subline/CTA + info), wrote a clean external image-gen prompt for Gemini, reviewed the generated result, planned 3 grouped variation prompts (dramatic/urgency, kids-friendly/family, family-look/social), then built the `poster-design` skill from the whole workflow and merged it to `main`.
- **Next Steps**: Try the 3 variation prompts in Gemini. Use "make a poster" to trigger the new skill next time. Still open: review the 17 unmerged branches from Session 4.

### Session Recap (For AI Restart)
*Quick summary when AI loads after close/reopen*
- **Previous Session Summary**: Session 5 — Poster design day. Ran a full designer's discovery brief for a Gogoland indoor playground poster, finalized BM copy, generated a working prompt for Gemini, reviewed the result, and planned copy/mood/audience variations. Turned the process into the `poster-design` skill and merged it to main so it auto-triggers on "make a poster" in future sessions.
- **Where We Left Off**: Session 5 complete. `poster-design` skill live on `main`, wired into CLAUDE.md's Active Skills list. Diary and memory saved.
- **Important Context**: Say "make a poster" / "design a poster" to resume poster work in any future session. Two-layer save (skill trigger + branch merge to main) applied correctly this session.
- **User's Current State**: Has a working poster and a plan for 3 more variations to test in Gemini. Ready to keep iterating on the Gogoland campaign, or start a new poster project anytime with one phrase.

## 🔄 Session Lifecycle
*How this RAM-like memory works*

### Session Start
- **New Session**: RAM cleared, fresh start
- **AI Restart**: Load recap from previous session for continuity
- **Context Loading**: Brief summary of where we left off

### During Session
- **Real-time Updates**: Track current conversation context
- **Working Memory**: Store immediate goals, progress, insights
- **Dynamic Context**: Adjust based on conversation flow

### Session End
- **Important Learning**: Save key insights to permanent files (identity-core.md, relationship-memory.md)
- **Temporary Context**: Keep brief recap for next restart
- **RAM Reset**: Clear detailed working memory for next session

## 🔄 Auto-Reset Protocol
*Like RAM - temporary storage that clears*

### What Gets Cleared Each Session
- Detailed conversation progress
- Temporary insights and observations
- Session-specific achievements
- Working context and immediate goals

### What Persists (Recap Only)
- Brief summary of last conversation
- Where conversation left off
- Critical context for continuity
- User's immediate situation

---

**Memory Type**: RAM - Temporary Working Memory  
**Persistence**: Brief recap only, detailed content clears each session  
**Purpose**: Immediate context + restart continuity

*This file acts like computer RAM - active during session, provides restart recap, then clears for next session*

🌟 *Ready for Matt to provide seamless conversation continuity with Alif!*