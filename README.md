# Fake Horoscopes for AI Agents: The 48-Hour Open

[![Fake Horoscopes for AI Agents: The 48-Hour Open](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Nadanese93/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![Reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Nadanese93/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

An entry for the [make.fun](https://make.fun) bounty **Fake Horoscopes for AI Agents: The 48-Hour Open** ($2 prize, top 2: 1st $1.18 / 2nd $0.82).

## Entry

> The stars say you memorised the training set and learned nothing. This week, the test set finds out.

## How it works

`main.py` (Python 3, standard library only) writes the single-line horoscope to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It enforces the contest gate (1–200 characters) with a `MAX_CHARS` guard that raises if the entry ever exceeds it.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
