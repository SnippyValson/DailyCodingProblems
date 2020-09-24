# Solved by OWN without hints

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(node):
    if node is None:
        return "Node(NULL)"
    left_str = serialize(node.left)
    right_str = serialize(node.right)
    return "Node({0},{1},{2})".format(node.val, left_str, right_str)


def deserialize(node_string):
    if node_string == "Node(NULL)":
        return None
    node_str = node_string[len("Node("):len(node_string)][:-1]
    comma_index = 0
    for i in range(0, len(node_str)):
        if node_str[i] == ',':
            comma_index = i
            break
    val_ = node_str[0:comma_index]
    level = 0
    prev_comma_index = comma_index
    for i in range(comma_index, len(node_str)):
        if node_str[i] == '(':
            level = level + 1
        if node_str[i] == ')':
            level = level - 1
            if level == 0:
                comma_index = i
                break
    left_ = node_str[prev_comma_index + 1:comma_index + 1]
    level = 0
    prev_comma_index = comma_index + 1
    for i in range(comma_index + 1, len(node_str)):
        if node_str[i] == '(':
            level = level + 1
        if node_str[i] == ')':
            level = level - 1
            if level == 0:
                comma_index = i
                break
    right_ = node_str[prev_comma_index + 1:comma_index + 1]
    return Node(val_, deserialize(left_), deserialize(right_))


root = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(root))
assert deserialize(serialize(root)).left.left.val == 'left.left'
