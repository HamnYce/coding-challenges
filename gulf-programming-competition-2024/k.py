# A -
# input()
# print('25')

# B -
# for _ in range(int(input())):
#     l, r = map(int, input().split())
#     lcm = l * 2
#     if lcm <= r:
#         print(f"{l} {lcm}")
#     else:
#         print("-1 -1")

# C -
# from bisect import bisect_right
# from math import isqrt
# nums = list(map(int, input().split()))
# a = min(nums)
# b = max(nums)
# factors_a = set()
# factors_b = set()
# for i in range(1, isqrt(a) + 1):
#     if a % i == 0:
#         opposite = a // i
#         factors_a.add(i)
#         factors_a.add(opposite)

# for i in range(1, isqrt(b) + 1):
#     if b % i == 0:
#         opposite = b // i
#         factors_b.add(i)
#         factors_b.add(opposite)

# sorted_factors = list(sorted(factors_b.intersection(factors_a)))


# q = int(input())
# for _ in range(q):
#     low, high = map(int, input().split())
#     i = bisect_right(sorted_factors, high) - 1
#     factor = sorted_factors[i]
#     if factor < low:
#         print('-1')
#     else:
#         print(f"{factor}")

# D -
# from functools import reduce
# n = int(input())
# chocolate = input().replace(' ', '')
# if chocolate.count('1') == 0:
#     print('0')
# else:
#     nuts = []
#     for i, c in enumerate(chocolate):
#         if c == '1':
#             nuts.append(i)

#     diffs = []
#     for i in range(len(nuts) - 1):
#         diffs.append(nuts[i + 1] - nuts[i])
#     print(reduce(lambda a, b: a * b, diffs,1))

# E -
# Theory:
# a*b/lcm(a,b) = gcd(a,b)
# a*b/gcd(a,b) = lcm(a,b)
# a*b = lcm(a,b) * gcd(a,b)
# a == lcm(a, b), b == gcd(a,b)
# a == gcd(a, b), b == lcm(a, b)

# from math import gcd, lcm
# t = int(input())
# for _ in range(t):
#     g, l = map(int, input().split())
#     if g == gcd(g, l) and l == lcm(g, l):
#         print(min(g, l), max(g, l))
#     else:
#         print('-1')

# F -
# # from math import isqrt
# # from collections import Counter


# # def prime_factorise(n):
# #     if n == 1:
# #         return Counter([1])

# #     factors = Counter()
# #     for i in range(2, isqrt(n) + 1):
# #         while n % i == 0:
# #             factors[i] += 1
# #             n //= i
# #     if n != 1:
# #         factors[n] += 1
# #     return factors


# # def product(counter):
# #     total = 1
# #     for factor, amount in counter.items():
# #         total *= factor**amount
# #     return total

# # total_factors: Counter[int] = Counter()
# # anses = [0]

# # for i in range(1, 51):
# #     factors = prime_factorise(i)
# #     for factor, amount in factors.items():
# #         total_factors[factor] = max(amount, total_factors[factor])

# #     anses.append(product(total_factors))

# # print(anses)
# anses = [0, 1, 2, 6, 12, 60, 60, 420, 840, 2520, 2520, 27720, 27720, 360360, 360360, 360360, 720720, 12252240, 12252240, 232792560, 232792560, 232792560, 232792560, 5354228880, 5354228880, 26771144400, 26771144400, 80313433200, 80313433200, 2329089562800, 2329089562800, 72201776446800, 144403552893600, 144403552893600, 144403552893600, 144403552893600, 144403552893600, 5342931457063200, 5342931457063200, 5342931457063200, 5342931457063200, 219060189739591200, 219060189739591200, 9419588158802421600, 9419588158802421600, 9419588158802421600, 9419588158802421600, 442720643463713815200, 442720643463713815200, 3099044504245996706400, 3099044504245996706400]
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(anses[n])

# G -
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     if n % 2 == 1:
#         n -= 1

#     print(f"{n // 2}")

# H -
# from math import gcd
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     xs = list(sorted(set(map(int, input().split()))))
#     if len(xs) == 1:
#         print('-1')
#     else:
#         diffs = []
#         for i in range(1, len(xs)):
#             diffs.append(xs[i] - xs[i - 1])

