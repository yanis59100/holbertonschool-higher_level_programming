#!/usr/bin/python3
for letter in range(97, 123):
    if letter != ord('q') and letter != ord('e'):
        print("{}".format(chr(letter)), end="")
