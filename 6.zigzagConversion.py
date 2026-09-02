class Solution:
    def convert(self, s: str, numRows: int) -> str:

        grid = {}
        for i in range(numRows):
            grid[f"r{i}"] = ""

        output = ''
        self.direction = True
        self.current_row = 0

        for current_char in s:
            grid[f"r{self.current_row}"] += current_char

            if self.direction:
                if self.current_row+1 < numRows:
                    self.current_row += 1
                else:
                    self.direction = not self.direction
                    if self.current_row > 0:self.current_row -= 1
            else:
                if self.current_row > 0:
                    self.current_row -= 1
                else:
                    self.direction = not self.direction
                    if self.current_row+1 < numRows:self.current_row += 1


        for i in range(numRows):
            output += grid[f"r{i}"]

        return output