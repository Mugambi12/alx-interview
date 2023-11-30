#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def generate_pascal_triangle(rows):
    """Generates Pascal's Triangle up to the given number of rows."""
    if rows <= 0:
        return []

    pascal_triangle = []

    for current_row in range(rows):
        # Initialize a new row with 1s at the ends
        new_row = [0] * (current_row + 1)
        new_row[0] = 1
        new_row[-1] = 1

        for col_index in range(1, current_row):
            # Calculate values for the inner columns
            if 0 < col_index < len(new_row):
                left_value = pascal_triangle[current_row - 1][col_index]
                upper_left_value=pascal_triangle[current_row -1][col_index -1]
                new_row[col_index] = left_value + upper_left_value

        pascal_triangle.append(new_row)

    return pascal_triangle
