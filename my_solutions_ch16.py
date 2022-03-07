from collections import OrderedDict
from typing import Counter


def swap_nums(a, b):
    a = b - a
    b = b - a
    a = a + b
    return a, b


def word_frequency(book: list[str], word: str) -> int:
    freq = 0
    for w in book:
        if w.lower() == word.lower():
            freq += 1
    return freq


# To do this multiple times, then just store it in a dictionary
def word_frequency_dict(book: list[str], word: str) -> int:
    freq = {}
    for w in book:
        if w.lower() == word.lower():
            freq[word] += 1
    return freq[word]


def factorial_zeros(num):
    count = 0
    if num < 0:
        return -1

    # You want to see how divisible it is by 5 and then for mutliples of powers of 5 you are just want to add its power
    while num > 0:
        num = num // 5
        count += num

    return count


def smallest_diff(arr1, arr2):
    min_arr2 = min(arr2)
    arr1.sort()
    for num in arr1:
        if num > min_arr2:
            return num - min_arr2

    return -1


a = [1, 2, 11, 15]
b = [4, 12, 19, 23, 127, 235]

# See solution for number 8 since there is literally only one way to do it


def negate(a):
    negative = 0
    newSign = -1 if a > 0 else 1

    while a != 0:
        negative += newSign
        a += newSign

    return negative


def subtract(a, b):
    return a + negate(b)


def multiply(a, b):
    i = 0
    res = 0
    while i < abs(b):
        res += abs(a)
        i += 1

    return res if a > 0 and b > 0 else negate(res)


class Person:
    def __init__(self, birth, death) -> None:
        self.birth = birth
        self.death = death


def max_pop(people: Person) -> int:
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


def estimate(guess, solution):
    if len(guess) != len(solution):
        return None

    res = [0, 0]

    frequencies = Counter(solution)
    valid_chars = "RGBY"

    for i in range(len(guess)):
        if guess[i] == solution[i]:
            res[0] += 1
        elif guess[i] in valid_chars:
            if frequencies[guess[i]] > 0:
                res[1] += 1
                frequencies[guess[i]] -= 1

    return res


# print(estimate('RGBY','RRRR'))

# The first straightforward method for subarray would be to sort the array first
# then compare the sorted vs the unsorted and see the first point at which it is different and the last point it is different.
# This would be O(N*log(N)) since you are sorting, but we can do faster with O(N)

# Naive approach
def findSubarry(nums: list[int]) -> tuple:
    nums2 = sorted(nums)
    l, r = len(nums), 0

    for i in range(len(nums)):
        if nums[i] != nums2[i]:
            l = min(l, i)
            r = max(r, i)

    if l == len(nums):
        return (-1, -1)

    return (l, r)


# O(N) time solution
def findSub(nums: list[int]) -> tuple:
    if len(nums) < 2:
        return (-1, -1)

    prev = nums[0]
    end = 0

    # check that the array is in increasing order from left to right
    for i in range(0, len(nums)):
        if nums[i] < prev:
            end = i
        else:
            prev = nums[i]

    start = len(nums) - 1
    prev = nums[start]

    # check that the array is in descending order from right to left
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > prev:
            start = i
        else:
            prev = nums[i]

    if end == 0:
        return (-1, -1)

    return (start, end)


# This uses Kadane's Algorithm
def contiguous_sequence(nums: list[int]) -> int:
    max_sum = min(nums)
    sum_ = 0
    for num in nums:
        # First you check whether the sum plus the current would be more than the current num by itself
        sum_ = max(num, sum_ + num)
        # Then you see if the local maximum is the global maximum
        max_sum = max(max_sum, sum_)

    return max_sum


# Alternative solution
# maxsum = min(nums)
# sum_ = 0
# for num in nums:
#     sum_ += num
#     if sum_ > maxsum:
#         maxsum = sum_
#     if sum_ < 0:
#         sum_ = 0
# return maxsum

arr1 = [2, -8, 3, -2, 4, -10]

# print(contiguous_sequence(arr1))

# this extends the isomorphic problem
# This solution assumes spaces in between words
def match_pattern(str: str, pattern: str) -> bool:
    t = str.split()
    return len(set(zip(pattern, t))) == len(set(pattern)) == len(set(t)) and len(
        pattern
    ) == len(t)


# def match_pattern_no_space(pattern,string):
#   if len(pattern) == 0: return len(string) ==0

#   def build_from_pattern(pattern,main,alt):
#     first = pattern[0]
#     res = ''

#     for char in pattern:
#       if char == first:
#         res += main
#       else:
#         res+= alt

#     return res

#   main_char = pattern[0]
#   alternate_char = 'b' if main_char == 'a' else 'a'

#   count_of_main = Counter(pattern)[main_char]
#   count_of_alt = len(pattern) - count_of_main
#   first_alt = pattern.index(alternate_char)
#   max_main_size = len(string) // count_of_main

#   for num in range(max_main_size):
#     remaining_len = len(string) - num*count_of_main
#     first = string[0:num]
#     if count_of_alt == 0 or remaining_len%count_of_alt==0:
#       alt_start = first_alt*num
#       alt_size = 0 if count_of_alt == 0 else remaining_len//count_of_alt
#       second  = string[alt_start:(alt_size+alt_start)]

#       candidate = build_from_pattern(pattern,first,second)

#       if candidate == string:
#         return True

#   return False

# This can be done faster by pruning any possibilities that are not a valid word
def t9_convert(digits: str, valid_words: list[str]) -> list[str]:
    if not digits:
        return []

    lookup = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    result = [""]

    for char in digits:
        result = [prev + l for prev in result for l in lookup[char]]
    return [word for word in result if word in valid_words]


# valid_words = ["tree", "used"]

# print(t9_convert("8733",valid_words))

# Even faster with preprocessing
def word_to_num(valid_words: list[str]):
    valid_word_nums = {}
    lookup = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    for word in valid_words:
        num = "".join(
            [n for n, letters in lookup.items() for char in word if char in letters]
        )
        if not num in valid_word_nums.keys():
            valid_word_nums[num] = [word]
        else:
            valid_word_nums[num].append(word)
    return valid_word_nums


def t9_to_valid(digits, valid_words):
    valid_nums = word_to_num(valid_words)
    return [
        word for num, words in valid_nums.items() for word in words if num == digits
    ]


# valid_words = ["tree", "used"]

# print(t9_to_valid("8733",valid_words))


def sum_swap(arr1, arr2):
    if (sum(arr1) - sum(arr2)) % 2 != 0:
        return []
    target = abs(sum(arr1) - sum(arr2)) / 2
    arr1, arr2 = (arr1, arr2) if sum(arr2) > sum(arr1) else (arr2, arr1)
    for num2 in arr2:
        num1 = int(abs(num2 - target))
        if num1 in arr1:
            return [num1, num2]
    return []


a = [4, 1, 2, 1, 1, 2]
b = [3, 6, 3, 3]


# print(sum_swap(b,a))


class LRU_Cache:
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v  # set key as the newest one
        return v

    def set_(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)
        self.dic[key] = value
