# 3069. Distribute Elements Into Two Arrays I
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 1-indexed array of distinct integers nums of length n.

# You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:

# If the last element of arr1 is greater than the last element of arr2, append nums[i] to arr1. Otherwise, append nums[i] to arr2.
# The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].

# Return the array result.


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1,arr2=[nums[0]],[nums[1]]
        for i in nums[2:]:
            if arr1[-1] > arr2[-1] :
                arr1.append(i)
            else:
                arr2.append(i)
        arr1.extend(arr2)
        return arr1
        


"""
-First initalized two array arr1 and arr2 with first two elements of nums.
-Then used a for loop to iterate through the remaining elements of nums.
-For each element, I compared the last element of arr1 with the last element of arr2.
-If the last element of arr1 is greater than the last element of arr2, I appended the current element to arr1.
-Otherwise, I appended the current element to arr2.
-Finally, I extended arr2 to arr1 and returned arr1 as the result.
""" 