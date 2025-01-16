# A -
# output_statement = "Hey stupid robber, you can get {}."


# def dp(i, capacity_left,  total_value, n, memo):
#     if i == n or capacity_left == 0:
#         return total_value
#     if (i, capacity_left) in memo:
#         return memo[(i, capacity_left)]
#     take = dp(i + 1, capacity_left -
#               items[i][0], total_value + items[i][1], n, memo) if capacity_left >= items[i][0] else 0
#     leave = dp(i+1, capacity_left, total_value,  n, memo)
#     memo[(i, capacity_left)] = max(take, leave)
#     return memo[(i, capacity_left)]


# t = int(input())


# for _ in range(t):
#     k, n = map(int, input().split())
#     items = []
#     for _ in range(n):
#         items.append(tuple(map(int, input().split())))
#     print(output_statement.format(dp(0, k, 0, n, dict())))

# C -

# n = int(input())
# items = list(map(int, input().split()))
# memo = dict()


# def dp(i, last_number):
#     global items
#     if i == -1:
#         return 0
#     if (i, last_number) in memo:
#         return memo[(i, last_number)]

#     take = 0
#     if last_number > items[i]:
#         take = 1 + dp(i - 1, items[i])

#     leave = dp(i - 1, last_number)
#     best = max(take, leave)
#     memo[(i, last_number)] = best
#     return best


# print(dp(n - 1, 21))

# D -
# import sys
# sys.setrecursionlimit(5000)


# def dp(i, j, s, t, memo):
#     if i == -1 or j == -1:
#         return 0
#     if (i, j) in memo:
#         return memo[(i, j)]
#     if s[i] == t[j]:
#         memo[(i, j)] = 1 + dp(i - 1, j - 1, s, t, memo)
#     else:
#         memo[(i, j)] = max(dp(i - 1, j, s, t, memo), dp(i, j - 1, s, t, memo))
#     return memo[(i, j)]


# lines = iter(sys.stdin.readlines())
# while True:
#     s = next(lines, None)
#     t = next(lines, None)
#     if s is None or t is None:
#         break
#     sys.stdout.write("{}\n".format(dp(len(s)-1, len(t)-1, s, t, dict()) - 1))

# E -
# def dp(i, coins, memo):
#     if i < 0:
#         return 0
#     if memo[i] != -1:
#         return memo[i]

#     take = coins[i] + dp(i - 2, coins, memo)
#     leave = dp(i - 1, coins, memo)

#     memo[i] = max(take, leave)
#     return memo[i]


# t = int(input())
# for case in range(1, t+1):
#     n = int(input())
#     coins = list(map(int, input().split()))
#     print(f"Case {case}: {dp(n - 1, coins, [-1] * (n))}")

# F -
# import sys
# sys.setrecursionlimit(5000)
# memo = dict()
# coins = [1, 5, 10, 25, 50]
# one_way = "There is only 1 way to produce {} cents change.\n"
# more_than_one_way = "there are {} ways to produce {} cents change.\n"
# lines = sys.stdin.readlines()


# def dp(i, rem):
#     global coins, memo
#     if rem == 0:
#         return 1
#     if i == -1 or rem < 0:
#         return 0
#     if (i, rem) in memo:
#         return memo[(i, rem)]
#     take = 0
#     if rem >= coins[i]:
#         take = dp(i, rem - coins[i])
#     leave = dp(i - 1, rem)
#     memo[(i, rem)] = take+leave
#     return memo[(i, rem)]


# for line in lines:
#     n = int(line)
#     m = dp(4, n)
#     if m == 1:
#         sys.stdout.write(one_way.format(n))
#     else:
#         sys.stdout.write(more_than_one_way.format(m, n))

# with open('output.txt', 'w') as f:
#      f.write(str([dp(4, i) for i in range(30_001)]))


# x = []
# for line in sys.stdin.readlines():
#     n = int(line)
#     if x[n] == 1:
#         sys.stdout.write("There is only 1 way to produce {} cents change.\n".format(n))
#     else:
#         sys.stdout.write("there are {} ways to produce {} cents change.\n".format(x[n], n))

