#!/usr/bin/env python3


num_support_ssl = 0

with open("input.txt") as f:
    # with open("small.in") as f:
    for line in f:
        in_brackets = False
        support_ssl = False

        aba_seqs = set()
        bab_seqs = set()

        for i, ch in enumerate(line.strip()[:-2]):
            if ch == "[":
                in_brackets = True
            elif ch == "]":
                in_brackets = False

            elif ch == line[i + 2] and ch != line[i + 1]:
                if not in_brackets:
                    for bab in bab_seqs:
                        if bab[1] == ch and bab[0] == line[i + 1]:
                            support_ssl = True
                            break
                    aba_seqs.add(f"{ch}{line[i+1]}")
                else:
                    for aba in aba_seqs:
                        if aba[1] == ch and aba[0] == line[i + 1]:
                            support_ssl = True
                            break
                    bab_seqs.add(f"{ch}{line[i+1]}")

        if support_ssl:
            num_support_ssl += 1

print(num_support_ssl)
