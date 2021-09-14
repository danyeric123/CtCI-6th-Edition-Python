def swap_nums(a,b):
  a = b - a
  b = b - a
  a = a + b 
  return a,b

def word_frequency(book : list[str], word : str) -> int:
  freq = 0
  for w in book:
    if w.lower() == word.lower():
      freq += 1
  return freq

# To do this multiple times, then just store it in a dictionary

def factorial_zeros(num):
  count = 0
  if num < 0:
    return -1
  
  # You want to see how divisible it is by 5 and then for mutliples of powers of 5 you are just want to add its power
  while num > 0:
    num = num // 5
    count += num
    
  return count

def smallest_diff(arr1,arr2):
  min_arr2 = min(arr2)
  arr1.sort()
  for num in arr1:
    if num > min_arr2:
      return num-min_arr2
    
  return -1

a = [1,2,11,15]
b = [4,12,19,23,127,235]

# See solution for number 8 since there is literally only one way to do it

def negate(a):
  negative = 0
  newSign = -1 if a>0 else 1
  
  while(a!=0):
    negative+=newSign
    a+=newSign

  return negative

def subtract(a,b):
  return a+negate(b)

def multiply(a,b):
  i = 0
  res=0
  while(i<abs(b)):
    res+=abs(a)
    i+=1
  
  return res if a>0 and b>0 else negate(res)

class Person:
  def __init__(self, birth,death) -> None:
      self.birth = birth
      self.death = death

def max_pop(people : Person) -> int:
  dates = []
  for person in people:
      dates.append((person.birth, 1))
      dates.append((person.death, -1))
      
  dates.sort()

  population = max_population = max_year = 0
  for year, change in dates:
      population += change
      if population > max_population:
          max_population = population
          max_year = year
  
  return max_year