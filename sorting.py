import random

def findKthLargest(nums, k):
  if not nums: return
  pivot = random.choice(nums)
  print(pivot)
  right =  [x for x in nums if x > pivot]
  mid  =  [x for x in nums if x == pivot]
  left = [x for x in nums if x < pivot]
  
  R, M = len(right), len(mid)
  
  if k <= R:
    return findKthLargest(right, k)
  elif k > R + M:
    return findKthLargest(left, k - R - M)
  else:
    return mid[0]
    
nums = [9,12,1,4,8,2,6]
print(findKthLargest(nums,3))