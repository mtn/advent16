#!/usr/bin/env python3

import hashlib

inp = "yjdafjpo"

digests = {}
keys = []
i = 0

def search_j(ch, i):
    global digests
    for j in range(i+1, i+1001):
        if j not in digests:
            digests[j] = hashlib.md5(str.encode("{}{}".format(inp, j))).hexdigest()
        dj = digests[j]

        for jind in range(0, len(dj)-4):
            if ch == dj[jind] == dj[jind+1] == dj[jind+2] == dj[jind+3] == dj[jind+4]:
                di = digests[i]
                return True

while True:
    if i not in digests:
        digests[i]= hashlib.md5(str.encode("{}{}".format(inp, i))).hexdigest()

    di = digests[i]
    for ind in range(0, len(di)-2):
        if di[ind] == di[ind+1] == di[ind+2]:
            ch = di[ind]
            if search_j(ch, i):
                keys.append(i)
                if len(keys) == 64:
                    print(i)
                    exit()
                break
            else:
                break

    i += 1
