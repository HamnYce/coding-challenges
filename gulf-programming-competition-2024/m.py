# A -
# import sys
# from queue import Queue


# def is_valid(x, y, n, m):
#     return x >= 0 and x < n and y >= 0 and y < m


# def bfs(qu, n, m, ans, vis):
#     while qu.qsize():
#         i, j = qu.get()

#         for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             ni, nj = i + di, j + dj
#             if is_valid(ni, nj, n, m) and not vis[ni][nj]:
#                 vis[ni][nj] = True
#                 qu.put((ni, nj))
#                 ans[ni][nj] = ans[i][j] + 1


# t = int(sys.stdin.readline())

# for abcd in range(t):
#     if abcd:
#         sys.stdin.readline()
#     n, m = map(int, sys.stdin.readline().split())
#     mat = []
#     for _ in range(n):
#         mat.append(sys.stdin.readline().strip())
#     ans = [[0] * m for _ in range(n)]
#     qu = Queue()
#     vis = [[False] * m for _ in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if mat[i][j] == '1':
#                 qu.put((i, j))
#                 vis[i][j] = True

#     bfs(qu, n, m, ans, vis)

#     for i in range(n):
#         for j in range(m):
#             sys.stdout.write(f"{ans[i][j]} ")
#         sys.stdout.write("\n")

# B -
# from queue import Queue
# from collections import defaultdict
# BIG_BOY_N = 32768
# adj = defaultdict(list)
# for i in range(BIG_BOY_N):
#     adj[(i+1) % BIG_BOY_N].append(i)
#     adj[(i*2) % BIG_BOY_N].append(i)

# dist = [0] * BIG_BOY_N
# q = Queue()
# q.put((0,0))
# vis = set([0])
# while q.qsize():
#     x, d = q.get()
#     dist[x] = d
#     for next_node in adj[x]:
#         if next_node in vis:
#             continue
#         q.put((next_node, d + 1))
#         vis.add(next_node)

# input()
# [print(dist[int(i)], end=" ") for i in input().split()]

# C -
# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# n, m = 1, 1
# while n or m:
#     n, m = map(int, input().split())
#     indegrees = [0] * n
#     adj = defaultdict(list)
#     for _ in range(m):
#         a, b = map(int, input().split())
#         a -= 1
#         b -= 1
#         adj[a].append(b)
#         indegrees[b] += 1

#     answer = []
#     stack = [i for i in range(n) if indegrees[i] == 0]

#     while stack:
#         top_stick = stack[-1]
#         stack.pop()
#         answer.append(top_stick)
#         for next_stick in adj[top_stick]:
#             indegrees[next_stick] -= 1
#             if indegrees[next_stick] == 0:
#                 stack.append(next_stick)
#     if len(answer) == n:
#         print('\n'.join(map(lambda x: str(x + 1), answer)))
#     else:
#         print('IMPOSSIBLE')

# D -
# from queue import Queue
# import sys


# def is_valid(x, y):
#     return x >= 0 and x < 8 and y >= 0 and y < 8


# trans = dict(zip('abcdefgh', range(8)))
# trans.update(dict(zip('12345678', range(8))))
# lines = sys.stdin.readlines()

# deltas = (
#     (-1, -2),
#     (-1, 2),
#     (1, -2),
#     (1, 2),
#     (-2, -1),
#     (-2, 1),
#     (2, -1),
#     (2, 1)
# )

# for line in lines:
#     sorc, dest = line.split()
#     x1, y1 = map(lambda c: trans[c], sorc)
#     x2, y2 = map(lambda c: trans[c], dest)
#     vis = set()
#     q = Queue()
#     q.put((x1, y1, 0))
#     vis.add((x1, y1))
#     dist = 1
#     while q.qsize():
#         x, y, dist = q.get()
#         if x == x2 and y == y2:
#             break
#         for dx, dy in deltas:
#             nx = x + dx
#             ny = y + dy
#             if is_valid(nx, ny) and (nx, ny) not in vis:
#                 vis.add((nx, ny))
#                 q.put((nx, ny, dist + 1))
#     print(f"To get from {sorc} to {dest} takes {dist} knight moves.")

# E -
# from queue import Queue
# n, m = map(int, input().split())

# vis = set()
# dist = 0

# q = Queue()
# q.put((n, 0))
# mini = 10000
# while q.qsize():
#     x, dist = q.get()
#     nx1, nx2 = x - 1, x*2
#     if x == m:
#         mini = min(dist, mini)
#     if nx1 > 0 and nx1 not in vis:
#         vis.add(nx1)
#         q.put((nx1, dist + 1))
#     if x < m and nx2 not in vis:
#         vis.add(nx2)
#         q.put((nx2, dist + 1))
# print(mini)

# F -
# DID IT IN CPP
# from queue import Queue
# input = open('input.txt').readline
# print = open('output.txt', 'w').write

# n, m = map(int, input().split())
# k = int(input())
# trees = list(map(lambda tree_coord: int(tree_coord) - 1, input().split()))

# deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

