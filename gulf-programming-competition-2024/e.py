
# A -
# input()
# a = [0] * 101
# for x in map(int, input().split()):
#   a[x] += 1
# print(sum(a) - max(a))

# B -
# n, d = map(int, input().split())
# a = [0] * (2*(10**4) + 10)
# t = 0
# for x in map(int, input().split()):
#   a[x] += 1

# for i in range(len(a) - 2*d):
#   t += a[i] * a[i + d] * a[i+d+d]

# print(t)

# C -
# import sys
# n = sys.stdin.readline()
# a = list(map(int, sys.stdin.readline().split()))

# for i in range(1, len(a)):
#   a[i] += a[i-1]

# D -
# q = int(sys.stdin.readline())
# for _ in range(q):
#   l, r = map(int, sys.stdin.readline().split())
#   if l == 0:
#     sys.stdout.write(f"{a[r]}\n")
#   else:
#     sys.stdout.write(f"{a[r] - a[l-1]}\n")

# E -
# import sys
# lines = sys.stdin.readlines()
# num_to_freq = dict()
# freq_to_num = dict()

# for line in lines[1:]:
#     query, x = map(int, line.split())
#     if query == 1:
#         if x not in num_to_freq:
#             num_to_freq[x] = 0
#         if num_to_freq[x] not in freq_to_num:
#             freq_to_num[num_to_freq[x]] = 0
#         freq_to_num[num_to_freq[x]] -= 1
#         num_to_freq[x] += 1
#         if num_to_freq[x] not in freq_to_num:
#             freq_to_num[num_to_freq[x]] = 0
#         freq_to_num[num_to_freq[x]] += 1
#     elif query == 2:
#         if x in num_to_freq:
#             freq_to_num[num_to_freq[x]] -= 1
#             num_to_freq[x] = max(0, num_to_freq[x] - 1)
#             freq_to_num[num_to_freq[x]] += 1
#     else:
#         sys.stdout.write(
#             f"{1 if x in freq_to_num and freq_to_num[x] else 0}\n")

# F -
# import sys
# lines = sys.stdin.readlines()
# s = lines[0]
# s = "$" + s
# slen = len(s)
# a = [0] * slen

# for i in range(slen - 1):
#     if s[i] == s[i + 1]:
#         a[i] = 1

#     if (i - 1) > 0:
#         a[i] += a[i - 1]

# a[-1] += a[-2]

# for line in lines[2:]:
#     l, r = map(int, line.split())
#     sys.stdout.write("{}\n".format(a[r - 1] - a[l - 1]))
#

# G -
# min_j = 0
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# for i in range(1, len(a)):
#     a[i] += a[i - 1]

# min_j = k - k
# min_val = a[k]

# for i in range(k + 1, len(a) - k):
#     if a[i] - a[i - k] < min_val:
#         min_val = a[i] - a[i - k]
#         min_j = i - k

# print(min_j)
# print(min_val)

# H -
# import sys
# lines = sys.stdin.readlines()
# a = list(map(int, lines[1].split()))
# sa = list(sorted(a))

# for i in range(1, len(a)):
#     a[i] += a[i - 1]
#     sa[i] += sa[i - 1]

# for line in lines[3:]:
#     i, l, r = map(int, line.split())
#     if l == 1:
#         left = 0
#     else:
#         left = a[l - 2] if i == 1 else sa[l - 2]

#     right = a[r - 1] if i == 1 else sa[r - 1]
#     sys.stdout.write(f"{right - left}\n")

# I -
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# t = 0

# for i, b in enumerate(map(int, input().split())):
#     if b == 1:
#         t += a[i]
#         a[i] = 0

# for i in range(1, len(a)):
#     a[i] += a[i - 1]

# pt = a[k - 1]
# for i in range(k, len(a)):
#     pt = max(pt, a[i] - a[i - k])

# print(t + pt)

