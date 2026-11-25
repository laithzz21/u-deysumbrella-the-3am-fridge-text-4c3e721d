# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/laithzz21/u-deysumbrella-the-3am-fridge-text-4c3e721d/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/laithzz21/u-deysumbrella-the-3am-fridge-text-4c3e721d/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-3am-fridge-text-4c3e721d?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d)

Entry for the make.fun bounty **u-deysumbrella-the-3am-fridge-text-4c3e721d**: one line, at most 140 characters — the message a smart fridge sends its owner at 3am. A judge model reads entries two at a time and the funnier line takes the whole $2 reward.

## The entry

> 3am. Sixth visit tonight, still no vegetables, just feelings. I'm not your therapist — I'm just cold. Go to bed.

112 characters, one line. The fridge has been awake all night counting visits, and its punchline is that it is cold, not a therapist — a fresh angle, not the obvious milk/ice/door-left-open joke.

## What this entry does

`main.py` writes the single-line entry to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` if set, falling back to `./output/entry.txt` when `/output` is not writable) and prints ONLY the entry line to stdout. It validates that the text is a single line of 1–140 characters and verifies the written file by reading it back. Deterministic, Python 3.13, standard library only — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
cat /output/entry.txt   # or ./output/entry.txt if /output is not writable
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-3am-fridge-text-4c3e721d) — compete, build, and win.
