#!/usr/bin/env python3
"""Describe Your Ex in One Word -- writes one word to /output/entry.txt.

Competition: u-puan-describe-your-ex-in-one-word-9fc6ebe7 (make.fun).
Gate: /output/entry.txt must be UTF-8 text of 1-111 characters, not only
whitespace. The word below is exactly one word, 5 chars, no newline.

Word: extra -- my ex was an extra. A background character with no lines,
and also, of course, so extra: dramatic over everything, all the time.
Two jokes in one word: the film-extra reading (a walk-on part in your
life, instantly forgettable) and the slang reading (over-the-top about
everything). Both readings are verdicts on an ex, so the word lands
whichever way the judge hears it first.

Calibration (judged as a stranger, per the published judge criteria,
each /5; C1 verdict readability, C2 comic punch, C3 surprise,
C4 craft, C5 recognition):
  extra     4 5 4 5 5 = 23  -- double meaning, 5 chars
  refund    5 4 3 5 5 = 22  -- instant verdict, but "want a refund" is a
                            familiar breakup joke (C3 3)
  trailer   4 5 4 4 5 = 22  -- best parts were in the preview; slight
                            trailer-park/truck ambiguity (C4 4)
  cameo     4 4 4 5 4 = 21  -- brief appearance; gentler punch
  draft     4 4 4 5 4 = 21  -- unfinished, never sent; same tier as cameo
  sequel    4 4 3 5 5 = 21  -- "the sequel nobody asked for" is a known
                            frame (C3 3)
  archived  4 3 4 5 4 = 20  -- clever, filed away; mild punch (C2 3)
  pilot     3 4 4 3 4 = 18  -- REJECTED: reads first as airplane pilot,
                            not a TV pilot episode; meaning does not
                            arrive without a caption (C1 3, C4 3)
  Excluded as cliches before scoring: toxic, narcissist, liar, cheater,
  mistake, regret, ghost, redflag -- hundreds of entries will use these.
Head-to-head, top 2: extra vs refund -- refund wins C1 (5-4), extra
wins C2 (5-4) and C3 (4-3), C4/C5 tied; extra wins 2-1. Extra vs
trailer -- tied on C1/C2/C3/C5, extra wins C4 (5-4) and the size
tie-break (5 vs 7 chars). Pick: extra.
"""
import os
import sys
from pathlib import Path

WORD = "extra"


def _gate_ok(word):
    """Mirror of the house gate: 1-111 chars, UTF-8, not only whitespace,
    exactly one word."""
    return (
        1 <= len(word) <= 111
        and word.strip() == word
        and word
        and len(word.split()) == 1
        and word.isascii()
    )


def main():
    if not _gate_ok(WORD):
        print(f"gate failed for word: {WORD!r}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(WORD, encoding="utf-8")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
