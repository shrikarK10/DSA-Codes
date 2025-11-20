# 290. Word Pattern
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
 

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        patterns = list(pattern)
        if(len(words)!=len(patterns)):
            return False
        
        mapping = {}

        for i in range (0,len(words)):
            if patterns[i] not in mapping and words[i] not in mapping.values(): 
                mapping[patterns[i]] = words[i]
            elif (patterns[i] , words[i]) in mapping.items():
                continue
            else:
                if (patterns[i] , words[i]) not in mapping.items() :
                    return False
        return True
    

"""
Approach:
- When it came to mapping I instantly thought about using a dictionary for mapping.
- Initially I wanted to use hastmap but later i found out that dictionary in python is the hashmaop itself.
- I started by splitting the string s into words using the split() method and converting the pattern into a list of characters.
- I checked if the lengths of the words list and the patterns list are equal. If not, I returned False immediately.
- I initialized an empty dictionary called mapping to store the mappings between pattern characters and words.
- Then I figured out that we can check for key directly using "in" operator in python.
- Also for checking value existence in dictionary I used mapping.values() method.
- And for checking both key and value pair I used mapping.items() method.
- I iterated through the indices of the words and patterns lists simultaneously.
- For each index I checked if the current pattern and word already exists in the mapping dictionary.
- If both the pattern character and the word are not in the mapping, I added them as a new key-value pair.
- Then to check if whole key-value pair exists or just one of them exists , I used mapping.items() method to check if the current pair already exists in the mapping.
- If the pair does not exist, then we can say that one of them is already mapped to some other value, so I returned False.
- If we finish iterating through all the words and patterns without any conflicts, I returned True
"""