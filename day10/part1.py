#!/usr/bin/env python3

from collections import defaultdict

bots = defaultdict(list)
low_targets = defaultdict(int)
high_targets = defaultdict(int)
with open("input.txt") as f:
    for line in f:
        splt = line.split()
        if line.startswith("value"):
            val = int(splt[1])
            bot = int(splt[-1])
            bots[bot].append(val)
        elif line.startswith("bot"):
            bot = int(splt[1])
            low_targets[bot] = (int(splt[6]), splt[5])
            high_targets[bot] = (int(splt[11]), splt[10])

for tgt, typ in low_targets.values():
    if typ == "bot" and tgt not in bots:
        bots[tgt] = []
for tgt, typ in high_targets.values():
    if typ == "bot" and tgt not in bots:
        bots[tgt] = []


outputs = {}
while True:
    for bot, chips in bots.items():
        if len(chips) != 2:
            continue
        low, high = min(chips), max(chips)

        if low == 17 and high == 61:
            print(bot)
            exit()

        bots[bot] = []
        low_tgt, low_typ = low_targets[bot]
        high_tgt, high_typ = high_targets[bot]

        if low_typ == "bot":
            bots[low_tgt].append(low)
        else:
            outputs[low_tgt] = low
        if high_typ == "bot":
            bots[high_tgt].append(high)
        else:
            outputs[high_tgt] = high
