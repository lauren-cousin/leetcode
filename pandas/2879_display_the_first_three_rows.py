# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.
#
# Difficulty: Easy
# Time: O(1) – because retrieving the first 3 rows is a constant-time operation.
# Space: O(1) – because the function only returns a small, fixed-size subset of the DataFrame.
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)