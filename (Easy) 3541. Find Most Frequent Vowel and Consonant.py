# 3541. Find Most Frequent Vowel and Consonant
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s consisting of lowercase English letters ('a' to 'z').

# Your task is to:

# Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
# Find the consonant (all other letters excluding vowels) with the maximum frequency.
# Return the sum of the two frequencies.

# Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

# The frequency of a letter x is the number of times it occurs in the string.

class Solution:
    def maxFreqSum(self, s: str) -> int:
        s_set = set(s)
        counts_vowels=[0]
        counts_cons =[0]
        for i in s_set:
            if (i=="a" or i =="i" or i=="e" or i=="o" or i=="u"):
                counts_cons.append(s.count(i))
            else:
                counts_vowels.append(s.count(i))

        return max(counts_vowels) + max(counts_cons)
    


"""
Approach:
- I started by converting the string into a set to get unique characters.
- I initialized two lists, counts_vowels and counts_cons, to keep track of the frequencies of vowels and consonants, respectively.
- I iterated through each unique character in the set.
- For each character, I checked if it was a vowel (a, e, i, o, u). If it was, I counted its occurrences in the original string and appended the count to counts_vowels. If it was a consonant, I did the same for counts_cons.
- After processing all characters, I found the maximum frequency in both counts_vowels and counts_cons.
- Finally, I returned the sum of the maximum frequencies of vowels and consonants.
"""