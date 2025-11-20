# 1437. Check If All 1's Are at Least Length K Places Away
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.


from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums: return True

        j=-1
        i=-1
        ind=-1
        while(True):
            ind+=1
            if (nums[ind]==1):
                if i==-1: i=ind
                elif j ==-1 : j = ind
                if j > i :
                    if j - i - 1< k : 
                        return False
                    i=j
                    j=-1
            if(ind==len(nums)-1) : break

        return True
    

"""
Approach:
- I wanted to use two pointers to track the positions of the 1's in the array.
- I initialized two pointers, i and j, to -1 to indicate that we haven't found any 1's yet.
- I also initialized an index variable ind to -1 to keep track of our current position in the array.
- first I checked if there are any 1's in the array. If not, I returned True immediately.
- I then entered a while loop that continues until we reach the end of the array.
- Inside the loop, I incremented the index variable ind to move to the next position in the array.
- If the current element is 1, I checked if i is -1 (indicating this is the first 1 we've found) and set i to the current index.
- If i is not -1 and j is -1, I set j to the current index (indicating this is the second 1 we've found).
- If j is greater than i, I checked the distance between the two 1's. If the distance is less than k, I returned False.
- I then updated i to j and reset j to -1 to continue checking the rest of the array.
- If we reach the end of the array without finding any pairs of 1's that are too close together, I returned True.
"""