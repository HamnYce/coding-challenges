

# A -

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     good = False
#     for i in range(1, n):
#         if i % 3 == 0:
#             continue
#         for j in range(i+1, n):
#             if j % 3 == 0:
#                 continue
#             k = n - (i+j)
#             if k % 3 == 0 or k <= j:
#                 continue
#             if i + j + k == n:
#                 good = True
#                 print(f"YES\n{i} {j} {k}")
#             if good:
#                 break
#         if good:
#             break
#     if not good:
#         print("NO")

# C -
# infile = open('input.txt')
# outfile = open('output.txt', 'w')
# lines = iter(infile.readlines())
# n, m = map(int, next(lines).split())
# crops = []
# for _ in range(n):
#     crops.append(list(map(int, next(lines).split())))
# A, B, C = map(int, next(lines).split())
# comp = list(sorted([A,B,C]))
# total = 0

# for i in range(n):
#     for j in range(1, m):
#         crops[i][j] += crops[i][j-1]

# for j in range(m):
#     for i in range(1, n):
#         crops[i][j] += crops[i - 1][j]


# # check last row
# last_row = n - 1
# for j in range(m - 2):
#     for k in range(j+1, m - 1):
#         a = crops[last_row][j]
#         b = crops[last_row][k] - crops[last_row][j]
#         c = crops[last_row][m - 1] - crops[last_row][k]

#         if sorted([a,b,c]) == comp :
#             total += 1

# last_column = m - 1
# for i in range(n - 2):
#     for j in range(i+1, n - 1):
#         a = crops[i][last_column]
#         b = crops[j][last_column] - crops[i][last_column]
#         c = crops[n - 1][last_column] - crops[j][last_column]
#         if sorted([a, b, c]) == comp:
#             total += 1

# outfile.write(f"{total}")

# # D -
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     if k < 3:
#         for _ in range(k):
#             n = len(arr)
#             smallest_diff = 10**20
#             for i in range(n):
#                 for j in range(i+1, n):
#                     smallest_diff = min(smallest_diff, abs(arr[i]-arr[j]))

#             arr.append(smallest_diff)
#         print(min(arr))
#     else:
#         print(0)

# E -
# from math import ceil
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = list(sorted(map(int, input().split())))
#     mid = ceil(n / 2)
#     arr = arr[mid - 1:]
#     n = len(arr)
#     median = arr[0]
#     i = 0
#     while i < n:
#         arr[i] -= median
#         if arr[i] != 0:
#             break
#         i+=1
#     print(i)


# F -
# n = int(input())
# total = 0
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     if a+b+c >1:
#         total+=1
# print(total)

# G -
