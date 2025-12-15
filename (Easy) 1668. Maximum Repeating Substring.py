# 1668. Maximum Repeating Substring
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

# Given strings sequence and word, return the maximum k-repeating value of word in sequence.

class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        rep_count=[]
        rep_count_value =0
        i=0
        x=len(word)
        while(i<=len(sequence)):
            if(sequence[i:i+x]==word):
                rep_count_value +=1
                i+=x
            else:
                i+=1
                if(rep_count_value>0):
                    rep_count.append(rep_count_value)
                    rep_count_value=0
                    i-=x-1

        if(len(rep_count)==0):
            return 0
        else:
            return max(rep_count)
        
"""
Approach:
- So we declare a empty list for keeping track of the repeating word in the particular substring so at the end the list will contain all the repeating counts of the word in the sequence. 
- and a variable rep_count_value to keep track of the repeating count current substring.
- For kind of two pointer approach we declare i and x where x is the length of the word and i is the iterator for traversing the sequence.
- Now in while loop we will check for each substring from i to i+x if it is equal to the word or not.
- If it is equal we increment the rep_count_value by 1 and move i by x
- If it is not equal we move i by 1 and check if rep_count_value is greater than 0 which means we have found some repeating words in the previous substring so we append that count to the rep_count list and reset rep_count_value to 0 for next substring count.
- This was the solution until i found out that there can be overlapping substrings as well.
- So to handle that case we decrement i by x-1 so that we can check again from the next index of the previous substring's starting index.
- Finally if the rep_count list is empty that means there was no repeating word in the sequence so we return 0 else we return the maximum value from the rep_count list.
"""