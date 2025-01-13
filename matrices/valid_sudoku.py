from typing import List

def valid_sudoku(board: List[List[str]]) -> bool:
    col_map = {}
    by3_map = {}
    by3_idx = 0

    for idx, row in enumerate(board):
        row_set = set()
        for i, num in enumerate(row):
            if num.isdigit():
                if num in row_set:
                    return False

                if i in col_map and num in col_map[i]:
                    return False

                if by3_idx in by3_map and num in by3_map[by3_idx]:
                    return False

                row_set.add(num)
                col_map.setdefault(i, set()).add(num)
                by3_map.setdefault(by3_idx, set()).add(num)

            if i < len(board) - 1 and (i + 1) % 3 == 0:
                by3_idx += 1

        if (idx + 1) % 3 == 0:
            by3_idx += 1
        else:
            by3_idx -= 2
    return  True



print(valid_sudoku([["5","3",".",".","7",".",".",".","."],
                    ["6",".",".","1","9","5",".",".","."],
                    [".","9","8",".",".",".",".","6","."],
                    ["8",".",".",".","6",".",".",".","3"],
                    ["4",".",".","8",".","3",".",".","1"],
                    ["7",".",".",".","2",".",".",".","6"],
                    [".","6",".",".",".",".","2","8","."],
                    [".",".",".","4","1","9",".",".","5"],
                    [".",".",".",".","8",".",".","7","9"]]))


