def getSum(a: int, b: int) -> int:
  ## APPROACH : BITWISE OPERATIONS ##
  ## LOGIC ##
  #   1. For any two numbers, if their binary representations are completely opposite, then XOR operation will directly produce sum of numbers ( in this case carry is 0 )
  #   2. what if the numbers binary representation is not completely opposite, XOR will only have part of the sum and remaining will be carry, which can be produced by and operation followed by left shift operation.
  #   3. For Example 18, 13 => 10010, 01101 => XOR => 11101 => 31 (ans found), and operation => carry => 0
  #   4. For Example 7, 5
  #   1 1 1                   1 1 1
  #   1 0 1                   1 0 1
  #   -----                   -----
  #   0 1 0   => XOR => 2     1 0 1  => carry => after left shift => 1 0 1 0
  #   2                                                              10
  # now we have to find sum of 2, 10 i.e a is replace with XOR result and b is replaced wth carry result
  # similarly repeating this process till carry is 0
  #   steps will be 7|5 => 2|10 => 8|4  => 12|0
  
## TIME COMPLEXITY : O(1) ##
## SPACE COMPLEXITY : O(1) ##
  
  # 32 bit mask in hexadecimal
  mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
  while(b & mask > 0):
      carry = (a & b) << 1
      a = a ^ b
      b = carry
  return (a & mask) if b > 0 else a

from random import randrange

def shuffle(nums):
  ans = nums[:]                     # copy list
  for i in range(len(ans)-1, 0, -1):     # start from end
      j = randrange(0, i+1)    # generate random index 
      ans[i], ans[j] = ans[j], ans[i]    # swap
  return ans

def count_twos_in_range_at_digit(num: int, digit : int)->int:
  power = pow(10,digit)
  next_power = power*10
  right = num % power
  
  round_down = num - (num % next_power)
  round_up = round_down + next_power
  
  digit_ =  (num/power)%10
  
  if digit_ < 2:
    return round_down / 10
  elif digit_ == 2:
    return round_down / 10 + right + 1
  else:
    return round_up / 10
  
def count_twos_in_range(num : int) -> int:
  count = 0
  len_num = len(str(num))
  
  for digit in range(0,len_num):
    count += count_twos_in_range_at_digit(num, digit)
    
  return count

# print(count_twos_in_range(22))

# simple answer
def num_twos_range(num):
  
  def num_twos(num):
    count = 0
    while num:
      if num%10 == 2:
        count+=1
      num = num// 10
    return count
  
  count = 0
  for i in range(2,num+1):
    count+= num_twos(i)
  
  return count

# print(num_twos_range(22))

def majority_elem(nums):
  
  def get_candidate(nums):
    majority = 0
    count = 0
    for n in nums:
      if count == 0:
        majority = n
      
      if n == majority:
        count += 1
      else:
        count -= 1
    return majority
  
  cand = get_candidate(nums)
  
  def validate(nums, majority):
    count = 0
    for n in nums:
      if n == majority:
        count += 1
        
    return count > len(nums) / 2
  
  return cand if validate(nums,cand) else -1

# test = [3,1,1,1,7,3,7,7,7]

# print(majority_elem(test))

class Location:
  def __init__(self, first: int, second : int) -> None:
      self.first = first
      self.second = second
      
  def set_location(self,first,second):
    self.first = first
    self.second = second
  
  def distance(self):
    return abs(self.first-self.second)
  
  def update(self,loc):
    if(loc.distance() < self.distance()):
      self.set_location(loc.first,loc.second)
      
def find_closest(words,word1,word2):
  best = current = Location(-1,-1)
  
  for i,word in enumerate(words):
    if word == word1:
      current.first = i
      best.update(current)
    elif word == word2:
        current.second = i
        best.update(current)
        
  return best

def smallest_k(nums : list[int], k: int)->list[int]:
  return nums.sort()[:k+1]
    