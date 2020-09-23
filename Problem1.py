def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k-num in seen:
            return True
        seen.add(num)
    return False


result = two_sum([10, 15, 3, 7], 16)
print(result)