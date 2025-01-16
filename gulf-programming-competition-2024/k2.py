# A -
# t = s
# total = 0

# while 'ab' in s:
#     i = s.index('ab')
#     s = s[:i] + 'bba' + s[i+2:]
#     total += 1
#     print(s)

# s = t

# s = input()
# manual_total = 0
# dist = 0
# test_dist = 0
# for c in reversed(s):
#     if c == 'b':
#         dist += 1
#     else:
#         manual_total += dist
#         dist = (dist * 2) % int(1e9 + 7)
# print(manual_total % int(1e9 + 7))

# B -
# from math import gcd
# def relatively_prime(n):
#     relative_primes = set()
#     for i in range(1, n):
#         if gcd(n, i) == 1:
#             relative_primes.add(i)
#     return relative_primes
# def primitive_roots(n):
#     total = 0
#     relative_primes = relatively_prime(n)
#     for x in range(1, n):
#         powers = set()
#         for p in range(n - 1):
#             val = x**p % n
#             if val in powers:
#                 break
#             powers.add(val)
#         if len(relative_primes.intersection(powers)) == len(relative_primes):
#             total += 1
#     return total
# anses = []
# for i in range(1, 2001):
#     print(i)
#     anses.append(primitive_roots(i))
# with open('o.txt', 'w') as f:
#     f.write(str(anses))

# x = //hard coded in here from o.txt
# print(x[int(input()) - 1])

# C -
# from math import gcd, ceil
# UB = 5*(10**18)
# x, y, d = 0, 0, 0


# def extended_euclid(a, b):
#     global x, y, d
#     if (b == 0):
#         x = 1
#         y = 0
#         d = a
#         return
#     extended_euclid(b, a % b)
#     x1 = y
#     y1 = x - (a // b) * y
#     x = x1
#     y = y1


# a, b, c = map(int, input().split())
# c = -c
# extended_euclid(a, b)
# if c % d == 0:
#     x0 = x * c // gcd(a, b)
#     y0 = y * c // gcd(a, b)

#     def new_x(n):
#         return x0 + (b//d)*n

#     def new_y(n):
#         return y0 - (a//d)*n

#     lower_boundary = ceil(max((-UB-x0) / (b//d), (UB-y0) / -(a//d)))
#     upper_boundary = int(min((UB-x0) / (b//d), (-UB-y0) / -(a//d)))

#     if lower_boundary <= upper_boundary:
#         n = (lower_boundary + upper_boundary) // 2
#         print(new_x(n), new_y(n))
#     else:
#         print(-1)
# else:
#     print(-1)

# E
# n, m = map(int, input().split())
# mat = []
# for _ in range(n):
#     mat.append(input().split())
# total = - (n * m)

# for row in range(n):
#     total += 2**mat[row].count('0') - 1
#     total += 2**mat[row].count('1') - 1

# for col in range(m):
#     count_0 = 0
#     count_1 = 0
#     for row in range(n):
#         if mat[row][col] == '0':
#             count_0 += 1
#         elif mat[row][col] == '1':
#             count_1 += 1
#     total += 2**count_0 - 1
#     total += 2**count_1 - 1


# print(total)

# F -
# with open('input.txt') as f:
#     from math import comb
#     k, n = map(int, f.readline().split())
#     open('output.txt', 'w').write(f"{comb(n, k) % int(1e9 + 7)}")

# G -
# from math import lcm
# n = int(input())
# xs = list(map(int, input().split()))
# val = lcm(*xs)
# total = 0
# for x in xs:
#     total += val // x
# print(total % int(1e9+7))

# H -
# from math import comb
# color_amount = int(input())
# colors = [0] * color_amount
# for i in range(color_amount):
#     colors[i] = int(input())

# total_balls = colors.copy()
# for i in range(1, color_amount):
#     total_balls[i] += total_balls[i - 1]

# total_ways = [1] * color_amount
# for i in range(1, color_amount):
#     partitions = total_balls[i - 1]
#     ball_amount = colors[i] - 1
#     total_ways[i] = comb(partitions + ball_amount, ball_amount) * total_ways[i - 1]

# print(total_ways[-1] % int(1e9+7))

# I -
# from math import comb
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     print(comb(n + m - 1, m - 1) % int(1e9 + 7))

# J -
