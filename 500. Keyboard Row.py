# 500. Keyboard Row
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".



final=[]
for i in words:
  flag_row = -1
  for j in i.lower() :
    if j in "qwertyuiop"  :
      if (flag_row == -1 or flag_row==1):
        flag_row = 1
      else:
        flag_row =-1
        break
    if j in "asdfghjkl"  :
      if (flag_row == -1 or flag_row==2):
        flag_row = 2
      else:
        flag_row=-1
        break
    if j in "zxcvbnm"  :
      if (flag_row == -1 or flag_row==3):
        flag_row = 3
      else:
        flag_row =-1
        break
  if flag_row != -1:
    final.append(i)
final


"""
Approach:
- Used two nested for loops to check if a letter is in the row specified.
- But to optimize this I found out that if a single letter is in a different row than other letters then it can't be typed using letters of the alphabet on only one row of American keyboard.
- So I used a flag to check if a letter is in a different row than other letters.
- And breaked the loop instantly if it appears in a different row than other letters and initialized the flag to -1.
- So when the nested loop ends we check if flag is -1 , if its not then we append the current word in the final list.
"""