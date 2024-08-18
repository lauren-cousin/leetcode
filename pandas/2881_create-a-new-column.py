# DataFrame employees
# +-------------+--------+
# | Column Name | Type.  |
# +-------------+--------+
# | name        | object |
# | salary      | int.   |
# +-------------+--------+
# A company plans to provide its employees with a bonus.
#
# Write a solution to create a new column name bonus that contains the doubled values of the salary column.
#
# Difficulty: Easy
# Time: O(n) – because the function must iterate over all rows to compute the bonus for each employee.
# Space: O(1) – because the new column is added in place, so it does not require additional space proportional to the input size.

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees