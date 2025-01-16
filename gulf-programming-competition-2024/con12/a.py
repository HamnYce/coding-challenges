# s = input()
# ans = []
# si = 0
# ci = 0
# for c in s:

#     if c == 'C':
#         ci += 1
#         si = 0
#         if ci == 3:
#             ans.append('P')
#             ci = 0
#         else:
#             ans.append('B')
#     if c == 'S':
#         si += 1
#         ci = 0
#         if si == 3:
#             ans.append('T')
#             si = 0
#         else:
#             ans.append('D')

# print(''.join(ans))


# import sys
# import math
# for _ in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     x = math.isqrt(n*2)
#     if x*(x+1) // 2 > n:
#         print(x-1)
#     else:
#         print(x)

# n, a, p = map(int, input().split())
# p /= 100
# print(n + a*p - a*(1-p))

import sys
input = sys.stdin.readline
n = int(input())
points = [int(input()) for _ in range(n)]
grades = [n for _ in range(n)]


