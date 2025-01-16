# A -
# v, e = map(int, input().split())
# adj = []
# for _ in range(v):
#     adj.append([])

# for _ in range(e):
#     a, b = map(int, input().split())
#     adj[a - 1].append(b - 1)

# visited = [False] * v


# def dfs(curr_v):
#     global visited
#     if visited[curr_v]:
#         return
#     visited[curr_v] = True
#     for next_v in adj[curr_v]:
#         dfs(next_v)

# dfs(0)
# if all(visited) and e == v - 1:
#     print("YES")
# else:
#     print("NO")

# B -
# from sys import stdin

# t = int(stdin.readline())


# def colorise(curr_v, color, adj, colors):
#     if colors[curr_v] == 0:
#         colors[curr_v] = color
#     elif colors[curr_v] == color:
#         return True
#     else:
#         return False

#     good = True

#     for next_v in adj[curr_v]:
#         good = good and colorise(next_v, 1 if color == 2 else 2, adj, colors)

#     return good


# for case in range(1, t + 1):
#     v, e = map(int, stdin.readline().split())
#     adj = [list() for _ in range(v)]
#     colors = [0] * v
#     for _ in range(e):
#         a, b = map(int, stdin.readline().split())
#         a -= 1
#         b -= 1
#         adj[a].append(b)
#         adj[b].append(a)

#     good = True
#     for i in range(v):
#         if not good:
#             break
#         if not colors[i]:
#             good = good and colorise(i, 1, adj, colors)

#     print(f"Scenario #{case}:\n{'Suspicious bugs found!' if not good else 'No suspicious bugs found!'}")

# C -
# from collections import defaultdict
# import sys
# lines = sys.stdin.readlines()
# offset = 0

# while True:
#     n, m = map(int, lines[offset].split())
#     offset += 1
#     if n == 0 and m == 0:
#         break

#     adj = defaultdict(list)
#     indegrees = [0]*n
#     for _ in range(m):
#         over, under = map(int, lines[offset].split())
#         offset += 1

#         over -= 1
#         under -= 1
#         indegrees[under] += 1
#         adj[over].append(under)

#     visited = [False] * n
#     stack = []
#     answer = []
#     for node in range(n):
#         if indegrees[node] == 0:
#             stack.append(node)

#     while stack:
#         curr_node = stack[-1]
#         stack.pop()
#         answer.append(curr_node)
#         for next_node in adj[curr_node]:
#             indegrees[next_node] -= 1
#             if indegrees[next_node] == 0:
#                 stack.append(next_node)


#     if len(answer) == n:
#         print('\n'.join(map(lambda x: str(x+1), answer)))
#     else:
#         print('IMPOSSIBLE')


# D -
# from collections import defaultdict
# import sys
# c, r = 1, 1
# while True:
#     c, r = map(int, sys.stdin.readline().split())
#     if c == 0 and r == 0:
#         break
#     trans = dict()
#     for i in range(c):
#         trans[sys.stdin.readline().strip()] = i

#     adj = defaultdict(list)

#     for _ in range(r):
#         prey, pred = sys.stdin.readline().split()
#         prey = trans[prey]
#         pred = trans[pred]

#         adj[prey].append(pred)
#         adj[pred].append(prey)

#     visited = [False] * c
#     biggest_chain_length = 0
#     for node in range(c):
#         chain_length = 0
#         stack = [node]
#         while stack:
#             curr_node = stack[-1]
#             stack.pop()
#             if visited[curr_node]:
#                 continue
#             chain_length += 1
#             visited[curr_node] = True
#             for next_node in adj[curr_node]:
#                 stack.append(next_node)
#         biggest_chain_length = max(biggest_chain_length, chain_length)

#     sys.stdout.write(f"{biggest_chain_length}\n")
#     sys.stdin.readline()

# E -
# n = int(input())
# roots = [True] * n
# adj = [list() for _ in range(n)]

# for _ in range(n-1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1

#     roots[b] = False

#     adj[a].append(b)
#     adj[b].append(a)

# # finding root node
# root_node = 0
# for i, node in enumerate(roots):
#     if node:
#         root_node = i
# ##

# farthest_node = root_node
# farthest_distance = 0

# visited = [0] * n
# stack = [(root_node, 0)]
# while stack:
#     node, dist = stack[-1]
#     visited[node] = 1
#     if dist > farthest_distance:
#         farthest_node = node
#         farthest_distance = dist
#     stack.pop()
#     for next in adj[node]:
#         if visited[next]:
#             continue
#         stack.append((next, dist + 1))
# ##

# visited = [0] * n
# stack = [(farthest_node, 0)]
# farthest_node = 0
# farthest_distance = 0
# while stack:
#     node, dist = stack[-1]
#     visited[node] = 1
#     if dist > farthest_distance:
#         farthest_node = node
#         farthest_distance = dist
#     stack.pop()
#     for next in adj[node]:
#         if visited[next]:
#             continue
#         stack.append((next, dist + 1))
# ##
# print(farthest_distance)

# F -

# from collections import defaultdict

# n = int(input())
# adj = defaultdict(list)
# dep = [0] * n
# top_managers = []

# for i in range(n):
#     p = int(input())
#     if p != -1:
#         adj[p - 1].append(i)
#     else:
#         top_managers.append(i)

# for i in top_managers:
#     stack = [i]
#     while stack:
#         curr_node = stack[-1]
#         stack.pop()
#         for next_node in adj[curr_node]:
#             dep[next_node] = dep[curr_node] + 1
#             stack.append(next_node)

# ans = max(dep)
# print(ans + 1)

# G -
# from collections import defaultdict
# n = int(input())
# relations = map(int, input().split())

