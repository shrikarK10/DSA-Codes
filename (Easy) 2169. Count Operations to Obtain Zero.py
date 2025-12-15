# 2169. Count Operations to Obtain Zero
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two non-negative integers num1 and num2.

# In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

# For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
# Return the number of operations required to make either num1 = 0 or num2 = 0.4


class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count=0
        if(num1 * num2 ==0):
            return count
        while(True):
            if(num1==num2):
                count+=1
                return count
            else:
                if (num1>num2):
                    num1 = num1-num2
                    count+=1
                else:
                    num2 = num2-num1
                    count+=1
        return count

"""
Approach: 
- Initialize a counter variable count to keep track of the number of operations.
- Check if either num1 or num2 is already zero, if so return count (which is 0).
- Use a while loop to repeatedly perform the subtraction operation until either num1 or num2 becomes zero.
- Inside the loop, check if num1 is equal to num2. If they are equal, perform one subtraction operation (which will make one of them zero) and return the count.
- If num1 is greater than num2, subtract num2 from num1 and increment the count.
- If num2 is greater than num1, subtract num1 from num2 and increment the count.
- Finally, return the count of operations.
"""