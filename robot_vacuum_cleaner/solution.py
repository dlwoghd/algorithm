from collections import deque


class RobotVacuumCleaner:
    board = []
    is_horiz = 1
    is_not_horiz = 0
    counter = 1
    queue = deque()
    n = 0

    def __init__(self, n: int, horizrizontal: bool):
        self.n = n
        self.board = [[False] * n for _ in range(n)]
        self.is_horiz = 1 if horizrizontal else 0
        self.is_not_horiz = 0 if horizrizontal else 1

    def start(self):
        self.queue.append((0, 0))

        while self.queue:
            row, col = self.queue.popleft()
            self.board[row][col] = self.counter
            self.counter += 1
            next_row, next_col = self.next(row, col)
            if next_row < self.n and next_col < self.n and next_row >= 0 and next_col >= 0:
                self.queue.append((next_row, next_col))

        return self.board

    def next(self, row, col):
        if row > col:
            if col == 0:
                if row % 2 == 0:
                    row += 1 and self.is_horiz
                    col += 1 and self.is_not_horiz
                else:
                    col += 1 and self.is_horiz
                    row += 1 and self.is_not_horiz
            elif row % 2 == 0:
                col -= 1 and self.is_horiz
                col += 1 and self.is_not_horiz
            else:
                col += 1 and self.is_horiz
                col -= 1 and self.is_not_horiz
        elif row < col:
            if row == 0:
                if col % 2 == 0:
                    row += 1 and self.is_horiz
                    col += 1 and self.is_not_horiz
                else:
                    col += 1 and self.is_horiz
                    row += 1 and self.is_not_horiz
            elif col % 2 == 0:
                row += 1 and self.is_horiz
                row -= 1 and self.is_not_horiz
            else:
                row -= 1 and self.is_horiz
                row += 1 and self.is_not_horiz
        else:
            if row == 0:
                row += 1 and self.is_horiz
                col += 1 and self.is_not_horiz

            elif row % 2 == 0:
                col -= 1 and self.is_horiz
                row -= 1 and self.is_not_horiz
            else:
                row -= 1 and self.is_horiz
                col -= 1 and self.is_not_horiz

        return [row, col]


if __name__ == '__main__':
    robotVacuumCleaner = RobotVacuumCleaner(5, True).start()

    for row in robotVacuumCleaner:
        print(row)
