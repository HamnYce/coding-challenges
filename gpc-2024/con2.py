# A -
# print(1, input())

# B -
# n, m = map(int, input().split())
# d = dict()

# for _ in range(n):
#     name, ip = input().split()
#     d[ip + ';'] = name

# for _ in range(m):
#     op, ip = input().split()
#     print(f"{op} {ip} #{d[ip]}")

# C -
# n, m = map(int, input().split())
# xs = [0] * (n + 1)
# for _ in range(m):
#     a, b = map(int, input().split())
#     for i in range(a, b + 1):
#         xs[i] += 1
# mini = 10000
# mini_index = -1
# for i, x in enumerate(xs):
#     if i == 0:
#         continue
#     if x == 0 or x > 1:
#         mini = x
#         mini_index = i
#         break

# print("OK" if mini_index == -1 else f"{mini_index} {mini}")


# D -
# t = int(input())
# for _ in range(t):
#     n, s = map(int, input().split())
#     if n == 1:
#         print(s)
#     elif n == 2:
#         print(s // 2)
#     else:
#         print(s // (n // 2 + 1))

# E -
# n = int(input())
# biggest_diff = 0
# have = dict(zip(map(int, input().split()), range(n)))
# want = dict(zip(map(int, input().split()), range(n)))
# for k in have:
#     if want[k] > have[k]:
#         biggest_diff = max(biggest_diff, want[k] - have[k])
# print(biggest_diff)