# adj = defaultdict(list)
# for a, b in enumerate(relations):
#     b -= 1
#     adj[a].append(b)
#     adj[b].append(a)

# colors = [0]*n  # this also acts as a visited array
# color = 0
# for node in range(n):
#     if colors[node] == 0:
#         color += 1
#         stack = [node]
#         while stack:
#             curr_node = stack[-1]
#             stack.pop()
#             colors[curr_node] = color
#             for next_node in adj[curr_node]:
#                 if colors[next_node] == 0:
#                     stack.append(next_node)
# print(color)

# H -
# from collections import defaultdict
# import sys
# n, m = 1, 1
# while n or m:
#     n, m = map(int, sys.stdin.readline().split())
#     adj = defaultdict(list)
#     indegree = [0] * n
#     for _ in range(m):
#         a, b = map(int, sys.stdin.readline().split())
#         adj[a - 1].append(b - 1)
#         indegree[b - 1] += 1

#     indegree_zero = []

#     for node in range(n):
#         if indegree[node] == 0:
#             indegree_zero.append(node)

#     answer = []
#     while indegree_zero:
#         curr_node = indegree_zero[-1]
#         indegree_zero.pop()
#         answer.append(curr_node)
#         for next_node in adj[curr_node]:
#             indegree[next_node] -= 1
#             if indegree[next_node] == 0:
#                 indegree_zero.append(next_node)

#     sys.stdout.write(' '.join(map(lambda x: str(x+1), answer)) + "\n")

# I -
# from collections import defaultdict
# n, m = map(int, input().split())
# adj = defaultdict(list)
# for _ in range(m):
#     a, b = map(int, input().split())
#     adj[a - 1].append(b - 1)
#     adj[b - 1].append(a - 1)

# visited = [False] * n
# power = 0
# for node in range(n):
#     nodes_in_tree = 0
#     stack = [node]
#     while stack:
#         curr_node = stack[-1]
#         stack.pop()
#         if visited[curr_node]:
#             continue
#         visited[curr_node] = True
#         nodes_in_tree += 1
#         for next_node in adj[curr_node]:
#             stack.append(next_node)

#     if nodes_in_tree:
#         power += nodes_in_tree - 1
# print(2**power)

# J -
# from collections import defaultdict
# n = int(input())
# adj = defaultdict(list)
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     adj[a - 1].append(b - 1)
#     adj[b - 1].append(a - 1)

# inits = list(map(int, input().split()))
# goals = list(map(int, input().split()))

# node = 0
# node_value = inits[0]
# flip_next = 0
# stack: list[tuple[int, int, int]] = [(node, node_value, flip_next)]
# answer = []
# visited = [False] * n

# while stack:
#     node, node_value, flip_next = stack[-1]
#     visited[node] = True
#     stack.pop()
#     flip_next_next = inits[node] ^ goals[node]
#     if node_value != goals[node]:
#         answer.append(node)

#     for next_node in adj[node]:
#         if visited[next_node]:
#             continue
#         stack.append((
#             next_node,
#             inits[next_node] ^ flip_next,
#             flip_next_next
#         ))
# print(len(answer))
# for v in answer:
#     print(v + 1)

# K -
# from collections import defaultdict


# n = int(input())
# adj = defaultdict(list)
# for _ in range(n):
#     a, b = map(int, input().split())
#     adj[a].append(b)
#     adj[b].append(a)

# starting_node = 0
# for node in adj:
#     if len(adj[node]) == 1:
#         starting_node = node

# stack = [starting_node]
# visited = set()
# while stack:
#     node = stack[-1]
#     stack.pop()

#     if node in visited:
#         continue
#     print(node, end=" ")
#     visited.add(node)

#     for next_node in adj[node]:
#         if next_node in visited:
#             continue
#         stack.append(next_node)

# L -
# from collections import defaultdict


# adj = defaultdict(list)
# n, orig_capital, new_capital = map(int, input().split())
# orig_capital -= 1
# new_capital -= 1
# relations = list(map(lambda s: int(s) - 1, input().split()))
# relations.insert(orig_capital, -1)

# for child, parent in enumerate(relations):
#     if parent == -1:
#         continue
#     adj[parent].append(child)
#     adj[child].append(parent)

# # we have a tree and now we just want to dfs from the new capital head and print out the parents
# direct_parents = [-2] * n
# direct_parents[new_capital] = -1

# stack = [new_capital]
# while stack:
#     curr_city = stack[-1]
#     stack.pop()
#     for next_city in adj[curr_city]:
#         if direct_parents[next_city] != -2:
#             continue

#         direct_parents[next_city] = curr_city
#         stack.append(next_city)

# for city in direct_parents:
#     if city == -1:
#         continue
#     print(f"{city + 1}", end=" ")

# M
# from collections import defaultdict
# n = int(input())
# adj = defaultdict(list)
# a = 0
# for _ in range(n - 1):
#     a, b = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[a].append(b)
#     adj[b].append(a)

# red = set()  # False
# blue = set()  # True

# visited = [False] * n
# stack = []
# stack.append((a, 'red'))
# red.add(a)

# while stack:
#     node, node_color = stack[-1]
#     stack.pop()
#     visited[node] = True
#     next_color = 'blue' if node_color == 'red' else 'red'
#     next_color_set = blue if node_color == 'red' else red

#     for next_node in adj[node]:
#         if visited[next_node]:
#             continue
#         next_color_set.add(next_node)
#         stack.append((next_node, next_color))

# total = 0
# for node in red:
#     total += abs(len(adj[node]) - len(blue))

# for node in blue:
#     total += abs(len(adj[node]) - len(red))
# print(total // 2)
