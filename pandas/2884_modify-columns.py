# DataFrame employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | salary      | int    |
# +-------------+--------+
# A company intends to give its employees a pay rise.
# Write a solution to modify the salary column by multiplying each salary by 2.
# The result format is in the following example.
#
# Example 1:
# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 19666  |
# | Piper   | 74754  |
# | Mia     | 62509  |
# | Ulysses | 54866  |
# +---------+--------+
# Output:
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Jack    | 39332  |
# | Piper   | 149508 |
# | Mia     | 125018 |
# | Ulysses | 109732 |
# +---------+--------+
# Explanation:
# Every salary has been doubled.
#
# Difficulty: Easy
# Time: O(n) – due to iterating through each salary. You must iterate over all n elements in the salary column to modify them, so the operation inherently takes O(n) time. Not possible to achieve O(1).
# Space: O(1) – as the modification is done in place without creating a new DataFrame.
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] =  employees['salary'].multiply(2)
    return employees