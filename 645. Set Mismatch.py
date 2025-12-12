# 645. Set Mismatch
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.




class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a,b=0,0
        nums.sort()
        n= len(nums)
        re=[]
        for i in range (1,n):
            if nums[i] == nums[i-1]:
                a= nums[i]
                print(a)
                nums.remove(a)
                break
        act_sum = (n*(n+1)) // 2
        b = act_sum - sum(nums)

        re.append(a)
        re.append(b)
        return re


"""
Approach:
- I used a simple approach to find the number that occurs twice and the number that is missing.
- I initialized two variables a and b to store the number that occurs twice and the number that is missing.
- Also Sorted the array for better comparisions.
- I used a for loop to iterate through the nums array.
- I checked if the current element is equal to the previous element.
- If it is equal to the previous element, I assigned it to the a variable which we append later in the list.
- Then I calculated the actual sum of the array and subtracted the sum of the array from it to get the missing number.
- Finally, I returned the list of the number that occurs twice and the number that is missing.
"""

