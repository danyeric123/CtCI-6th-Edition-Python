# Using DFS
from collections import defaultdict


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
# Runtime: O(N log N) since it is calls get_height on the same node once per node above it
# This runs slower because of recursion twice--once in is_balanced and another time in get_height
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
  
# DFS version, O(V)
# It traverses the tree and does the calculations as it is checking balanced
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
    
    
# This runs in O(V+D) where D is the dependencies   
def determine_build_order(projects, dependencies):
    # First you create a dependency list and add whatever it is dependent upon as the value
    # If something has no dependencies, it will still be in the set but just have an empty set
    dependency_tree = {p: set() for p in projects}
    build_order = []
    unbuilt_projects = set(projects)
    for dependency, project in dependencies:
        dependency_tree[project].add(dependency)

    while unbuilt_projects:
        something_built = False
        for project in list(unbuilt_projects):
            dependencies = dependency_tree[project]
            # You get its dependencies and then check whether either there are no dependencies
            # or the dependency was already built (hence removed from unbuilt projects list)
            if not unbuilt_projects.intersection(dependencies):
                build_order.append(project)
                unbuilt_projects.remove(project)
                something_built = True
        if not something_built:
            raise NoValidBuildOrderError("No valid build order exists")

    return build_order

class NoValidBuildOrderError(Exception):
    pass

#c Creative solution to similar problem
def findOrder(self, numCourses, prerequisites):
        pre, suc = defaultdict(int), defaultdict(list)
        for a, b in prerequisites:
            pre[a] += 1
            suc[b].append(a)
        free = set(range(numCourses)) - set(pre)
        out = []
        while free:
            a = free.pop()
            out.append(a)
            for b in suc[a]:
                pre[b] -= 1
                pre[b] or free.add(b)
        return out * (len(out) == numCourses)