# A -
n, m = map(int, input().split())
mat = []
right = True
weeds = []

for _ in range(n):
    line = input()
    mat.append(line)

for i in range(n-1):
    if right:
        weeds.append(max(mat[i].rindex('W'), mat[i+1].rindex('W')))
    else:
        weeds.append(max(mat[i].index('W'), mat[i+1].index('W')))
    right = not right

total = m - 1
curr=0
for i in range(len(weeds)):
    if weeds[i] != -1:
        total += abs(curr - weeds[i])
        curr = weeds[i]
    right = not right
print(total)

# B
# n = int(input())
# arr = list(map(int, input().split()))
# prev = arr.index(min(arr))
# smallest = arr[prev]
# smallest_distance = n-1
# for i in range(prev + 1, n):
#     if arr[i] == smallest:
#         smallest_distance = min(smallest_distance, i - prev)
#         prev = i
# print(smallest_distance)

# C -
# from collections import defaultdict, deque

# n, m = map(int, input().split())
# adj = defaultdict(set)
# vis = [False] * (n)
# total_vis = 0
# good = True
# for _ in range(m):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[a].add(b)
#     adj[b].add(a)

# while total_vis != n - 1:
#     q = deque()
#     next_to_vis = 0
#     for i in range(n):
#         if not vis[i]:
#             next_to_vis = i
#             break
#     q.appendleft(next_to_vis)
#     while q:
#         u = q.pop()
#         vis[u] = True
#         total += 1


# print("YES" if good else "NO")


# D -
# import sys
# lines = sys.stdin.readlines()


# for line in lines:
#     line = line.strip()
#     n = len(line)
#     ans = set()
#     for i in range(n):
#         for j in range(i+1, n+1):
#             # print("n:"+ line[i:j] + ",rn:"+ line[i:j][::-1])
#             if line[i:j] == line[i:j][::-1]:
#                 ans.add(line[i:j])
#     print("The string '{}' contains {} palindromes.".format(line, len(ans)))


# E -
# from bisect import bisect_right
# n, m = map(int, input().split())
# cities = list(map(int, input().split()))
# towers = list(map(int, input().split()))

# ind = []
# for city in cities:
#     tower_i = bisect_right(towers, city)

#     if tower_i == m:
#         ind.append(city - towers[tower_i - 1])
#         continue
#
#
#     min_dist = min(abs(city - towers[tower_i]), abs(city - towers[tower_i - 1]))
#     ind.append(min_dist)


# print(max(ind))
