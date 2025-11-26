# 1704. Determine if String Halves Are Alike
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first =s[:-len(s)//2]
        second=s[len(s)//2:]
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        count_f=0
        count_s=0
        for i in first :
            if i in vow: count_f+=1
        
        for i in second:
            if i in vow: count_s+=1
        
        return count_f==count_s
    


"""
Approach:
- We start by splitting the input string s into two halves: first and second. The first half contains the characters from the beginning of the string up to the midpoint, and the second half contains the characters from the midpoint to the end of the string.
- We define a list vow that contains all the vowels (both lowercase and uppercase) for easy checking.
- We initialize two counters, count_f and count_s, to keep track of the number of vowels in the first and second halves, respectively.
- We iterate through each character in the first half of the string. If the character is found in the vow list, we increment the count_f counter.
- We repeat the same process for the second half of the string, incrementing the count_s counter for each vowel found.
- Finally, we compare the two counters count_f and count_s. If they are equal, it means both halves have the same number of vowels, and we return true. Otherwise, we return false.
"""
