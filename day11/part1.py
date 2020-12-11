#!/usr/bin/env python3

from itertools import combinations
from collections import deque


def disp(all_objects, floors):
    l = []
    for i, obj in enumerate(all_objects):
        elem, typ = obj.split()
        l.append(elem[0] + typ[0] + str(floors[i]))
    return tuple(l)

floor_contents = {}
with open("input.txt") as f:
    lines = f.read().strip().replace("-compatible", "").split("\n")

for i in range(3):
    floor_contents[i] = (
        lines[i][lines[i].find("a ") :]
        .replace(".", "")
        .replace(", and", ",")
        .replace("and ", ",")
        .replace("a ", "")
        .rstrip()
        .replace(", ", ",")
        .split(",")
    )
floor_contents[3] = []

all_objects = []
for i in range(3):
    all_objects.extend(floor_contents[i])

init = []
for obj in all_objects:
    for i in range(3):
        if obj in floor_contents[i]:
            init.append(i)
assert len(init) == len(all_objects)

steps = {}
q = deque([(tuple(init), 0, 0)]) # init stats, first floor, 0 steps taken

while q:
    n, f, s = q.popleft()
    if (n,f) in steps:
        steps[(n, f)] = min(steps[(n,f)], s)
        continue

    if n == tuple([3] * len(all_objects)):
        print(s)
        break

    steps[(n, f)] = s

    # PRNT = False

    for nf in [f-1, f+1]:
        if nf < 0 or nf > 3:
            continue

        choices = [i for i, v in enumerate(n) if v == f]

        for fst, snd in combinations(choices, 2):
            fstelem, fsttyp = all_objects[fst].split()
            sndelem, sndtyp = all_objects[snd].split()
            if fsttyp != sndtyp and fstelem != sndelem:
                continue

            nxt = list(n)
            nxt[fst] = nf
            nxt[snd] = nf
            next_inds = [i for i, v in enumerate(nxt) if v == nf]
            next_generators = [i for i in next_inds if all_objects[i].endswith("generator")]

            valid = True
            next_objs = [all_objects[i] for i, f in enumerate(nxt) if f == nf]
            for obj in next_objs:
                elem, typ = obj.split()
                if typ == "microchip":
                    valid = valid and (not next_generators or f"{elem} generator" in next_objs)

                if not valid:
                    break

            if valid:
                q.append((tuple(nxt), nf, s+1))

        for c in choices:
            nxt = list(n)
            nxt[c] = nf
            next_inds = [i for i, v in enumerate(nxt) if v == nf]
            next_generators = [i for i in next_inds if all_objects[i].endswith("generator")]

            valid = True
            next_objs = [all_objects[i] for i, f in enumerate(nxt) if f == nf]
            for obj in next_objs:
                elem, typ = obj.split()
                if typ == "microchip":
                    valid = valid and (not next_generators or f"{elem} generator" in next_objs)

                if not valid:
                    break

            if valid:
                q.append((tuple(nxt), nf, s+1))