#         print(gcd(*diffs))

# I -
# from math import lcm
# t = int(input())
# for _ in range(t):
#     a = input()
#     b = input()
#     lcm_length = lcm(len(a), len(b))
#     mult_a = lcm_length // len(a)
#     mult_b = lcm_length // len(b)
#     maybe_a = a * mult_a
#     maybe_b = b * mult_b
#     if maybe_a == maybe_b:
#         print(maybe_a)
#     else:
#         print('-1')

# J -
# import sys
# def has_number_divisible(x, n):
#     for i in range(2, n + 1):
#         if x % i:
#             return True
#     return False


# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     xs = list(map(int, sys.stdin.readline().split()))
#     good = True
#     for i, x in enumerate(xs, start=2):
#         if not has_number_divisible(x, i):
#             good = False
#             break

#     print("YES" if good else "NO")


# K -
# t = int(input())
# for n in range(t):
#     n = int(input())
#     best = -1
#     for i in range(2, int(n**.5) + 1):
#         if n%i == 0:
#             best = i
#             break
#     if best == -1:
#         best = n

#     a = n // best
#     b = n - a
#     print(a,b)

# L -
# from math import gcd


# def prime_factorise(n):
#     prime_factors = dict()

#     for i in range(2, int(n**.5) + 1):
#         if n % i == 0:
#             prime_factors[i] = 0
#         while n % i == 0:
#             prime_factors[i] += 1
#             n //= i
#     if n != 1:
#         prime_factors[n] = 1

#     return prime_factors


# a, b = map(int, input().split())
# common = gcd(a, b)
# a //= common
# b //= common

# p_a = prime_factorise(a)
# p_b = prime_factorise(b)
# total = 0
# for v in p_a.values():
#     total += v

# for v in p_b.values():
#     total += v

# if 2 in p_a:
#     del p_a[2]
# if 3 in p_a:
#     del p_a[3]
# if 5 in p_a:
#     del p_a[5]

# if 2 in p_b:
#     del p_b[2]
# if 3 in p_b:
#     del p_b[3]
# if 5 in p_b:
#     del p_b[5]
# if len(p_a) + len(p_b) == 0:
#     print(total)
# else:
#     print('-1')

# M -
# from math import gcd
# from collections import Counter
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     xs = list(map(int, input().split()))
#     counter_xs = Counter(xs)
#     maxi = max(counter_xs)
#     ans = [maxi] * counter_xs[maxi]
#     del counter_xs[maxi]
#     cum_gcd = maxi

#     while len(counter_xs):
#         best_gcd = 0
#         best_num = 0
#         for num in counter_xs:
#             temp_gcd = gcd(cum_gcd, num)
#             if temp_gcd > best_gcd:
#                 best_gcd = temp_gcd
#                 best_num = num

#         cum_gcd = best_gcd
#         ans += [best_num] * counter_xs[best_num]
#         del counter_xs[best_num]

#     for a in ans:
#         print(f"{a} ", end="")
#     print()

# N -
# from math import comb
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     n -= k
#     print(comb(n + k - 1, k - 1))

# O -
# from collections import Counter
# from math import comb
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     followers = Counter(map(int, input().split()))
#     total = 0
#     amount = 0
#     for blogger in sorted(followers, reverse=True):
#         if total + followers[blogger] > k:
#             amount = followers[blogger]
#             break
#         total += followers[blogger]

#     spaces_left = k - total
#     ans = comb(amount, spaces_left) % (10**9 + 7)
#     print(ans)

# P -
# from math import comb
# from bisect import bisect_left
# import sys
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n, m, k = map(int, sys.stdin.readline().split())
#     nums = list(
#         sorted(
#             list(
#                 map(int, sys.stdin.readline().split())
#             )
#         )
#     )
#     total_ways = 0
#     for i in range(m - 1, n):
#         range_size = i - bisect_left(nums, nums[i] - k)

#         total_ways += comb(range_size, m - 1)
#     print(total_ways % (10**9 + 7))
