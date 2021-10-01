# Using DFS
def is_route(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            print(visited)
            if node == end or is_route(graph, node, end, visited):
                return True
    return False

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

# You recursively go through each subtree (kinda like DFS) and get the depth
# of each subtree, returning the max of each subtree. You then check the difference
# between left and right and make sure it is less than 2. The other two calls to isBalancced
# is to make sure that each subtree also returns True, now just the max height of each side
# Runtime: O(E), but runs slower because of recursion twice--once in is_balanced and another time in get_height
def is_balanced(root):
        if not root:
            return True

        return abs(get_height(root.left) - get_height(root.right)) < 2 and is_balanced(root.left) and is_balanced(root.right)

def get_height(root):
    if not root:
        return 0

    return 1 + max(get_height(root.left), get_height(root.right))

# This is faster since it does everything in one method and pass
# 
def is_balanced_short(root):
    def helper(root):
        if not root:
            return (True, 0)
        (balanced_l, l_depth), (balanced_r, r_depth) = helper(root.left), helper(root.right)
        return (balanced_l and balanced_r and abs(l_depth - r_depth) <= 1, 1 + max(l_depth, r_depth))
    res, _ = helper(root)
    return res
  
# DFS version, O(V+E)
def is_balanced_dfs(root) -> bool:
        res = True
        def dfs(root):
          global res
          if not root:
              return 0
          left = dfs(root.left) + 1
          right = dfs(root.right) + 1
          
          if abs(right - left) > 1:
              res = False
          
          return max(left, right)
        dfs(root)
        return res
      
# In order traversal
def is_valid_BST(self, root):
    output = []
    self.inOrder(root, output)
    
    for i in range(1, len(output)):
        if output[i-1] >= output[i]:
            return False

    return True

def inOrder(self, root, output):
    if root is None:
        return
    
    self.inOrder(root.left, output)
    output.append(root.val)
    self.inOrder(root.right, output)
    
# Pre-Order traversal, converting tree to string
def isSubtree(root, subRoot) -> bool:
        def convert(p):
            return "^" + str(p.val) + "#" + convert(p.left) + convert(p.right) if p else "$"
        
        return convert(subRoot) in convert(root)