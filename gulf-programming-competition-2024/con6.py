# A -
# print('All in!')


# B -
# n, k = map(int, input().split())

# factors = set()
# for i in range(1, int(n**.5) + 10):
#     if n % i == 0:
#         factors.add(i)
#         factors.add(n // i)

# factors = list(sorted(factors))
# if k > len(factors):
#     print('-1')
# else:
#     print(factors[k - 1])

# C -
import sys
lines = sys.stdin.readlines()
for i in range(1, len(lines[1:]), 2):
    n = int(lines[i])
    frogs = filter(lambda x: x <= n, map(int, lines[i + 1].split()))
    leap_sizes = dict()
    for frog in frogs:
        if frog not in leap_sizes:
            leap_sizes[frog] = 0
        leap_sizes[frog] += 1

    visited = [0] * (n + 1)
    for leap_size, num_of_frogs in leap_sizes.items():
        for i in range(0, n + 1, leap_size):
            visited[i] += num_of_frogs

    best = 0
    for i in range(1, n + 1):
        if visited[i] > best:
            best = visited[i]
    print(best)

# D -
# import sys
# from collections import Counter
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     xs = list(map(int, sys.stdin.readline().split()))
#     # test for number uniqueness
#     d = Counter(xs)
#     counts = Counter(d.values())
#     uniqueness = counts.most_common(1)[0][1] == 1


#     # test for contiguous numbers
#     stack = [xs[0]]
#     for x in xs[1:]:
#         if stack[-1] != x:
#             stack.append(x)

#     contiguousness = True
#     have = set()
#     for x in stack:
#         if x in have:
#             contiguousness = False
#             break
#         have.add(x)

#     print("YES" if uniqueness and contiguousness else "NO")

# E -
# n, h = map(int, input().split())
# xs = list(reversed(list(map(int, input().split()))))

# while len(xs):
#     if h < xs[-1]:
#         break
#     h += xs[-1]
#     xs.pop()

# if len(xs):
#     print("NAO")
# else:
#     print("SIM")
