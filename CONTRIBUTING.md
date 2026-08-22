# Contributing

The rule of this repo: **no edit without a failing test first.** Every rule in these skills traces to an observed failure (see `tempered/references/doctrine.md`), and changes are held to the same standard.

To propose a change:

1. Show the failure: a real prompt where the current skill misbehaves, with the actual reply.
2. Make the minimal edit that fixes it.
3. Show a rerun where the edit holds — a live run with tools beats a text-only roleplay (text-only agents have been observed never reading the skill file at all; check tool-use counts).
4. Update the doctrine file's provenance section with the new failure → rule pair.

Word budgets are part of the contract: `tempered/SKILL.md` stays under 500 body words. Pay for additions with deletions.
