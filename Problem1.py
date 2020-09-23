# Use set since look up in set is O(1)
def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k-num in seen:
            return True
        seen.add(num)
    return False


result = two_sum([10, 15, 3, 7], 17)
print(result)