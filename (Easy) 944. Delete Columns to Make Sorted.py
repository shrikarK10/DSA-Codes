# 944. Delete Columns to Make Sorted
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an array of n strings strs, all of the same length.

# The strings can be arranged such that there is one on each line, making a grid.

# For example, strs = ["abc", "bce", "cae"] can be arranged as follows:
# abc
# bce
# cae
# You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

# Return the number of columns that you will delete.



class Solution:
    def minDeletionSize(self, strs):
        count=0
        flag = False
        for i in range (0 , len(strs[0])):
            for j in range (0,len(strs)-1):
                if strs[j][i] <= strs[j+1][i]:
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag == False:
                count+=1
        return count
    
