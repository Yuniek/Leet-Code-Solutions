"2265. Count Nodes Equal to Average of Subtree"
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def list_to_tree(values) -> TreeNode|None:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])

    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Left child
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1

    return root

        
class Solution:
    def averageOfSubtree(self, root:TreeNode|None) -> int:
        count = 0
        def depthFirstSearch(node:TreeNode|None) -> tuple[int,int]:
            nonlocal count
            if node == None:
                return (0,0)

            left_sum, left_count = depthFirstSearch(node.left)
            right_sum, right_count = depthFirstSearch(node.right)

            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            if total_sum//total_count == node.val:
                count += 1
            return (total_sum, total_count)
        depthFirstSearch(root)
        return count



print(Solution().averageOfSubtree(list_to_tree([4,8,5,0,1,None,6])))