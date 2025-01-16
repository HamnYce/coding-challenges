# A -
# t = int(input())


# def win(coin_i, taken, total, smallest, coins, n, s):
#     if total >= s:
#         if total - smallest >= s:
#             return -1
#         return taken

#     if coin_i >= n:
#         return -1

#     take = win(coin_i + 1, taken + 1, total +
#                coins[coin_i], coins[coin_i], coins, n, s)
#     leave = win(coin_i + 1, taken, total, smallest, coins, n, s)

#     return max(take, leave)


# for _ in range(t):
#     n, s = map(int, input().split())
#     coins = list(sorted(map(int, input().split()), reverse=True))
#     print(win(0, 0, 0, 0, coins, n, s))


# B -
# import sys

# t = int(sys.stdin.readline())

# for _ in range(t):
#     n, k = map(int, sys.stdin.readline().split())
#     if (n % 2) == (k % 2):
#         if n >= k*k:
#             print("YES")
#         else:
#             print("NO")
#     else:
#         print("NO")

# C -
# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     adj = dict()
#     not_taken = set(range(1, n + 1))
#     not_married = set(range(1, n + 1))
#     for i in range(1, n +1):
#         adj[i] = list(map(int, input().split()[1:]))

#     for princess in adj:
#         for kingdom in adj[princess]:
#             if kingdom in not_taken:
#                 not_taken.remove(kingdom)
#                 not_married.remove(princess)
#                 break
#     if len(not_married) and len(not_taken):
#         princess = not_married.pop()
#         kingdom = not_taken.pop()
#         print(f"IMPROVE\n{princess} {kingdom}")
#     else:
#         print("OPTIMAL")


# D -
# from math import ceil
# import sys
# lines = sys.stdin.readlines()


# def win(n, l):
#     if n <= l:
#         return 1
#     if n > l:
#         return win(n // 2, l) + win(ceil(n/2), l)


# for line in lines:
#     a, b = map(int, line.split())
#     print(win(a, b))

# E -
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     xs = map(int, input().split())
#     even = 0
#     odd = 0
#     for x in xs:
#         if x % 2 == 0:
#             even += x
#         else:
#             odd += x
#     print('YES' if even > odd else 'NO')
