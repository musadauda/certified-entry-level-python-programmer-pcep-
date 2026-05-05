# using dict, keep count of how many times a character occur in a string

def countchars(s):
    counts = {}
    for char in s:
        counts.setdefault(char, 0)
        counts[char] += 1

    return counts

print(countchars("musa dauda"))


## Alternatively


def countcharsAdvanced (s):
    counts = {}
    for char in s:
        counts.setdefault(char, 0)
        update = {char: counts.get(char, 0) + 1}
        print(update)
        counts = counts | update

    return counts

print(countchars("musa dauda"))
print(countcharsAdvanced("musa dauda"))

