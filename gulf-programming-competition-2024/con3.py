# A -
# n = int(input())
# xs = map(int, input().split())
# total = 0
# ks = [0] * 150005
# ks[0] = 1
# for x in sorted(xs):
#     if ks[x - 1]:
#         if ks[x]:
#             if ks[x + 1]:
#                 continue
#             else:
#                 ks[x + 1] = 1
#         else:
#             ks[x] = 1
#     else:
#         ks[x - 1] = 1

# ks[0] = 0
# print(sum(ks))

# B -
# import sys
# readline = sys.stdin.readline
# write = sys.stdout.write
# n, m = map(int, readline().split())
# xs = list(map(int, readline().split()))
# ltr = [0] * n
# rtl = [0] * n
# for i in range(1, n):
#     ltr[i] = min(xs[i] - xs[i - 1], 0)

# for i in range(n - 2, -1, -1):
#     rtl[i] = min(xs[i] - xs[i + 1], 0)

# for i in range(1, n):
#     ltr[i] += ltr[i - 1]

# for i in range(n - 2, -1, -1):
#     rtl[i] += rtl[i + 1]
# for i in range(n):
#     ltr[i] = abs(ltr[i])
#     rtl[i] = abs(rtl[i])

# for _ in range(m):
#     s, t = map(int, readline().split())
#     s -= 1
#     t -= 1
#     if s < t:
#         write(f"{ltr[t] - ltr[s]}\n")
#     else:
#         write(f"{rtl[t] - rtl[s]}\n")


# C -
# n = int(input())
# tri = n * (n + 1) // 2
# print(1 + 6 * tri)

# D -
# n, m = map(int, input().split())
# d = dict()
# xs = map(int, input().split())
# for x in xs:
#     if x not in d:
#         d[x] = 0
#     d[x] += 1

# foods = [0] * 105

# for k, val in d.items():
#     foods[k] = val

# eating = [0] * len(foods)
# death = False
# for _ in range(n):
#     best_food_to_eat = -1
#     best_index = -1
#     for i in range(len(foods)):
#         days_last = foods[i] // (eating[i] + 1)
#         if days_last > best_food_to_eat:
#             best_food_to_eat = days_last
#             best_index = i
#     eating[best_index] += 1

# maxi = 100000
# for i in range(len(foods)):
#     if eating[i] == 0:
#         continue
#     maxi = min(maxi, foods[i] // eating[i])
# print(maxi)


# E -
# s, t, x = map(int, input().split())
# xs = [0] * 24
# while s != t:
#     xs[s] = 1
#     s = (s + 1) % 24

# xs[t] = 0
# if xs[x]:
#     print("Yes")
# else:
#     print("No")
