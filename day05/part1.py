#!/usr/bin/env python3

import hashlib

inp = "cxdnnyjw"

pass_nums = []

index = 0

m = hashlib.md5()
m.update((inp + str(index)).encode())

hexdigest = m.hexdigest()

while len(pass_nums) != 8:
    m = hashlib.md5()
    m.update((inp + str(index)).encode())

    hexdigest = m.hexdigest()
    if hexdigest[:5] == "00000":
        pass_nums.append(hexdigest[5])

    index += 1

print("".join(pass_nums))
