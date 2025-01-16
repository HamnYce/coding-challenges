# A -
# def sumi(xs):
#     if len(xs) == 0:
#         return 0
#     return xs[0] + sum(xs[1:])


# for i in range(int(input())):
#     xs = list(map(int, input().split()))
#     print(f"Case {i + 1}: {sumi(xs[1:])}")

# B -
# def rec(n, m, i):
#     if n > m:
#         return 1e10
#     elif m == n:
#         return i
#     return min(rec(n * 2, m, i + 1), rec(n * 3, m, i + 1))


# n, m = map(int, input().split())
# if n > m:
#     print(-1)
# elif n == m:
#     print(0)
# else:
#     ans = rec(n, m, 0)
#     if ans == 1e10:
#         print(-1)
#     else:
#         print(ans)

# C -
# s = input()
# lens = len(s)
# offset = 0
# for i in range(1, lens):
#     offset += 2**i

# s = s.replace('4', '0')
# s = s.replace('7', '1')
# b = int(s, 2)
# print(offset + b + 1)

# D -
# from bisect import bisect_left
# lucky = []
# limit = 10


# def create_lucky(acc):
#     global lucky, limit
#     if len(acc) > limit:
#         return
#     left_lucky = acc + '4'
#     right_lucky = acc + '7'
#     lucky.append(left_lucky)
#     lucky.append(right_lucky)
#     create_lucky(left_lucky)
#     create_lucky(right_lucky)


# create_lucky('')
# lucky = list(sorted(map(int, lucky)))
# l, r = map(int, input().split())
# i = bisect_left(lucky, l)
# num = lucky[i]
# total = 0
# for x in range(l, r + 1):
#     if x > num:
#         i += 1
#         num = lucky[i]
#     total += num

# print(total)

# E -
# n = int(input())
# xs = input()
# ks, ls = ''.join(sorted(xs[:n])), ''.join(sorted(xs[n:]))
# print("YES" if all([k < l for k, l in zip(ks, ls)])
#       or all([k > l for k, l in zip(ks, ls)]) else "NO")

# F -
# def fun(total, xs, n):
#     if total == n:
#         return True
#     if (len(xs) == 0 or total > n):
#         return False

#     return fun(total + xs[0], xs[1:], n) or fun(total, xs[1:], n)


# for _ in range(int(input())):
#     n = int(input())
#     input()
#     xs = list(map(int, input().split()))
#     print("YES" if fun(0, xs, n) else "NO")

# G -
# import sys
# lines = sys.stdin.readlines()


# def music(total, acc, songs, limit):
#     if total > limit:
#         return (-1, [])

#     if len(songs) == 0 or total == limit:
#         return (total, acc)

#     left = music(total, acc, songs[1:], limit)
#     right = music(total + songs[0], acc + [songs[0]], songs[1:], limit)

#     return max(left, right)


# for line in lines:
#     parse = list(map(int, line.split()))
#     limit = parse[0]
#     n = parse[1]
#     songs = parse[2:]
#     best_music = music(0, [], songs, limit)
#     for track in best_music[1]:
#         print(track, end=" ")
#     print(f"sum:{best_music[0]}")

# H -
# import sys


# def si(total, acc, rest, limit, the_bank):
#     if total == limit:
#         the_bank.add(tuple(sorted(acc, reverse=True)))
#     elif total > limit or len(rest) == 0:
#         pass
#     else:
#         si(total, acc, rest[1:], limit, the_bank)
#         si(total + rest[0], acc + rest[:1], rest[1:], limit, the_bank)
#     return the_bank


# lines = sys.stdin.readlines()
# for line in lines[:-1]:
#     nums = list(map(int, line.split()))
#     limit = nums[0]
#     n = nums[1]
#     xs = list(sorted(nums[2:]))
#     sols = si(0, [], xs, limit, set())
#     print(f"Sums of {limit}:")
#     if len(sols) > 0:
#         for sol in sorted(list(sols), reverse=True):
#             ans = '+'.join(map(str, sol))
#             print(ans)
#     else:
#         print("NONE")

# I -
# def score(seq, quads):
#     total = 0
#     for quad in quads:
#         if seq[quad[1]] - seq[quad[0]] == quad[2]:
#             total += quad[3]

#     return total


# def rec(total, acc, moves_left, limit, quads):
#     if moves_left == 0:
#         return score(acc, quads)

#     best = total
#     start = 1 if len(acc) == 0 else acc[-1]

#     for i in range(start, limit + 1):
#         best = max(best, rec(best, acc + [i], moves_left - 1, limit, quads))

#     return best


# n, m, q = map(int, input().split())
# quads = []
# for _ in range(q):
#     a, b, c, d = map(int, input().split())
#     quads.append((a - 1, b - 1, c, d))

# print(rec(0, [], n, m, quads))

# J -
# import sys
# from itertools import permutations


# def good_board(rows):
#     for i in range(len(rows)):
#         pos = (i, rows[i])
#         for j in range(i + 1, len(rows)):
#             other = (j, rows[j])
#             if pos[1] == other[1]:
#                 return False
#             if abs(pos[0] - other[0]) == abs(pos[1] - other[1]):
#                 return False

#     return True


# all_queens = []

# for comb in permutations(range(1, 9)):
#     if good_board(comb):
#         all_queens.append(comb)


# def score(rows):
#     global all_queens
#     best = 7
#     for queens in all_queens:
#         diff = map(lambda d: 1 if d[0] != d[1] else 0, zip(rows, queens))
#         best = min(best, sum(diff))
#     return best


# lines = sys.stdin.readlines()
# for i, line in enumerate(lines, start=1):
#     rows = list(map(int, line.split()))
#     print(f"Case {i}: {score(rows)}")

# K -
# import sys
# primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

# anses = dict()


# def permute(acc: list, have: set, n, last_even):
#     start = 3 if last_even else 2
#     if len(acc) == n:
#         if 1 + acc[-1] in primes:
#             sys.stdout.write(' '.join(map(str, acc)) + "\n")
#     for i in range(start, n + 1, 2):
#         if i in have:
#             continue
#         if acc[-1] + i not in primes:
#             continue
#         acc.append(i)
#         have.add(i)
#         permute(acc, have, n, not last_even)
#         have.remove(i)
#         acc.pop()


# lines = sys.stdin.readlines()

# for i, line in enumerate(lines, start=1):
#     if i > 1:
#         sys.stdout.write("\n")
#     n = int(line)
#     sys.stdout.write(f"Case {i}:\n")
#     permute([1], {1}, n, False)

# L -
# import sys


# def gen(acc, words, rule, bank):
#     if rule == '':
#         bank.append(acc)
#         return bank
#     op = rule[0]
#     if op == '#':
#         for word in words:
#             gen(acc + word, words, rule[1:], bank)
#     else:
#         for i in range(0, 10):
#             gen(acc + f"{i}", words, rule[1:], bank)
#     return bank


# lines = sys.stdin.readlines()

# offset = 0
# while offset < len(lines):
#     sys.stdout.write("--\n")
#     n = int(lines[offset])
#     offset += 1
#     words = []
#     for _ in range(n):
#         words.append(lines[offset][:-1])
#         offset += 1
#     rules = []
#     m = int(lines[offset])
#     offset += 1
#     for _ in range(m):
#         rules.append(lines[offset][:-1])
#         offset += 1
#     bank = []
#     for rule in rules:
#         gen('', words, rule, bank)
#     for password in bank:
#         sys.stdout.write(password + "\n")
