# 506. Relative Ranks
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

# The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

# The 1st place athlete's rank is "Gold Medal".
# The 2nd place athlete's rank is "Silver Medal".
# The 3rd place athlete's rank is "Bronze Medal".
# For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.



class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s_score = sorted(score,reverse=True)
        maps=[]
        if len(s_score)==1: return ["Gold Medal"]
        
        for i in range (0,len(s_score)):
            if i==0:
                maps.append(["Gold Medal",s_score[i]])
            elif i==1:
                maps.append(["Silver Medal",s_score[i]])
            elif i==2:
                maps.append(["Bronze Medal",s_score[i]])
            else:
                maps.append([str(i+1),s_score[i]])
        re = [0 for i in range(0,len(score))]
        for i in maps:
            re[score.index(i[1])] = i[0]
        return re   



"""
Approach:
- I sorted the scores in descending order and stored it in a new array s_score.
- I then used a for loop to iterate through the sorted scores and stored the rank and score in a dictionary maps.
- If the length of s_score is 1, I returned ["Gold Medal"] as the result.
- For each score in s_score, I checked if it is the highest, second highest, or third highest score and stored the rank and score in maps.
- If the score is not the highest, second highest, or third highest score, I stored the rank as the position of the score in s_score.
- I then used a for loop to iterate through the scores and stored the rank in the result array re.
- Finally, I returned the result array re as the result.
"""
