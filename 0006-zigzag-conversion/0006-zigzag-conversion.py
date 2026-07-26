class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        stepping_down = False

        for char in s:
             rows[current_row] += char

             if current_row == 0 or current_row == numRows - 1:
                stepping_down = not stepping_down

             current_row += 1 if stepping_down else -1
        return "".join(rows)