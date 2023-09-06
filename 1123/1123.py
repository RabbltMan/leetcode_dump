from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchTree(self, root: Optional[TreeNode], layer=0) -> List:
        if root.left is None and root.right is None:
            return
        if root.left:
            self.tree.append((layer+1, root.left))
            self.searchTree(root.left, layer+1)

        if root.right:
            self.tree.append((layer+1, root.right))
            self.searchTree(root.right, layer+1)

    def searchFather(self, leaves: List, tree: List) -> TreeNode:
        GeneralLeftLeavesIndex = [tree.index(node) for node in leaves]
        GeneralLeftLeavesIndex = [index for index in GeneralLeftLeavesIndex if index-1 not in GeneralLeftLeavesIndex]
        if (len(GeneralLeftLeavesIndex) == 1):
            return tree[GeneralLeftLeavesIndex[0] - 1][1]
        while True:
            for i, idx in enumerate(GeneralLeftLeavesIndex):
                for node in self.tree[idx: : -1]:
                    if node[0] == self.tree[idx][0] - 1:
                        GeneralLeftLeavesIndex[i] = self.tree.index(node)
                        break
            if (len(set(GeneralLeftLeavesIndex)) == 1):
                return self.tree[GeneralLeftLeavesIndex[0]][1]
        
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.tree = [(0, root), ]
        self.searchTree(root)
        maxDepth = 0
        for node in self.tree:
            if node[0] > maxDepth:
                maxDepth = node[0]
        self.leaves = [node for node in self.tree if node[0] == maxDepth]
        
        if (len(self.leaves) == 1):
            return self.leaves[0][1]
        return self.searchFather(self.leaves, self.tree)