# q = Queue()
# vis = [[False] * m for _ in range(n)]
# for i in range(0, k*2, 2):
#     q.put((trees[i], trees[i + 1], 0))
#     vis[trees[i]][trees[i + 1]] = True


# farthest_node = (0, 0)
# farthest_dist = 0
# while q.qsize():
#     x, y, dist = q.get()
#     if dist > farthest_dist:
#         farthest_dist = dist
#         farthest_node = (x, y)
#     for dx, dy in deltas:
#         nx, ny = x+dx, y+dy
#         if nx >= 0 and nx < n and ny >= 0 and ny < m and not vis[nx][ny]:
#             vis[nx][ny] = True
#             q.put((nx, ny, dist + 1))
# print(f"{farthest_node[0] + 1} {farthest_node[1] + 1}")

# G -
# from collections import defaultdict
# from queue import Queue


# n, m = map(int, input().split())
# vis = [False] * n
# adj = defaultdict(list)
# for _ in range(m):
#     a, b = map(int, input().split())
#     adj[a - 1].append(b - 1)
#     adj[b - 1].append(a - 1)

# q = Queue()
# q.put(0)
# vis[0] = True
# while q.qsize():
#     u = q.get()

#     for v in adj[u]:
#         if vis[v]:
#             continue
#         vis[v] = True
#         q.put(v)
# print("FHTAGN!" if n==m and all(vis) else "NO")


# H -
# from queue import Queue
# import sys


# deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]


# def solve(mat, n, m):
#     global deltas

#     vis = [[False] * m for _ in range(m)]
#     best = 0
#     for i in range(n):
#         for j in range(m):
#             if vis[i][j] or mat[i][j] == '0':
#                 continue
#             vis[i][j] = True
#             q = Queue()
#             q.put((i, j))
#             count = 0
#             while q.qsize():
#                 x, y = q.get()
#                 count += 1
#                 for dx, dy in deltas:
#                     nx, ny = x + dx, y + dy
#                     if (nx >= 0 and nx < n and ny >= 0 and ny < m
#                         and mat[nx][ny] == '1'
#                             and not vis[nx][ny]):
#                         q.put((nx, ny))
#                         vis[nx][ny] = True
#             best = max(best, count)

#     return best


# lines = sys.stdin.readlines()
# lines.append('\n')

# mat = []
# i = 0
# for line in lines[2:]:
#     if line == '\n':
#         if i:
#             print()
#         i += 1
#         n, m = len(mat), len(mat[0]) - 1
#         print(solve(mat, n, m))
#         mat.clear()
#     else:
#         mat.append(line)

# I -
# import sys
# from queue import Queue
# input = sys.stdin.readline
# x0, y0, x1, y1 = map(int, input().split())
# deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
# n = int(input())

# allowed = set()

# for _ in range(n):
#     r, a, b = map(int, input().split())
#     for i in range(a, b+1):
#         allowed.add((r, i))

# q = Queue()
# q.put((x0, y0, 0))
# vis = set()
# vis.add((x0, y0))
# best_d = -1
# while q.qsize():
#     x, y, d = q.get()

#     if x == x1 and y == y1:
#         best_d = d
#         break

#     for dx, dy in deltas:
#         nx, ny = x + dx, y + dy
#         if (nx > 0 and nx <= 1e9 and ny > 0 and ny <= 1e9
#             and (nx, ny) not in vis
#                 and (nx, ny) in allowed):
#             vis.add((nx, ny))
#             q.put((nx, ny, d+1))
# print(best_d)

# J -
# from collections import defaultdict
# from queue import Queue
# n, m = map(int, input().split())
# adj = defaultdict(list)
# for _ in range(m):
#     a, b = map(int, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# q = Queue()
# vis = [False] * (n + 1)
# q.put((1, 0))
# vis[1] = True
# u, d = 1, 0
# while q.qsize():
#     u, d = q.get()
#     for v in adj[u]:
#         if vis[v]:
#             continue
#         vis[v] = True
#         q.put((v, d + 1))

# vis = [False] * (n + 1)
# q.put((u, 0))
# vis[u] = True
# d = 0
# q.put((u, d))
# while q.qsize():
#     u, d = q.get()
#     for v in adj[u]:
#         if vis[v]:
#             continue
#         vis[v] = True
#         q.put((v, d + 1))

# print(d)

# K -
# from collections import defaultdict
# from queue import Queue
# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     adj = defaultdict(list)
#     for _ in range(m):
#         a, b = map(int, input().split())
#         adj[a - 1].append(b - 1)
#         adj[b - 1].append(a - 1)
#     s = int(input()) - 1
#     dists = [0] * n
#     q = Queue()
#     q.put((s, 0))
#     vis = [False] * n
#     vis[s] = True
#     while q.qsize():
#         u, d = q.get()
#         dists[u] = d
#         for v in adj[u]:
#             if vis[v]:
#                 continue
#             vis[v] = True
#             q.put((v, d + 6))
#     for i in range(n):
#         if i == s:
#             continue

#         print(dists[i] if vis[i] else -1, end=" ")
#     print()

