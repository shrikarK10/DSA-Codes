# 3637. Trionic Array I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums of length n.

# An array is trionic if there exist indices 0 < p < q < n − 1 such that:

# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.



class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        out = False
        point = "0"
        for i in range (0,len(nums)-1):
            if nums[i] < nums[i+1]:
                if point == "0" or point =="1":
                    point = "1"
                    continue
                else:
                    out = True
            elif nums[i] > nums [i+1] and (point =="1" or point =="2"):
                point = "2"
                if out == True : return False
            else : return False
        return out


"""
Approach:
- The question was little bit confusing to me.
- But after carefull analysis I got an idea
- I used a for loop to iterate over the list.
- First checked if the current element is less than the next element.
- If it is less than next element I assigned this point "0" to "1" to show that the pattern is started (i.e. increasing->decreasing->increasing)
- Then I checked for the next element if it is greater than the next element.
- If we found such a element then we assign the point from "1" to "2" to show that the pattern is now in decreasing phase.
- Then if we found a element which is less than the next element and point is "2" then we can know that the pattern is completed.
- This was the initial approach but it has its flaws.
- Later I understood that if normal numbers without being in the patter can be in decreasing phase and we were initializing the point to "2" , directly without starting the pattern.
- So to avoid that I used point such a that if and only if the point is "1" or "2" only then we can assume it is going in decreasing phase.
- And after that I also figured out that the end of the pattern should be the end of the array so to implement that I assigned the out variable to false if it is not end of the array and the pattern switch from increasing to decreasing.
- And finally I returned the out variable.
"""