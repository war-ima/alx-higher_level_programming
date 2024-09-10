#!/usr/bin/python3

for small_letter in range(97, 123):
    if chr(small_letter) != 'q' and chr(small_letter) != 'e':
        print("{}".format(chr(small_letter)), end="")