# L -
# from queue import Queue
# n, m, k = map(int, input().split())
# mat = [list(input()) for _ in range(n)]
# deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]


# q = Queue()
# vis = [[False]*m for _ in range(n)]
# start = -1, -1
# for i in range(n):
#     for j in range(m):
#         if mat[i][j] == '.':
#             start = i, j


# q.put(start)
# vis[start[0]][start[1]] = True
# stack = [start]

# while q.qsize():
#     x, y = q.get()

#     for dx, dy in deltas:
#         nx, ny = x+dx, y+dy

#         if (nx >= 0 and nx < n and ny >= 0 and ny < m and mat[nx][ny] == '.' and not vis[nx][ny]):
#             vis[nx][ny] = True
#             q.put((nx, ny))
#             stack.append((nx, ny))

# while k:
#     x, y = stack[-1]
#     stack.pop()
#     mat[x][y] = 'X'
#     k -= 1

# for line in mat:
#     print(''.join(line))

# M -
# from collections import defaultdict
# from queue import Queue


# n = int(input())
# adj = defaultdict(list)
# u = 1
# vis = [False] * n
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[a].append(b)
#     adj[b].append(a)

# q = Queue()
# q.put((u, 0))
# vis[u] = True

# while q.qsize():
#     u, d = q.get()
#     for v in adj[u]:
#         if vis[v]:
#             continue
#         vis[v] = True
#         q.put((v, d + 1))

# vis = [False]*n
# q.put((u, 0))
# vis[u] = True
# while q.qsize():
#     u, d = q.get()
#     for v in adj[u]:
#         if vis[v]:
#             continue
#         vis[v] = True
#         q.put((v, d + 1))
# print(d)

# N -
# from queue import Queue


# n, p = map(int, input().split())
# adj = dict()
# indegrees = [0] * n
# outdegrees = [0] * n
# tanks = list()
# q = Queue()

# for _ in range(p):
#     a, b, d = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[a] = (b, d)
#     outdegrees[a] += 1
#     indegrees[b] += 1

# for i in range(n):
#     if outdegrees[i] == 1 and indegrees[i] == 0:
#         tanks.append(i)


# for tank in tanks:
#     q.put((tank, adj[tank][0], adj[tank][1]))

# ans = []
# while q.qsize():
#     tank, house, diam = q.get()

#     if house in adj:
#         q.put((tank, adj[house][0], min(adj[house][1], diam)))
#     else:
#         ans.append((tank, house, diam))

# print(len(ans))
# for tank, tap, diam in sorted(ans):
#     print(tank+1, tap+1, diam)

# O
# from collections import defaultdict
# from queue import Queue
# n = int(input())
# adj = defaultdict(list)
# vis = [False] * n
# parent_colors = [0] * n

# for _ in range(n-1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[a].append(b)
#     adj[b].append(a)

# q = Queue()
# colors = [0]*n

# q.put(0)
# vis[0] = True
# colors[0] = 1
# parent_colors[0] = 1

# while q.qsize():
#     u = q.get()
#     current_color = 1
#     for v in adj[u]:
#         if vis[v]:
#             continue
#         while current_color == colors[u] or current_color == parent_colors[u]:
#             current_color += 1
#         vis[v] = True
#         q.put(v)
#         parent_colors[v] = colors[u]
#         colors[v] = current_color
#         current_color += 1

# print(max(colors))
# for color in colors:
#     print(color, end=" ")

# P -
# from collections import defaultdict
# from queue import Queue
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# n = int(input())
# adj = defaultdict(list)


# for _ in range(n-1):
#     a, b, t = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[a].append((b, t))
#     adj[b].append((a, t))

# vis = [False]*n
# answer = list()

# q = Queue()
# q.put((0, -1))
# vis[0] = True

# while q.qsize():
#     u, last_broken = q.get()
#     leaf = True
#     for v, t in adj[u]:
#         if vis[v]:
#             continue
#         leaf = False
#         vis[v] = True
#         q.put((v, v if t == 2 else last_broken))

#     if leaf and last_broken != -1:
#         answer.append(last_broken + 1)

# print(f"{len(answer)}\n")
# print(' '.join(map(str, answer)))

# Q -
# set of layers
# just compare sets
# from collections import defaultdict
# from queue import Queue

# n = int(input())
# adj = defaultdict(list)
# vis = [False]*n
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[b].append(a)
#     adj[a].append(b)

# bfsed = iter(map(lambda c: int(c) - 1, input().split()))

# q = Queue()
# q.put((0, 1))
# vis[0] = True

# our_layers = defaultdict(set)
# their_layers = defaultdict(set)
# while q.qsize():
#     node, layer = q.get()

#     our_layers[layer].add(node)
#     their_layers[layer].add(next(bfsed))

#     for next_node in adj[node]:
#         if vis[next_node]:
#             continue
#         vis[next_node] = True
#         q.put((next_node, layer + 1))

# good = all(our_layers[layer] == their_layers[layer] for layer in our_layers)
# print("Yes" if good else "No")

