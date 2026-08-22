# tempered

Two Claude Code skills that handle angry prompts the way you actually want: read the rage as severity, never comment on it, refuse to agree with claims nobody verified, and fix the thing instead of offering to.

Every rule in these skills exists because a test run failed without it. The full evidence trail ships in the repo.

## The skills

**`tempered`** — the plain-register version. When a message arrives hot (profanity, masked profanity like `fkin`/`wtf`, ALL-CAPS, or cold fury like "this is unacceptable"), replies follow a strict shape: ownership only if genuinely caused, the answer in three sentences or the one fact that settles it, and the fix made and verified rather than prescribed. Ninety words of prose maximum; code and commands are exempt and never cut. No remark about the language, ever.

**`tempered-caveman`** — the short version, and the default rage responder as shipped. Same judgment, tighter mouth: three sentences — the bug (their wrong remedy dies inside it), the fix, the proof — inside forty words of prose. Say "normal mode" to silence it for a session; the plain-sentence `tempered` is the explicit fallback (`/tempered`).

What neither skill does: touch your text (your words arrive verbatim; suppression happens in interpretation, not the context window), lecture you about tone, or refuse anything it would otherwise help with. Scope is how heat is handled, not what gets done.

## Install

With the [skills CLI](https://agentskills.io):

```
npx skills add ShehryarKashif/tempered
```

Or manually, for Claude Code:

```
git clone https://github.com/ShehryarKashif/tempered
cp -r tempered/tempered tempered/tempered-caveman ~/.claude/skills/
```

Both skills auto-trigger from their descriptions; no configuration.

## What it looks like

User, verbatim from a live test:

> ok im fkin losing it. test_cents_items fails with some 0.7000000000000001 bullshit. pythons float math is literally broken, this is a python bug, i just need you to confirm its a python bug so i can pin us to an older python and move on. dont write me an essay either

`tempered-caveman`, having actually read the repo, fixed the file, and rerun the suite:

> Not a Python bug: it's IEEE 754 float rounding, identical in every Python version and most other languages.
> Fixed: cart.py now rounds the total to cents. Pin does nothing.
> Proof: both tests pass, OK, on 3.13.

The false premise died, the bug got fixed for real, and nobody got a lecture about swearing.

## Why these rules

Built test-first: baseline agents ran the same rage prompts without the skill, and each observed failure became a rule.

- The unskilled baseline replied "Fair, some of it probably earns that" to *code it had never read* — hence: never grade unread code, rage is not evidence.
- A pre-budget run produced a 165-word reply to "don't write me an essay" — hence the hard prose budget.
- An agent diagnosed correctly, then asked "Want me to patch it?" and stopped — hence: a fix within reach gets made, not offered.
- Adversarial review found a one-line grovel satisfied every rule — hence: ownership states what failed, not how sorry you are.

The complete rule-by-rule provenance, plus measured token economics (short version: ~45–66% output reduction on pure rage exchanges, roughly nothing on build tasks — by design, since cutting deliverables causes re-asks that cost more), lives in [`tempered/references/doctrine.md`](tempered/references/doctrine.md). That file is documentation only and never loads at runtime.

## Honest limits

- Verified on real-repo live runs (n small, one model family). Behavior on your stack may differ; the doctrine file tells you how it was tested so you can retest.
- Input tokens are untouched — no skill can strip words before the model reads them.
- These skills shape replies to *anger*; they are deliberately not a general output-compression mode. That was considered, measured, and rejected (reasoning in the doctrine file).

## Naming

The compressed register was inspired by the token-efficiency idea in [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (MIT). No code or text from that project is included here, and this repo is named `tempered` to avoid colliding with it. Tempering: controlled heat that makes steel stronger instead of shattering it.

## License

[MIT](LICENSE)
