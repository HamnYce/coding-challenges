# C -
# from math import ceil

# n, m, x, y, z = map(int, input().split())
# sub_z = min(z * 3, n)
# n -= sub_z
# z -= ceil(sub_z / 3.0)

# sub_y = min(y * 2, n)
# n -= sub_y
# y -= ceil(sub_y / 2.0)

# if n + m <= x + y + z:
#     print('Yes')
# else:
#     print('No')

# D -
# from math import ceil

# n, m, k = map(int, input().split())


# H -
# n = int(input())
# xs = list(sorted(map(int, input().split())))
# for i in range(n):
#     print(xs[i], xs[-i-1], end=" ")


# K
# board = []
# for _ in range(16):
#     board.append(input())
# e = [0, 0]
# head = [0, 0]
# for i in range(len(board)):
#     for j in range(len(board[i])):
#         if board[i][j] == 'E':
#             e = [i, j]
#         if board[i][j] == ':':
#             head = [i, j]


# moves = input()
# for move in moves:
#     if move == '<':
#         head[1] -= 1
#     elif move == '>':
#         head[1] += 1
#     elif move == 'v':
#         head[0] += 1
#     elif move == '^':
#         head[0] -= 1

# print('Yes' if head == e else 'No')
