# 1507. Reformat Date
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a date string in the form Day Month Year, where:

# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:

# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.


class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        months = {
                'Jan': '1', 'Feb': '2', 'Mar': '3', 'Apr': '4',
                'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8',
                'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'
                 }

        year = date[-4:]
        month_str = date[-8:-5]
        month = months[month_str]
        day = date[:-11]

        if(len(day)==1):
            day="0"+day
        if(len(month)==1):
            month="0"+month
        return year+"-"+month+"-"+day 
    

"""
Approach:
- First we create a dictionary to map the month to their respective numerical values.
- Then we extract the year, month and day from the input date string using basic string slicing.
- We check if the day or month is a single digit, if so we prepend a '0' to make it two digits.
- Finally we concatenate the year, month and day in the required format and return the result.
"""