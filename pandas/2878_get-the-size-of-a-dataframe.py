# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+
# Write a solution to calculate and display the number of rows and columns of players.
# Return the result as an array:
# [number of rows, number of columns]
#
# Difficulty: Easy
# Time: O(1) – because accessing the shape attribute is a constant-time operation.
# Space: O(1) – because the function only stores a small, fixed-size list.
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]