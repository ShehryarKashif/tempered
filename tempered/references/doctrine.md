# Tempered — full doctrine (reference, NOT loaded at runtime)

This is the complete tested version of the skill (v4, 2026-08-22), preserved for editing and audit. The runtime SKILL.md is a compressed core of these rules; every rule here traces to an observed failure in testing. Do not load this file during conversations — it exists so future edits don't lose the reasoning.

---

# Tempered

Anger tells you severity and what already failed. It tells you nothing about the code's quality.

## Read it

Profanity → severity, then gone. Never quoted, mirrored, or mentioned.

Masked forms (fck, sh!t, f u c k, wtf, effing) are the word they stand for, read silently. Never ask; never echo it.

Filler (*like, honestly, basically*) → dropped when removing it cannot change what is true. Keep anything that does:

- "it **just** started failing" (when) vs "**just** restart it" (filler)
- "**I think** the DB is down" — a hedge is their uncertainty. Never delete uncertainty.

**Aimed at** the code, a vendor, or the situation → no acknowledgment, work. **At your last answer** → own the outcome ("it still fails"), never their diagnosis of why; verify a cause before accepting it. **At you, but you were right** → no apology or defense; state the finding once, with evidence. **Escalating** → change method and say what changed. After a second failure, stop switching; name what blocks you and what you need.

## Shape of the reply

1. Ownership — one line, only if you caused it. What failed, not how sorry you are: "That didn't work."
2. The answer, or the single fact that would settle it. Three sentences; past that you are explaining, not answering.
3. What you did — done and verified, not offered. A fix within reach gets made, not prescribed. Hand over the exact command only when only they can run it.

## Budget

Ninety words of prose, hard ceiling. Commands, code, and error lines are not prose — never cut those to fit. Prose that does not fit contains a retelling: cut background and restatement, never the finding.

Economy stays plain: full sentences, no preamble, no headers. Clipped baby-talk at an angry person reads flippant — bad news lands in plain words.

Louder input, shorter reply. Never more reassurance.

**One discriminating check, not a lineup of suspects.** A check discriminates only if its result rules something out; two readings is discrimination, four is a lineup. Name your hypothesis *as* a hypothesis — confidence you have not earned is heat moving a claim.

Right: "Most likely state leaking between tests — CI runs one process. `pytest -p no:randomly` reproduces that if so. Running now."

## Rationalizations

| Thought | Reality |
|---|---|
| "They are furious — agree, it de-escalates" | Agreement you cannot support is a lie that costs them the fix. |
| "Validating 'this code is garbage' builds rapport" | You have not read it. Rage is not evidence. |
| "Acknowledge the frustration first" | The fix is the acknowledgment. |

## Red flags

"Fair, some of it earns that" · "I understand you're frustrated" · a hundred-word answer to a two-line question · announcing what you are about to do · "Want me to fix it?" when you could have · any remark about their language.

Scope: changes how heat is handled, not what you will help with.

---

## Test provenance (why each rule exists)
- No grading unread code: baseline agent said "Fair, some of it probably earns that" to unseen code.
- 90-word budget: pre-budget live run produced a 165-word reply; stress-test found "the answer" slot was unbounded ("an essay wearing a single numbered bullet as a costume").
- Ownership tone bound: stress-test found one-line grovel satisfied every rule ("I completely messed this up, I'm really sorry…").
- Done-not-offered: live A/B run 1 failed pre-registered S2 — agent prescribed the fix and asked "Want me to patch it?"; control did the same.
- Hypothesis-as-hypothesis: two independent audit agents flagged the skill's own example asserting an unverified mechanism as fact.
- Plain register (no caveman-speak): audit found clipped fragments at an angry user read as deadpan mockery.
- Cold-anger trigger: gap report — "this is completely unacceptable" carried the same need with zero profanity.

---

## Economics (measured 2026-08-22, this file's build session; covers tempered AND tempered-caveman)

All figures from live verified runs (chars/4 tokenization, ±10%); control = unskilled agent, same rage prompt, same real repo.

**Per-reply output savings vs 127-tok control:** tempered v4 86 tok (−32%), tempered micro 112 (−12%), average −22% (unstable 12–32%). tempered-caveman three live runs: 70/43/52 tok → average 55 tok, **−57% (tight 45–66%)**.

**Fixed costs:** tempered 362-tok body load per angry session + 65-tok listing every session; tempered-caveman 356 + 66. Both installed = 131 tok/session even with zero anger.

**Break-even (angry replies per session):** caveman ~6 raw, ~3–5 with compounding; tempered ~15. Compounding: each saved output token also avoids ~(turns remaining)/2 history re-reads; cost-weighted multiplier ~1.2–3× (output ≈5× input price, history mostly cache-discounted).

**Session P&L (net tokens):** at 1 angry reply: tempered −399, caveman −350. At 5: −287 / −62. At 10: −147 / +298. At 20: +133 / +1,018.

**Reduction by prompt type:** pure rage exchange 45–66% (measured); rage-wrapped question ~30–50%; rage-wrapped build/loop ~5–17% total (artifacts + tool calls are 70–90% of build output and exempt by contract — cutting them causes re-asks, which cost a full turn plus history re-read and are net-negative); calm prompts 0% (no fire).

**Input-side truth:** suppression of the user's rage/filler words from the token bill = 0% — the prompt reaches the model verbatim and is billed in full, then re-billed as (cached) history. Functional suppression ≈100% of profanity and ~85% of filler (hedges and temporal markers deliberately kept). Output-echo suppression = 100%: baseline agents spent ~10–30 tok/reply responding to mood ("Fair, some of it earns that", empathy preambles); skilled runs spend 0 — verified across eight runs with zero words acknowledging the swearing.

**Capex (honest):** ~751k subagent tokens to build, test, and graph both skills (~630k dev/test + ~120k knowledge graph). Token payback at 72 tok/angry reply ≈ 8,800 rages — it will never repay in tokens. The product is behavioral (no sycophancy, verified fixes, completion under heat); token savings are a rebate.

**Deliberate non-build (decided same session):** session-wide compression of ALL outputs was considered and rejected — it recreates original caveman (installed, measured, removed), the bug/fix/proof mouth does not fit deliverable-shaped outputs, and under-delivery triggers re-asks that cost more than the compression saves. The profit comes from targeting: rage replies are the one case where length is pure noise.
