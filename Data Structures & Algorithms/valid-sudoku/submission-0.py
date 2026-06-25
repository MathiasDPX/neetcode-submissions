from itertools import chain

class Solution:
    def contain_duplicate(self, subset):
        for i in range(1, 10):
            if subset.count(str(i)) > 1:
                return True

        return False

    def get_subboxes(self, board, idx):
        # Get the box coordinates (from 0 to 2 in both axis) from its index
        x = idx % 3
        y = idx // 3

        # Cut the board into a 3x3 sub-box
        box = [row[x*3 : x*3+3] for row in board[y*3 : y*3+3]]

        # Convert the 2d sub-box into a 1d array
        return list(chain.from_iterable(box))

    def get_row(self, board, idx):
        return board[idx]

    def get_column(self, board, idx):
        return [row[idx] for row in board]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            # Each Sudoku has 9 rows, 9 columns and 9 sub-boxes

            row = self.get_row(board, i)
            col = self.get_column(board, i)
            box = self.get_subboxes(board, i)

            if self.contain_duplicate(row) or self.contain_duplicate(col) or self.contain_duplicate(box):
                return False

        return True