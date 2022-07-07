class LakeSearch:
    vx = [0, 1, 0, -1]
    vy = [-1, 0, 1, 0]

    def __init__(self, row, col, string_data):
        self.row = row
        self.col = col
        self.graph = list(
            map(lambda x: list(map(lambda y: True if y == 'L' else False, x.split(" "))),
                string_data.split("\n")[1:-1]))
        self.visited = [[False] * col for _ in range(self.row)]

    def search(self, r_idx, c_idx, current_visited):

        if r_idx < 0 or c_idx < 0 or r_idx >= self.row or c_idx >= self.col:
            return False

        if (r_idx, c_idx) in current_visited or self.graph[r_idx][c_idx]:
            return current_visited

        if self.visited[r_idx][c_idx]:
            return False

        self.visited[r_idx][c_idx] = True

        current_visited.add((r_idx, c_idx))

        for vector in range(4):
            if not current_visited:
                return False

            current_visited = self.search(r_idx + self.vy[vector], c_idx + self.vx[vector], current_visited)

        return current_visited

    def process(self):
        answer = 0
        mini = float('inf')
        maxi = 0

        for r_idx in range(self.row):
            for c_idx in range(self.col):
                if not self.graph[r_idx][c_idx]:
                    visited = set()
                    check = self.search(r_idx, c_idx,visited)
                    if check and len(check) > 0:
                        r = len(check)
                        answer += 1
                        mini = min(mini, r)
                        maxi = max(maxi, r)

        print(answer, mini, maxi)

        return answer


def solution(row, col, data):
    searcher = LakeSearch(row, col, data)
    answer = searcher.process()

    return answer


row = 10
col = 12
data = """
L . . . . . . . . L . .
. L . . . . . . . L L .
L L . . . . . . . . L .
. L . . . . . . . . . L
. . L . . . . . . . . L
. . . . . . L . . . . .
. . . . . L . L . . . .
. . . . L . L . L . . .
. . . . . L . L . . . .
. . . . . . L . . . . L
"""

if __name__ == '__main__':
    solution(row, col, data)
