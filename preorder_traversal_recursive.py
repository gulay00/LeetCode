# 144. Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/

class Solution:
    def preorderTraversal(self, root):
        result = []

        def preorder(node):
            if node is None:
                return

            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return result
