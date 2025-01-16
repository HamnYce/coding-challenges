# A -
# print(sum(map(int, input().split())))

# B -
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     ordered = map(int, input().split())
#     prefs = map(int, input().split())
#     have = dict()
#     want = dict()

#     for order in ordered:
#         if order not in have:
#             have[order] = 0
#         have[order] += 1

#     for pref in prefs:
#         if pref not in want:
#             want[pref] = 0
#         want[pref] += 1

#     total = 0
#     for pref in want:
#         if pref not in have:
#             continue
#         total += min(have[pref], want[pref])
#     print(total)

# C -
# n, m = map(int, input().split())
# cor = list(map(int, input().split()))
# wro = list(map(int, input().split()))

# min_cor, max_cor = min(cor), max(cor)
# min_wro, max_wro = min(wro), max(wro)
# v = max(2 * min_cor, max_cor)
# if v < min_wro:
#     print(v)
# else:
#     print(-1)

# D -
# from math import ceil
# n, m = map(int, input().split())
# ff = dict()
# for _ in range(m):
#     flat_num, floor_num = map(int, input().split())

#     ff[flat_num] = floor_num

# best_floor_sizes = []
# for floor_size in range(1, 100 + 1):
#     # we want to check if every flat is in its proper floor
#     # we need to generate a proper dictionary to check
#     good = True
#     for flat in ff:
#         if not good:
#             break
#         good = good and ceil(flat / floor_size) == ff[flat]
#     if good:
#         best_floor_sizes.append(floor_size)

# if len(best_floor_sizes):
#     a = ceil(n / best_floor_sizes[0])
#     if all(map(lambda floor_size: ceil(n / floor_size) == a, best_floor_sizes)):
#         print(a)
#     else:
#         print(-1)
# else:
#     print(-1)


# E -
# import sys
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     for i in range(2, n + 1, 2):
#         sys.stdout.write(f"{i} ")
#     for i in range(1, n + 1, 2):
#         sys.stdout.write(f"{i} ")

#     sys.stdout.write("\n")
