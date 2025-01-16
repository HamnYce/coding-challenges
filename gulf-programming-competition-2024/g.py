# A -
# t = int(input())

# for _ in range(t):
#     a, b = map(int, input().split())
#     print((a ^ a) + (b ^ a))

# B -
# print(bin(int(input())).count('1'))

# C -
# from itertools import combinations
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     p = int(input())
#     ps = list(map(int, input().split()))
#     possible = False

#     for i in range(0, p + 1):
#         for comb in combinations(ps, i):
#             if sum(comb) == n:
#                 possible = True
#                 break
#         if possible:
#             break
#     print("YES" if possible else "NO")

# D -
# from itertools import combinations
# n, l, r, x = map(int, input().split())
# ks = list(map(int, input().split()))
# total = 0

# for i in range(2, n + 1):
#     for comb in combinations(ks, i):
#         sumi = sum(comb)
#         diff = max(comb) - min(comb)
#         if diff >= x and r >= sumi >= l:
#             total += 1

# print(total)

# E -

# from itertools import permutations
# from math import ceil

# n = input()
# int_n = int(n)
# done = False
# for i in range(len(n), len(n) + 3):
#     for comb in permutations(('4' * ceil(i / 2)) + ('7' * ceil(i / 2))):
#         comb = ''.join(comb)
#         if int(comb) >= int_n and comb.count('4') == comb.count('7'):
#             print(comb)
#             done = True
#             break
#     if done:
#         break

# F -
# total = 0
# correct = 0


# s = input()
# t = input()

# stotal = sum(map(lambda c: -1 if c == '-' else 1, s))


# def foo(i, acc):
#     global total, correct, t, stotal
#     if i == len(s):
#         total += 1
#         if stotal == acc:
#             correct += 1
#         return

#     if t[i] in '-?':
#         foo(i + 1, acc - 1)

#     if t[i] in '+?':
#         foo(i + 1, acc + 1)


# foo(0, 0)
# print(correct / total)

# G -
# n = int(input())
# for _ in range(n):
#     low, high = map(int, input().split())
#     l_bin, h_bin = map(lambda v: bin(v)[2:], [low, high])
#     len_bin = len(h_bin)
#     ans = l_bin.rjust(len_bin, '0')
#     while True:
#         if '0' not in ans:
#             break
#         temp_ans = ans[:ans.rindex('0')] + '1' + ans[ans.rindex('0') + 1:]
#         if int(temp_ans, 2) <= high:
#             ans = temp_ans
#         else:
#             break
#     print(int(ans, 2))

# H -
# s = input()

# total = 0

# def foo(acc: str, rest: str):
#     global total

#     if len(rest) == 0:
#         total += eval(acc)
#         return

#     if len(acc) and acc[-1] != '+':
#         foo(acc + '+' + rest[0], rest[1:])
#     foo(acc + rest[0], rest[1:])

# foo('', s)
# print(total)

# I -
# from functools import reduce

# n = int(input())
# cs = list(map(int, input().split()))

# key = reduce(lambda e, acc: e ^ acc, cs)

# for c in cs:
#     print(c ^ key, end=" ")

# J -
# n = int(input())
# xs = list(map(int, input().split()))

# def m(acc, xs):
#     if len(xs) == 0:
#         return len(acc)

#     max1 = m(acc, xs[1:])

#     max2 = 0

#     if len(acc) == 0 or acc[-1] < xs[0]:
#         max2 = m(acc + [xs[0]], xs[1:])

#     return max(max1, max2)

# print(m([], xs))

# B -
# l = int(input())
# r = int(input())

# x = 0
# for i in range(l, r + 1):
#     for j in range(l, r + 1):
#         x = max(x, i ^ j)

# print(x)

# C -
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     binn = bin(n)[2:]
#     if binn.count('1') == 1:
#         print("-1")
#     else:
#         p = binn[::-1].index('1')
#         a = 2**p
#         b = a ^ n
#         print(f"{a} {b}")

# D -
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     binn = bin(n)[2:].rjust(32, '0')
#     flipped_binn = list(map(lambda c: '0' if c == '1' else '1', binn))
#     str_flipped_binn = ''.join(flipped_binn)
#     print(int(str_flipped_binn, 2))

# E -
# n = int(input())
# if n == 0:
#     print(1)
# else:
#     print(2**(bin(n)[2:].count('0')))

# F -

# from math import log2
# import sys
# lines = sys.stdin.readlines()
# for line in lines[1:]:
#     x = int(line)
#     print((2**(int(log2(x) + 1)) - 1) ^ x)


# Q -
# TODO: try out this solution
# NOTE: we want to accumulate the biggest number possible without decreasing the most possible
# import sys
# lines = sys.stdin.readlines()

# xs = [int(line) for line in lines[1].split()]
# d = [0] * 21


# for x in xs:
#     b = bin(x)[2:].rjust(21, '0')

#     for i, bit in enumerate(b):
#         if bit == '1':
#             d[i] += 1


# d.reverse()
# total = 0
# for _ in xs:
#     b = 0
#     for i, number_of_active_bits in enumerate(d):
#         if number_of_active_bits:
#             b += 1 << i
#             if number_of_active_bits:
#                 d[i] -= 1

#     total += b * b
# print(total)
