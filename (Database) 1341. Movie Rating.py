# 1341. Movie Rating
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Movies

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | title         | varchar |
# +---------------+---------+
# movie_id is the primary key (column with unique values) for this table.
# title is the name of the movie.
# Each movie has a unique title.
# Table: Users

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | user_id       | int     |
# | name          | varchar |
# +---------------+---------+
# user_id is the primary key (column with unique values) for this table.
# The column 'name' has unique values.
# Table: MovieRating

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | movie_id      | int     |
# | user_id       | int     |
# | rating        | int     |
# | created_at    | date    |
# +---------------+---------+
# (movie_id, user_id) is the primary key (column with unique values) for this table.
# This table contains the rating of a movie by a user in their review.
# created_at is the user's review date. 
 

# Write a solution to:

# Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
# Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.
# The result format is in the following example.

 

"""# Write your MySQL query statement below
    SELECT a.name as results
    FROM
        (
            SELECT name , COUNT(*) as c
            FROM
            Users u JOIN MovieRating m 
            ON (u.user_id=m.user_id)
            GROUP BY m.user_id
            ORDER BY c DESC, u.name ASC
            LIMIT 1
        ) as a

    UNION ALL

    SELECT b.title
    FROM
        (
            SELECT AVG(mr.rating) as r, m.title as title
            FROM Movies m JOIN MovieRating mr
            ON (m.movie_id=mr.movie_id)
            WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01' 
            GROUP BY mr.movie_id
            ORDER BY r DESC , m.title ASC
            LIMIT 1
        ) as b"""

"""
Approach:
- So i was thinking of how do to get both the results in one query.
- So i thought of using UNION ALL to combine the results of two separate queries which will be easier than writing a complex query with multiple subqueries.
- For the first part, I joined the Users and MovieRating tables on user_id, grouped by user_id to count the number of ratings per user, ordered by count descending and name ascending to handle ties, and limited the result to 1.
- For the second part, I joined the Movies and MovieRating tables on movie_id, filtered the ratings to only include those from February 2020, grouped by movie_id to calculate the average rating per movie, ordered by average rating descending and title ascending to handle ties, and limited the result to 1.  
- Finally, I combined both queries using UNION ALL to get the desired result.
"""