# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.
#
# Write a solution to remove the rows with missing values.
#
# The result format is in the following example.
#
#
#
# Example 1:
#
# Input:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 217        | None    | 19  |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# +------------+---------+-----+
# Output:
# +------------+---------+-----+
# | student_id | name    | age |
# +------------+---------+-----+
# | 32         | Piper   | 5   |
# | 779        | Georgia | 20  |
# | 849        | Willow  | 14  |
# +------------+---------+-----+
# Explanation:
# Student with id 217 has empty value in the name column, so it will be removed.
#
# Difficulty: Easy
# Time: O(n) – because the dropna function must scan all n rows in the DataFrame to identify and remove rows with missing values in the name column.
# Space: O(n) – because the dropna function creates and returns a new DataFrame with the specified rows removed. This requires additional space proportional to the size of the DataFrame, hence O(n) space complexity.
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])