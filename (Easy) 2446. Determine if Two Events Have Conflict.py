# 2446. Determine if Two Events Have Conflict
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

# event1 = [startTime1, endTime1] and
# event2 = [startTime2, endTime2].
# Event times are valid 24 hours format in the form of HH:MM.

# A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

# Return true if there is a conflict between two events. Otherwise, return false.


from datetime import datetime
class Solution(object):
    def haveConflict(self, event1, event2):
        """
        :type event1: List[str]
        :type event2: List[str]
        :rtype: bool
        """
        
        e1_time1 = datetime.strptime(event1[0], "%H:%M")
        e1_time2 = datetime.strptime(event1[1], "%H:%M")
        e2_time1 = datetime.strptime(event2[0], "%H:%M")
        e2_time2 = datetime.strptime(event2[1], "%H:%M")

        e1_time = e1_time2 - e1_time1
        e2_time = e2_time2 - e2_time1

        if ((e2_time1 - e1_time1).total_seconds()/60 > -1):
            return (e2_time1 - e1_time1).total_seconds() <= e1_time.total_seconds()
        else:
            return (e1_time1 - e2_time1).total_seconds() <= e2_time.total_seconds()
        

"""
Approach:
- We first convert the string to datetime
- Then we calculate the duration of both events by subtracting start time from end time.
- And after thay I was just going to return true or false based on if the start time of first event lies within the duration of other second event.
- But then i figured out that it is not given anywhere that event1 will always start before event2.
- So to handle that case I checked if event2 starts after event1 or not by subtracting their start times.
- If resulting value is greater than -1 means that event2 starts after event1 
- So based on i checked if the difference of their start times is less than or equal to the duration of event1.
- If yes means there is a conflict and we return true else false.
- If event2 starts before event1 we do the same process but with event1's start time and event2's duration.
"""