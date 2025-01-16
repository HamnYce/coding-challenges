# A -
# n, x = map(int, input().split())
# arr = list(map(int, input().split()))

# i = 0
# j = 0
# total = 0
# shortest_distance = 10**20


# while j < n:
#     total += arr[j]
#     j += 1
#     while i <= j and total >= x:
#         shortest_distance = min(shortest_distance, j - i)
#         total -= arr[i]
#         i += 1


# print(shortest_distance if shortest_distance != 10**20 else -1)


# B -
# import sys
# lines = sys.stdin.readlines()
# xs = []
# n = int(lines[0])
# for line in lines[1:]:
#     xs.append(int(line))
# xs = list(sorted(xs))
# i = 0
# j = n // 2
# total = 0
# while i < n // 2 and j < n:
#     if xs[j] >= 2 * xs[i]:
#         total += 1
#         i += 1
#     j += 1

# print(n - total)

# C -
# from bisect import bisect_left
# n = int(input())
# worms = list(map(int, input().split()))
# for i in range(1, n):
#     worms[i] += worms[i - 1]
# m = int(input())
# qs = map(int, input().split())
# for q in qs:
#     print(bisect_left(worms, q) + 1)

# D -
# from bisect import bisect_right
# from sys import stdout
# n, m = map(int, input().split())
# ais = list(sorted(map(int, input().split())))
# bis = map(int, input().split())

# for b in bis:
#     stdout.write(f"{bisect_right(ais, b)} ")

# E -
# n, t = map(int, input().split())
# times = list(map(int, input().split()))

# i, j = 0, 0
# total_time = 0
# max_books = 0

# while i <= j and j < n:
#     if total_time <= t:
#         max_books = max(max_books, j - i)
#         total_time += times[j]
#         j += 1
#         if total_time <= t:
#             max_books = max(max_books, j - i)
#     else:
#         total_time -= times[i]
#         i += 1

# print(max_books)

# F -
# Formula: 100 * p_i / sum(p[:i]) <= k
# Rearrange to get sum(p[:]): sum(p[:i]) >= 100 * p_i / k
# Then check at each stage if total is atleast that if not set it to that
# from math import ceil
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     ps = list(map(int, input().split()))
#     total = ps[0]
#     for i in range(1, n):
#         total = max(total, ceil(100 * ps[i] / k))
#         total += ps[i]
#     print(total - sum(ps))

# G -
# lo = -10**9 * 2
# hi = 10**9 * 2

# n = int(input())
# good = True
# for _ in range(n):
#     op, num_s, truth = input().split()
#     num = int(num_s)

#     if not good:
#         continue

#     if truth == 'N':
#         if op == ">":
#             op = "<="
#         elif op == "<":
#             op = ">="
#         elif op == ">=":
#             op = "<"
#         elif op == "<=":
#             op = ">"
#     if op == ">":
#         lo = max(lo, num)
#     elif op == "<":
#         hi = min(hi, num)
#     elif op == ">=":
#         lo = max(lo, num - 1)
#     elif op == "<=":
#         hi = min(hi, num + 1)

#     if lo + 1 >= hi:
#         good = False

# if good:
#     print(lo + 1)
# else:
#     print("Impossible")

# H -
# n, k = map(int, input().split())
# xs = list(sorted(map(int, input().split())))
# xs = xs[n // 2:]
# xs.reverse()
# curr_median = xs.pop()
# count_of_meds = 1


# while True:
#     if len(xs) == 0:
#         break
#     # the difference between the median and the next value
#     diff = xs[-1] - curr_median
#     if diff * count_of_meds > k:  # if we dont have enough k to make it to the next value then break
#         break
#     k -= diff * count_of_meds
#     curr_median = xs[-1]  # curr value of median is this value
#     count_of_meds += 1  # add one more median to the list
#     xs.pop()

# curr_median += k // count_of_meds

# print(curr_median)

# I&J -
# n, k = map(int, input().split())
# want = list(map(int, input().split()))
# have = list(map(int, input().split()))


# def win_func(amount):
#     if amount <= 0:
#         return True

