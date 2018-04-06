#!/usr/bin/env python3

from sys import exit, argv


def hdist(str1, str2, dist=0):
    """Finds the Hamming distance between str1 and str2"""

    if len(str1) != len(str2):
        print("String lengths not equal.")
        exit()

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            dist += 1
        else:
            continue
    return dist


def find_cent(strs_in, distances=[]):
    """for i in range(len(strs_in)):
        for j in range(len(strs_in)):
            distances[i].append(hdist(strs_in[i], strs_in[j]))"""
    distances = [[hdist(i, j) for j in strs_in] for i in strs_in]
    kvalues = [sum(i) for i in distances]
    print(distances)
    print(kvalues)
    return strs[kvalues.index(min(kvalues))]


strs_obj = open("/home/matthew/rdp/input2.txt")
strsline = strs_obj.read()
strs_obj.close()
print(strsline)
strs = strsline.splitlines()
print(strs)
strs.remove(strs[0])
print(strs)

print(find_cent(strs))

