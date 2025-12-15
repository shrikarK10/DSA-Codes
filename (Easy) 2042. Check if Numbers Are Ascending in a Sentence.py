# 2042. Check if Numbers Are Ascending in a Sentence
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A sentence is a list of tokens separated by a single space with no leading or trailing spaces. Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word consisting of lowercase English letters.

# For example, "a puppy has 2 eyes 4 legs" is a sentence with seven tokens: "2" and "4" are numbers and the other tokens such as "puppy" are words.
# Given a string s representing a sentence, you need to check if all the numbers in s are strictly increasing from left to right (i.e., other than the last number, each number is strictly smaller than the number on its right in s).

# Return true if so, or false otherwise.


import re
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        x = re.findall("\d+" , s)
        x_int = [int(i) for i in x]

        for i in range (0,len(x_int)-1) :
            if(x_int[i]>=x_int[i+1]):
                return False
        return True

"""
Approach:
- Instead using isdigit() method we can use regex to extract all the numbers from the string.
- We use re.findall("\d+" , s) to find all sequences of digits in the string s. This returns a list of strings representing the numbers.
- So at first I was just checking if the current list (x) is equals to the sorted version of itself to determine if the numbers are in ascending order.
- However, this approach does not account for the requirement that the numbers must be strictly increasing. For example, if the input string contains the numbers "2 2 3", the sorted version would also be "2 2 3", and the check would incorrectly return true.
- To fix this, we convert the list of number strings to a list of integers (x_int) using a list comprehension.
- We then iterate through the list of integers and compare each number with the next one to ensure that it is strictly less than the next number.
- If we find any number that is not strictly less than the next number, we return false.
- If we complete the loop without finding any such case, we return true, indicating that all numbers are strictly increasing."""