# J -
# input()
# a = list(map(int, input().split()))
# d = dict()
# t = 0
# nice = []
# for i in range(len(a)):
#     if a[i] not in d:
#         d[a[i]] = []

#     d[a[i]].append(i)
#     t += a[i]

# m = max(d)
# if len(d[m]) == 1:
#     for k, v in d.items():
#         if k == m:
#             continue
#         if t - k == 2 * m:
#             nice += v
#     mv = d.pop(m)
#     new_m = max(d)
#     if t - m == 2 * new_m:
#         nice += mv

# else:
#     for k, v in d.items():
#         if t - k == 2 * m:
#             nice += v


# print(len(nice))
# for i in nice:
#     print(f"{i + 1}", end=" ")

# K -
# import sys
# lines = sys.stdin.readlines()
# LENGTH = 200_010
# arr = [0] * LENGTH

# n, k, q = map(int, lines[0].split())

# for recipe in lines[1:1 + n]:
#     l, r = map(int, recipe.split())
#     arr[l] += 1
#     arr[r + 1] -= 1

# for i in range(1, LENGTH):
#     arr[i] += arr[i - 1]

# for i in range(1, LENGTH):
#     arr[i] = 1 if arr[i] >= k else 0
#     arr[i] += arr[i - 1]

# for query in lines[1 + n:]:
#     a, b = map(int, query.split())
#     sys.stdout.write("{}\n".format(arr[b] - arr[a - 1]))

# L -
# import sys
# n, m, k = map(int, sys.stdin.readline().split())

# base = list(map(int, sys.stdin.readline().split()))
# a = [0] * n

# ops = []
# ops_pref = [0] * m


# for _ in range(m):
#     ops.append(tuple(map(int, sys.stdin.readline().split())))

# for _ in range(k):
#     l, r = map(int, sys.stdin.readline().split())
#     ops_pref[l - 1] += 1
#     if r < m:
#         ops_pref[r + 1 - 1] -= 1

# for i in range(1, m):
#     ops_pref[i] += ops_pref[i - 1]

# for i in range(m):
#     l, r, d = ops[i]
#     a[l - 1] += d * ops_pref[i]
#     if r < n:
#         a[r + 1 - 1] -= d * ops_pref[i]

# for i in range(1, n):
#     a[i] += a[i - 1]

# for i in range(n):
#     sys.stdout.write("{} ".format(base[i] + a[i]))

# M -
# import sys
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n, m = map(int, sys.stdin.readline().split())

#     prog = list(map(lambda s: 1 if s == '+' else -
#                 1, sys.stdin.readline().strip()))

#     for i in range(1, n):
#         prog[i] += prog[i - 1]

#     pref: list[tuple[int, int]] = [(0, 0)] * n
#     pref[0] = (prog[0], prog[0])

#     for i in range(1, n):
#         prev_min, prev_max = pref[i - 1]
#         min_i = min(prev_min, prog[i])
#         max_i = max(prev_max, prog[i])
#         pref[i] = (min_i, max_i)

#     suff: list[tuple[int, int]] = [(0, 0)] * n
#     suff[-1] = (prog[-1], prog[-1])

#     for i in range(n - 2, -1, -1):
#         prev_min, prev_max = suff[i + 1]
#         min_i = min(prev_min, prog[i])
#         max_i = max(prev_max, prog[i])
#         suff[i] = (min_i, max_i)

#     for _ in range(m):
#         x, y = map(lambda i: i - 1, map(int, sys.stdin.readline().split()))
#         vals = [0]
#         offset = prog[y]

#         if x > 0 and y < n - 1:
#             offset = prog[y] - prog[x - 1]

#         if x > 0:
#             vals.append(pref[x - 1][0])
#             vals.append(pref[x - 1][1])
#         if y < n - 1:
#             vals.append(suff[y + 1][0] - offset)
#             vals.append(suff[y + 1][1] - offset)

#         sys.stdout.write(f"{max(vals) - min(vals) + 1}\n")
