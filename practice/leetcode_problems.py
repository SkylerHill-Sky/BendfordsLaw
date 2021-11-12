from typing import Optional, List

# You start traversal from root then goes to the left node,
# then again goes to the left node until you reach a leaf node.
# At that point in time, you print the value of the node or mark
# it visited and moves to right subtree. Continuing the same algorithm
# until all nodes of the binary tree are visited. The InOrder traversal
# is also known as left-node-right or left-root-right traversal or LNR traversal algorithm.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):     # represent so it shows that way, not __str__ which only works for str()
        return 'val: {}, left: {}, right: {}'.format(self.val, self.left, self.right)


# class Solution:
    # @staticmethod
    # def in_order_traversal(root) -> List[int]:
    #     tree_nodes = []
    #
    #     for i in range(0, len(root), 3):
    #         if i+1 > (len(root) - 1):
    #             tree_nodes.append(TreeNode(val=root[i]))
    #         elif i+2 > (len(root) - 1):
    #             tree_nodes.append(TreeNode(val=root[i]), left=i+1)
    #         else:
    #             tree_nodes.append(TreeNode(val=root[i], left=i+1, right=i+2))
    #         print(tree_nodes)

# need pointers not the value
#     @staticmethod
#     def in_order_traversal_b(root) -> List[int]:
#         tree_nodes = [TreeNode] * (len(root)//3)
#
#         for i in range(0, len(root), 3):
#             if i+1 > (len(root) - 1):
#                 tree_nodes[i] = TreeNode(val=root[i])
#             elif i+2 > (len(root) - 1):
#                 tree_nodes[i] = TreeNode(val=root[i], left=tree_nodes[i+1])
#             else:
#                 tree_nodes[i] = TreeNode(val=root[i], left=tree_nodes[i+1], right=tree_nodes[i+2])
#         print(tree_nodes)
#
#
#
#
# test = [1, None, 2, 3, 4]
# Solution.in_order_traversal(test)
from collections import deque

romanValues = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_recursive(total_so_far: int, numbers: deque, add_multiplier=-1) -> int:
    print(total_so_far, numbers, add_multiplier)

    if not total_so_far:
        if numbers[0] > numbers[-1]:
            return roman_recursive(numbers.popleft(), numbers, 1)  # trailing on the right side means add
        else:
            return roman_recursive(numbers.pop(), numbers, -1)     # trailing on the left side means subtract

    if len(numbers) >= 1:
        if numbers[0] > numbers[-1]:
            return roman_recursive((add_multiplier * numbers.popleft()) + total_so_far, numbers, 1)
        else:
            return roman_recursive((add_multiplier * numbers.pop()) + total_so_far, numbers, -1)

    # try to simplify this to <=
    if len(numbers) <= 1:
        plus = add_multiplier * numbers[0] if numbers else 0
        return total_so_far + plus


def roman_to_int(s: str) -> int:
    numbers = deque()
    i_count = 0
    for char in s:
        if char != 'I':
            if i_count:
                numbers.append(i_count)
                i_count = 0
            numbers.append(romanValues[char])
        else:
            i_count += 1

    if i_count:
        numbers.append(i_count)
    x = roman_recursive(0, numbers)
    print(s, numbers, x)


roman_to_int('III')
