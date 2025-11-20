# 1732. Find the Highest Altitude
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.


class Solution:
    def largestAltitude(self, gain):
        alt = 0
        alt_arr=[]
        for i in gain:
            alt = i+alt
            alt_arr.append(alt)
        return max([0]+alt_arr)

"""     
Approach:   
- We initialize the current altitude `alt` to 0 and an empty list `alt_arr` to store the altitudes at each point.
- We iterate through each net gain in the `gain` array, updating the current altitude by adding the net gain to it.
- After updating the altitude, we append the new altitude to the `alt_arr` list.
- Finally, we return the maximum altitude found in `alt_arr`, including the starting altitude of
    0 by using `max([0]+alt_arr)`.
"""