# 2678. Number of Senior Citizens
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:

# The first ten characters consist of the phone number of passengers.
# The next character denotes the gender of the person.
# The following two characters are used to indicate the age of the person.
# The last two characters determine the seat allotted to that person.
# Return the number of passengers who are strictly more than 60 years old.


from ast import List

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details :
            if(int(i[11:-2])>60):
                count+=1
        return count
    


"""
Approach:
- We will iterate through each string in the details list.
- For each string, we will extract the age by slicing the string from index 11 to index -2.
- We will convert the extracted age substring to an integer and check if it is greater than 60.
- If the age is greater than 60, we will increment our count variable.
- Finally, we will return the count of passengers who are strictly more than 60 years old.
"""
