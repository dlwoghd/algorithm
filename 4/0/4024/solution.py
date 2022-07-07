def solution(row, col, data):
    answer = 0
    graph = list(map(lambda x: list(map(lambda y: True if y == 'L' else False, x.split(" "))), data.split("\n")))
    for row in graph:
        print(row)

    return answer


row = 10
col = 12
data = """L . . . . . . . . L . .
. L . . . . . . . L L .
L L . . . . . . . . L .
. L . . . . . . . . . L
. . L . . . . . . . . L
. . . . . . L . . . . .
. . . . . L . L . . . .
. . . . L . L . L . . .
. . . . . L . L . . . .
. . . . . . L . . . . L"""

if __name__ == '__main__':
    solution(row, col, data)
