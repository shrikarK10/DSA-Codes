# 1935. Maximum Number of Words You Can Type
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

from typing import List
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_arr = text.split(" ")
        broken_arr = list(brokenLetters)
        count=0
        for i in text_arr :
            flag =-1
            for k in broken_arr:
                 if k in i :
                    flag = 0
                    break
            if flag != 0 :
                count+=1
        return count    



"""
Approach:
- We start by splitting the input string text into a list of words using the split(" ") method. This gives us an array of individual words to check.
- We convert the string of broken letters into a list of characters for easier checking.
- We initialize a counter count to keep track of the number of words that can be fully typed.
- We iterate through each word in the text_arr list.
- For each word, we initialize a flag variable to -1. This flag will help us determine if the word contains any broken letters.
- We then iterate through each broken letter in the broken_arr list.
- If we find that a broken letter is present in the current word, we set the flag to 0 and break out of the inner loop, indicating that this word cannot be fully typed.
- After checking all broken letters for the current word, we check the value of the flag. If it is still -1, it means the word does not contain any broken letters, and we increment the count by 1.
- Finally, we return the count, which represents the total number of words that can be fully typed using the keyboard.
"""