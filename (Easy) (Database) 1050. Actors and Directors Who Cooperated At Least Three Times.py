# 1050. Actors and Directors Who Cooperated At Least Three Times
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: ActorDirector

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key (column with unique values) for this table.
 

# Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

# Return the result table in any order.

# The result format is in the following example.



"""SELECT c.actor_id , c.director_id 
FROM (
        SELECT COUNT(*) as combo , actor_id , director_id
        FROM ActorDirector
        GROUP BY actor_id , director_id
) as c
WHERE c.combo >=3 """


"""
Approach:
- We need to identify pairs of actor_id and director_id that have collaborated at least three times
- We start by grouping the records in the ActorDirector table by both actor_id and director_id.
- For each group, we count the number of occurrences (collaborations) using COUNT(*).
- We then filter these groups to retain only those where the count of collaborations is three or more
- Finally, we select the actor_id and director_id from the filtered results to get the desired pairs.   
"""