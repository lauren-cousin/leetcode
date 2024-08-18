# DataFrame students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
#
# Write a solution to select the name and age of the student with student_id = 101.
#
# Difficulty: Easy
# Time: O(n) – because the function must scan the DataFrame to find the matching student_id.
# Space: O(1) – because the function only returns a small, fixed-size subset of the DataFrame.

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]