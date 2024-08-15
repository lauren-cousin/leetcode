# Description: Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.
# The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.
#
# Difficulty: Easy
# Tags: Math, String, Simulation
# Time: O(n) – because the function iterates through the student_data to create the DataFrame.
# Space: O(n) – because the DataFrame occupies space proportional to the size of the input list.
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])