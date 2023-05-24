#!/usr/bin/python3
"""
makeChange function determines the fewest number of coins needed
to meet a given amount
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island (grid):
    Args:
      grid: list of list of integers(list[list(int)]):
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    Return:
      int: Perimeter of the island.
    """

    rows = len(grid)  # Numbers of rows in the grid
    cols = len(grid[0])  # Numbers of columns in the grid
    perimeter = 0  # Counter perimeter

    for i in range(rows):  # Iteration in the cell's grid rows
        for j in range(cols):  # Iteration in the cell's columns

            if grid[i][j] == 1:  # If the cell represent the land
                # If the cell is in the first row or cell above is water(0)
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1

                # If the cell is first column of cell to the left is water(0)
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1

                # If cell first column or cell to the left is water (0)
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # If cell is in the last column or the cell right is water(0)
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    # Return the perimeter of the island
    return perimeter
