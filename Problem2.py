def pre_products(lst):
    pre = [0] * len(lst)
    pre[0] = 1
    for i in range(1, len(lst)):
        pre[i] = pre[i-1] * lst[i-1]
    return pre


def post_products(lst):
    post = pre_products([num for num in reversed(lst)])
    post = [num for num in reversed(post)]
    return post


def exclusive_products(lst):
    pre = pre_products(lst)
    post = post_products(lst)
    return [pr * po for pr, po in zip(pre, post)]


pro = exclusive_products([1, 2, 3, 4, 5])
print(pro)

pro = exclusive_products([3, 2, 1])
print(pro)

