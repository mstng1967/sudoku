DIGITS = set(range(1, 10))

def print_sudoku(sudoku, name='SUDOKU'):
    """Prints a Sudoku nicely"""

    print "### {} ###".format(name)
    for row in sudoku:
        print row

def is_correct(sudoku):
    """
    Checks whether or not a Sudoku is correct (every row, column and "box" has
    all numbers from 1 through 9).

    It takes a two-dimensional array as an input with all cells being an integer
    from 1 to 9 or None in case the cell is empty (in which case the Sudoku
    cannot be correct because it's incomplete).
    """

    # Check for repeated numbers on each row
    for row in sudoku:
        if DIGITS - set(row):
            return False

    # Check for repeated numbers on each column
    for column_index in range(9):
        if DIGITS - set([row[column_index] for row in sudoku]):
            return False

    # Check for repeated numbers on each box
    for box_number in range(9):
        seen_in_box = set([])
        box_row_base = (box_number / 3) * 3
        box_col_base = (box_number % 3) * 3
        for box_index in range(9):
            seen_in_box.add(sudoku[box_row_base + box_index / 3][box_col_base + box_index % 3])
        if DIGITS - seen_in_box:
            return False

    # If none of the previous checks failed, the Sudoku is correct
    return True

def solve(sudoku):
    """
    Solves a Sudoku, which means it fills in any empty cells with digits so that
    all rows, columns and boxes have all numbers 1 through 9.

    It takes a two-dimensional array as an input with all cells being an integer
    from 1 to 9 or None in case the cell is empty. It mutates the array in order
    to return the solution.
    """

    # Go through all numbers in the Sudoku.
    for row in range(9):
        for column in range(9):
            # Try all possible combinations of numbers recursively and look for
            # one that is a correct solution.
            if sudoku[row][column] is None:
                # Filter combinations that we see are not going to be possible
                # up front.
                seen = set([])
                box_row_base = (row / 3) * 3
                box_col_base = (column / 3) * 3
                for i in range(9):
                    # Numbers seen in this row.
                    seen.add(sudoku[row][i])
                    # Numbers seen in this column.
                    seen.add(sudoku[i][column])
                    # Numbers seen in this box.
                    seen.add(sudoku[box_row_base + i / 3][box_col_base + i % 3])

                # Try all solutions we consider possible at this point.
                for candidate in set(range(1, 10)) - seen:
                    sudoku[row][column] = candidate
                    if solve(sudoku):
                        return True

                # If none of the numbers returned a valid solution, restore the
                # state of the Sudoku and return to the parent so it can try a
                # different solution.
                sudoku[row][column] = None
                return False

    return True

# Read and solve all Sudokus from Project Euler!
# https://projecteuler.net/problem=96
file = open('p096_sudoku.txt')
while True:
    name = file.readline().rstrip()
    if name == '':
        break

    sudoku = []
    for _ in range(9):
        row = [None if num == '0' else int(num) for num in list(file.readline().rstrip())]
        sudoku.append(row)

    solve(sudoku)
    print_sudoku(sudoku, name=name)
