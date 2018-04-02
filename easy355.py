#!/usr/bin/env python3

def caesar(key, msg, out="", enc_list=[]):
    master = [i for i in "abcdefghijklmnopqrstuvwxyz"]
    enc_nums = [key + master.index(i) for i in msg]

    for i in enc_nums:
        if i > 25:
            enc_list.append(master[i-26])
        else:
            enc_list.append(master[i])

    for i in enc_list:
        out = out + i

    return out

def carrol(key, msg):


print(caesar(25, "thequickbrownfoxjumpsoverthelazydog"))
