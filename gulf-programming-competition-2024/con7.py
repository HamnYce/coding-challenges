# A -
# t = int(input())
# for _ in range(t):
#     m = int(input())
#     board = []

#     board.append(list(map(int, input().split())))
#     board.append(list(map(int, input().split())))

#     for j in range(1, m):
#         board[0][j] += board[0][j - 1]
#         board[1][j] += board[1][j - 1]

#     least_b = 1e10
#     for down_here in range(m):
#         if down_here == 0:
#             bottom_b = 0
#         else:
#             bottom_b = board[1][down_here - 1]

#         if down_here == m - 1:
#             upper_b = 0
#         else:
#             upper_b = board[0][m - 1] - board[0][down_here]

#         curr_b = max(bottom_b, upper_b)
#         least_b = min(least_b, curr_b)
#     print(least_b)

# B -
# n, k = map(int, input().split())
# l = -1
# r = 2**(n + 1)
# m = (l + r) // 2
# i = n + 1
# k -= 1
# while m != k:
#     m = (l + r) // 2
#     if k == m:
#         break
#     if k < m:
#         r = m
#     if k > m:
#         l = m
#     i -= 1
# print(i)


# C -
# t = int(input())
# for _ in range(t):
#     rating = int(input())
#     print("Division ", end="")

#     if rating <= 1399:
#         print(4)
#     elif rating <= 1599:
#         print(3)
#     elif rating <= 1899:
#         print(2)
#     else:
#         print(1)

# D -
# from bisect import bisect_left
# n, m = map(int, input().split())
# dorms = list(map(int, input().split()))
# letters = list(map(int, input().split()))

# for i in range(1, n):
#     dorms[i] += dorms[i - 1]


# for letter in letters:
#     dorm_number = bisect_left(dorms, letter)
#     if dorm_number == 0:
#         room_number = letter
#     else:
#         room_number = letter - dorms[dorm_number - 1]

#     print(dorm_number + 1, room_number)

# E -
# n = int(input())

# wd = []
# for _ in range(n):
#     op = input()
#     if op == 'pwd':
#         print('/', end="")
#         for dir in wd:
#             print(dir, end="/")
#         print()
#     else:
#         new_dir = op[3:]

#         if new_dir[0] == '/':
#             wd = []
#         for dir in new_dir.split('/'):
#             if dir == '':
#                 continue
#             if dir == '..':
#                 wd.pop()
#             else:
#                 wd.append(dir)
