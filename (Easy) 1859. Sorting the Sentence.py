# 1859. Sorting the Sentence
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.


x=s.split()
for i in range (0,len(x)):
  x[i] = x[i][::-1]
x.sort()
for i in range (0,len(x)):
  x[i] = x[i][1:]
  x[i] = x[i][::-1]
x


"""
Approach:
- I used a simple approach to sort the sentence.
- I first split the sentence into words and stored it in a list x.
- I then used a for loop to reverse each word in x.
- Next, I sorted the list x.
- Finally, I used another for remove the first character and reverse each word in x.
- I returned the sorted list x as the result.
"""
