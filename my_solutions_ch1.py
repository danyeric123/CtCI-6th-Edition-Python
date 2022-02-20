
from collections import Counter
from copy import copy
import unittest, re

def is_unique(str):
  return len(set(str)) == len(str)

# print(is_unique("hat"))
# print(is_unique("that"))
# print(is_unique("mat"))

def check_permutation(str1,str2):
  for char in str1:
    if char not in str2:
      return False
  return True

def check_permutation_pythonic(str1, str2):
  if len(str1) != len(str2):
      return False

  return Counter(str1) == Counter(str2)
  
# print(check_permutation("dog","god"))
# print(check_permutation("dogx","godz"))

# Harder Version of Check Permutation:

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Leetcode link: https://leetcode.com/problems/permutation-in-string/

def checkInclusion(s1: str, s2: str) -> bool:
  if len(s2) < len(s1):
      return False

  s1CharCount = {chr(ord('a')+i): 0 for i in range(26)}
  s2CharCount = {chr(ord('a')+i): 0 for i in range(26)}

  # Initialize sliding window
  l, r = 0, 0

  for i,char in enumerate(s1):
      s1CharCount[char] += 1
      s2CharCount[s2[i]] += 1
      r += 1
      
      
  if s1CharCount == s2CharCount:
      return True

  # Go through s2 with the sliding window and see if the charcount matches
  while r < len(s2):
      s2CharCount[s2[r]] += 1
      s2CharCount[s2[l]] -= 1
      if s1CharCount == s2CharCount:
          return True
      
      r += 1
      l += 1
      
  return False

def urlify_with_length(str,len):
  return str[:len].replace(" ","%20")


def urlify(str):
  return re.sub(r'\s\s+|\s$',"",str).replace(" ","%20")

# print(urlify("Mr John Smith     "))
# print(urlify("Mr John Smith "))
# print(urlify("Mr John Smith"))

def palindrome_permutation(str):
  chars = Counter(str.replace(" ","").lower())
  return sum(count%2 for count in chars.values()) <= 1

# print(palindrome_permutation("So patient a nurse to nurse a patient so"))
# print(palindrome_permutation("taco coa"))

# I believe this could be done with just one helper function since both replace_away and insert_away do the same thing
def one_away(str1,str2):
  if len(str1) == len(str2):
    return replace_away(str1,str2)
  if len(str1)+1 == len(str2):
    return insert_away(str1,str2)
  if len(str1)-1 == len(str2):
    return insert_away(str1,str2)
  
def replace_away(str1,str2):
  count =0
  for char in str1:
    if char not in str2:
      count += 1
      if count == 2:
        return False
  return True

# Not sure if this is right...
def insert_away(str1,str2):
  count =0
  for char in str1:
    if char not in str2:
      count += 1
      if count == 2:
        return False
  return True

# print(one_away("pale","bale"))

def str_compression(str1):
  compressed = ""
  count = 0
  
  for i in range(len(str1)):
    if str1[i] == str1[i-1]:
      count+=1
    else:
      compressed += str1[i-1]+str(count)
      count=1
  
  if count:
    compressed += str1[-1]+str(count)
  
  return min(str1, "".join(compressed), key=len)


# print(str_compress("aabcccccaaa"))
# print(str_compress("abcdef"))
# print(str_compress("aaa"))


def rotate_matrix_pythonic(matrix):
  matrix[:] = zip(*matrix[::-1])

def rotate_matrix(matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i < j:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  for row in matrix:
      row.reverse()
      
  return matrix

# print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

def zero_matrix(matrix):
  new_matrix = [x[:] for x in matrix]
  
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if matrix[row][col] == 0:
        new_matrix[row] = [0]*len(matrix[0])
        for i in range(len(matrix)):
          new_matrix[i][col] = 0
          
  return new_matrix

def zero_matrix_inplace(matrix):
  if not matrix:
            return []

  m = len(matrix)
  n = len(matrix[0])

  zeroes_row = [False] * m
  zeroes_col = [False] * n
  for row in range(m):
      for col in range(n):
          if matrix[row][col] == 0:
              zeroes_row[row] = True
              zeroes_col[col] = True

  for row in range(m):
      for col in range(n):
          if zeroes_row[row] or zeroes_col[col]:
              matrix[row][col] = 0

# print(zero_matrix([[1,1,1],[1,0,1],[1,1,1]]))


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False
  
  