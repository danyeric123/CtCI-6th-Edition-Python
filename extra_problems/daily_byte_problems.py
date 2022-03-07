"""
Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

s = "ABC#", t = "CD##AB", return true
s = "como#pur#ter", t = "computer", return true
s = "cof#dim#ng", t = "code", return false

"""


def check_keystrokes(str1, str2):
    # For edge cases where the string starts with #'s, you would need a different function to clean the data and return a string without #'s in it

    def resultant_string(str):
        res = ""
        for char in str:
            if char == "#":
                res = res[:-1]
                continue
            res += char
        return res

    return resultant_string(str1) == resultant_string(str2)


print(check_keystrokes("ABC#", "CD##AB"))
print(check_keystrokes("cof#dim#ng", "code"))
