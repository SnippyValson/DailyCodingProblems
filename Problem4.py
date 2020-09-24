# Solved with hint.
# Use array index to your advantage when ever possible.

def first_missing(lst):
    for i in range(0, len(lst)):
        if lst[i] != i:
            if 0 <= lst[i] <= len(lst)-1:
                temp = lst[lst[i]]
                lst[lst[i]] = lst[i]
                lst[i] = temp
    for i in range(0, len(lst)):
        if lst[i] != i:
            return i


print(first_missing([0, 3, 6, 1, 5]))
