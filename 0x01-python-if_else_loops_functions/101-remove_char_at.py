#!/usr/bin/python3
def remove_char_at(str, ch):
    if ch < 0:
        return (str)
    return (str[:ch] + str[ch+1:])
