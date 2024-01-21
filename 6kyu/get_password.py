# https://www.codewars.com/kata/58f6e7e455d7597dcc000045/train/python
import unittest
from typing import List

def get_password(grid: List[List[str]], directions: List[str]) -> str:
    """
    Generate a password by navigating a grid based on given directions.

    Args:
    grid List[List[str,..]]: The grid to navigate.
    directions List[str,..]: The direction for navigation.

    Returns:
    str: The generated password.
    """
    # Find the starting position marked by 'x'
    x_pos = next((x,y) for x, row in enumerate(grid) for y, col in enumerate(row) if col == 'x')

    password = ""
    directions_dict = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}

    for direction in directions:
        move, take = (direction[:-1], True) if direction.endswith("T") else (direction, False)
        y_change, x_change = directions_dict[move]
        new_row, new_col = x_pos[0] + y_change, x_pos[1] + x_change

        if take:
            password += grid[new_row][new_col]

        x_pos = (new_row, new_col)
    return password

class TestGetPassword(unittest.TestCase):

    def test_case_1(self):
        grid = [
            ["x", "l", "m"],
            ["o", "f", "c"],
            ["k", "i", "t"]
          ]
        directions = ["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"]

        self.assertEqual(get_password(grid,directions),"lock")

if __name__ == "__main__":
    unittest.main()