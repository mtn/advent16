#!/usr/bin/env python3

import hashlib

inp = "cxdnnyjw"

pass_vals = [None] * 8
charsfound = 0

index = 0

m = hashlib.md5()
m.update((inp + str(index)).encode())

hexdigest = m.hexdigest()

while charsfound != 8:
    m = hashlib.md5()
    m.update((inp + str(index)).encode())

    hexdigest = m.hexdigest()
    if hexdigest[:5] == "00000":
        try:
            ind = int(hexdigest[5])
            if ind >= 8 or pass_vals[ind] is not None:
                index += 1
                continue
            value = hexdigest[6]
        except:
            index += 1
            continue
        pass_vals[ind] = value
        charsfound += 1

    index += 1

print("".join(pass_vals))