#     global want, have, k, n
#     total_cost = 0
#     for i in range(n):
#         total_cost += max(amount * want[i] - have[i], 0)
#     return total_cost <= k


# lo = -1
# hi = 10**10
# m = 0
# while lo + 1 < hi:
#     m = (lo + hi) // 2
#     if win_func(m):
#         lo = m
#     else:
#         hi = m

# lo -= 10
# while win_func(lo):
#     lo += 1

# print(lo - 1)

# K -
# recipe = input()
# want = [recipe.count('B'), recipe.count('S'), recipe.count('C'), ]
# have = list(map(int, input().split()))
# prices = list(map(int, input().split()))
# money = int(input())


# def win_func(amount):
#     global want, have, money, prices
#     if amount <= 0:
#         return True

#     total_cost = 0
#     for i in range(3):
#         amount_needed = max(amount * want[i] - have[i], 0)
#         total_cost += amount_needed * prices[i]

#     return total_cost <= money


# lo = -1
# hi = 10**13
# m = 0
# while lo + 1 < hi:
#     m = (lo + hi) // 2
#     if win_func(m):
#         lo = m
#     else:
#         hi = m

# lo -= 10
# while win_func(lo):
#     lo += 1

# print(lo - 1)

# L -
# from sys import stdin


# def win_func(stalls, cows, min_step):
#     if min_step <= 1:
#         return True

#     count = 1
#     last_stall = stalls[0]
#     for i in range(1, len(stalls)):
#         if count >= cows:
#             break
#         if stalls[i] - last_stall >= min_step:
#             count += 1
#             last_stall = stalls[i]
#     return count >= cows


# t = int(stdin.readline())
# for _ in range(t):
#     n, cows = map(int, stdin.readline().split())
#     stalls = []
#     for _ in range(n):
#         stalls.append(int(stdin.readline()))
#     stalls = list(sorted(stalls))
#     lo = 0
#     hi = stalls[-1] - stalls[0] + 1
#     m = 1
#     while lo + 1 < hi:
#         m = (lo + hi) // 2
#         if win_func(stalls, cows, m):
#             lo = m
#         else:
#             hi = m
#     lo -= 3
#     while win_func(stalls, cows, lo):
#         lo += 1
#     print(lo - 1)

# M -
# def win_func(holes, strip_size, max_strips):
#     if strip_size < 1:
#         return False

#     curr_hole = holes[0]
#     curr_strip = 1
#     for hole in holes:
#         if curr_hole + strip_size < hole:
#             curr_hole = hole
#             curr_strip += 1

#     return curr_strip <= max_strips


# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     holes = list(map(int, input().split()))
#     lo = 1
#     hi = 10**10
#     m = -1
#     while lo + 1 < hi:
#         m = (lo + hi) // 2
#         if win_func(holes, m, k):
#             hi = m
#         else:
#             lo = m
#     lo += 10

#     while win_func(holes, lo, k):
#         lo -= 1

#     print(lo + 2)

# N -
# def win_func(houses, circum):
#     if circum < 0:
#         return (False, 0, [])
#     radius = circum / 2
#     antenna = 1
#     antenna_places = [houses[0] + radius]
#     for house in houses:
#         if len(antenna_places) > 3:
#             return (False, 0, [])
#         if not antenna_places[-1] - radius <= house <= antenna_places[-1] + radius:
#             antenna += 1
#             antenna_places.append(house + radius)

#     if len(antenna_places) > 3:
#         return (False, 0, [])
#     return (True, radius, antenna_places)
#     # check if hosues within range


# # same idea as before with holes and a range of the hole
# n = int(input())
# houses = list(sorted(map(int, input().split())))
# lo = -1
# hi = 10**10
# m = 10**10
# while lo + 1 < hi:
#     m = (lo + hi) // 2
#     if win_func(houses, m)[0]:
#         hi = m
#     else:
#         lo = m

# lo += 10
# while win_func(houses, lo)[0]:
#     lo -= 1

# _, radius, placements = win_func(houses, lo + 1)

# print(f"{radius:.6f}")
# while len(placements) < 3:
#     placements.append(placements[-1])
# for p in placements:
#     print(f"{p:.6f}", end=" ")
