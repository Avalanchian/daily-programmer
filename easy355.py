#!/usr/bin/env python3

alpha_nums = [i for i in "abcdefghijklmnopqrstuvwxyz"]

def caesar(key, msg):
    """Encrypts using a Ceasar cypher with specified key"""

    string_out, enc_list = ["", []]
    enc_nums = [key + alpha_nums.index(i) for i in msg]

    for i in enc_nums:
        if i > 25:
            enc_list.append(alpha_nums[i-26]) # Prevents index errors.
        else:
            enc_list.append(alpha_nums[i])

    # Convert enc_list to string.
    for i in enc_list:
        string_out = string_out + i

    return string_out

def carroll(key, msg):
    """Encrypts using a Carroll cypher with specified key"""

    key_list, key_map, carroll_list, string_out = [[], [], [], ""]
    # Maps key to each character in msg and converts to Ceasar key.
    while len(key_map) < len(msg):
        for i in key:
            if len(key_map) == len(msg):
                break
            else:
                key_map.append(i)
    key_list = [alpha_nums.index(i) for i in key_map]

    # Performs encryption.
    for i in range(len(msg)):
        carroll_list.append(caesar(key_list[i], msg[i]))

    # Convert carroll_list to string.
    for i in carroll_list:
        string_out = string_out + i

    return string_out

# Encrypt challenge inputs.
print(carroll("bond", "theredfoxtrotsquietlyatmidnight"))
print(carroll("train", "murderontheorientexpress"))
print(carroll("garden", "themolessnuckintothegardenlastnight"))

print(True)