# G -
# b, l, n = 1, 1, 1
# while b or l or n:
#     b, l, n = map(int, input().split())
#     cars = []
#     for _ in range(n):
#         weight, speed = map(int, input().split())
#         time = l / speed * 60
#         cars.append()

# H - not possible with top-down it seems
# import sys
# sys.setrecursionlimit(5000)
# s, t = '', ''
# memo = [[-1] * 2000 for _ in range(2000)]


# def dp(i, j):
#     global s, t, memo
#     if i < 0 and j < 0:
#         return 0
#     if i < 0 or j < 0:
#         return max(i, j) + 1
#     if memo[i][j] == -1:
#         insert_s = 1+dp(i, j - 1)
#         delete_s = 1+dp(i - 1, j)
#         replace = (1 if s[i] != t[j] else 0) + dp(i-1, j-1)
#         memo[i][j] = min(insert_s, delete_s, replace)
#     return memo[i][j]


# for _ in range(int(sys.stdin.readline())):
#     s, t = sys.stdin.readline().strip(), sys.stdin.readline().strip()
#     for i in range(len(s)):
#         for j in range(len(t)):
#             memo[i][j] = -1
#     print(dp(len(s)-1, len(t)-1))

# L -
# import sys
# sys.setrecursionlimit(5000)
# n, k = map(int, input().split())
# memo = [[0] * (k + 1) for _ in range(n + 1)]

# def dp(i, n, k):
#     global memo
#     if k == 1:
#         return 1
#     if memo[i][k]:
#         return memo[i][k]
#     total = sum([dp(j, n, k - 1) for j in range(i, n+1, i)])
#     memo[i][k] = total
#     return total


# print(sum([dp(i, n, k) for i in range(1, n + 1)]) % 1_000_000_007)

# M -
# def dp(acc, contains_d, n, k, d, memo):
#     if acc > n:
#         return 0
#     if memo[acc][1 if contains_d else 0] != -1:
#         return memo[acc][1 if contains_d else 0]

#     total = sum([dp(acc+i, contains_d or i >= d, n, k, d, memo)
#                 for i in range(1, k+1)])
#     memo[acc][1 if contains_d else 0] = total
#     return total


# n, k, d = map(int, input().split())
# memo = [[-1, -1] for _ in range(n+1)]
# memo[n][1] = 1
# memo[n][0] = 0
# print(sum([dp(i, i >= d, n, k, d, memo) for i in range(1, k+1)]) % 1_000_000_007)

# O -
# import sys
# sys.setrecursionlimit(1000000)
# memo = [-1]*(10**5+1)
# t, k = map(int, input().split())


# def dp(rem_flowers):
#     if rem_flowers < 0:
#         return 0
#     if memo[rem_flowers] != -1:
#         return memo[rem_flowers]
#     white = dp(rem_flowers - k) % (10**9+7)
#     red = dp(rem_flowers - 1) % (10**9+7)
#     memo[rem_flowers] = (white+red) % (10**9+7)
#     return memo[rem_flowers]


# memo[0] = 1
# dp(10**5)
# memo[0] = 0
# for i in range(1, 10**5+1):
#     memo[i] += memo[i-1]
# for _ in range(t):
#     a, b = map(int, input().split())
#     print((memo[b]-memo[a - 1]) % (10**9+7))

# P -
import sys
sys.setrecursionlimit(5000)
s = ''
memo = []


def dp(i, j):
    global s, memo
    if i > j:
        return ''
    if i == j:
        return s[i]

    if memo[i][j]:
        return memo[i][j]

    if (s[i] == s[j]):
        memo[i][j] = ''.join([s[i], dp(i+1, j-1), s[j]])
    else:
        insert_left = ''.join([s[j], dp(i, j-1), s[j]])
        insert_right = ''.join([s[i], dp(i+1, j), s[i]])

        if len(insert_left) < len(insert_right):
            memo[i][j] = insert_left
        else:
            memo[i][j] = insert_right
    return memo[i][j]


lines = sys.stdin.readlines()
for line in lines:
    s = line.strip()
    memo = [[None]*len(s) for _ in range(len(s))]
    t = dp(0, len(s)-1)
    print(len(t) - len(s), t)
