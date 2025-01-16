# A -
# from queue import PriorityQueue
# from collections import defaultdict
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# t = int(input())
# for _ in range(t):
#     adj = defaultdict(list)
#     pq = PriorityQueue()
#     n, m, s, d = map(int, input().split())

#     for _ in range(m):
#         a, b, c = map(int, input().split())
#         adj[a].append((b, c))
#         adj[b].append((a, c))

#     dist = [-1]*(n+1)
#     dist[s] = 0
#     pq.put((0, s))
#     while pq.qsize():
#         back_cost, u = pq.get()

#         if back_cost > dist[u]:
#             continue

#         for v, forward_cost in adj[u]:
#             if dist[v] == -1 or back_cost + forward_cost < dist[v]:
#                 dist[v] = back_cost + forward_cost
#                 pq.put((dist[v], v))
#     if dist[d] == -1:
#         print("NONE\n")
#     else:
#         print(f"{dist[d]}\n")

# B -
# from collections import defaultdict
# from queue import PriorityQueue
# import sys
# n, m = map(int, input().split())
# adj = defaultdict(dict)
# pq = PriorityQueue()
# input = sys.stdin.readline
# write = sys.stdout.write

# dist = [-1]*(n+1)
# parents = [-1]*(n+1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     if a == b:
#         continue

#     adj[a][b] = min(adj[a][b], c) if b in adj[a] else c

#     adj[b][a] = min(adj[b][a], c) if a in adj[b] else c

# dist[1] = 0
# pq.put((0, 1))
# while pq.qsize():
#     back_cost, u = pq.get()

#     if back_cost > dist[u]:
#         continue

#     for v in adj[u]:
#         forward_cost = adj[u][v]
#         if dist[v] == -1 or dist[u] + forward_cost < dist[v]:
#             dist[v] = dist[u] + forward_cost
#             parents[v] = u
#             pq.put((dist[v], v))

# if dist[n] == -1:
#     print(-1)
# else:
#     answer = []
#     while n != -1:
#         answer.append(n)
#         n = parents[n]
#
#     for u in reversed(answer):
#         write(f"{u} ")
#

# C -
# # Correct output, but doesn't work with UVA's interpreter
# from collections import defaultdict
# from heapq import heappop, heappush
# from math import ceil
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# inf = 10**18
# n, r = map(int, input().split())
# scenario = 1
# while n or r:
#     adj = defaultdict(list)
#     for _ in range(r):
#         u, v, c = map(int, input().split())
#         u -= 1
#         v -= 1
#         adj[u].append((c, v))
#         adj[v].append((c, u))

#     s, d, t = map(int, input().split())
#     s -= 1
#     d -= 1
#     if s == d:
#         print("Scenario %s\n" % scenario)
#         print("Minimum Number of Trips = 0\n\n")

#         scenario += 1
#         n, r = map(int, input().split())
#         continue
#     pq = [(inf, s)]
#     dist = [-1] * n

#     while pq:
#         back_cost, u = heappop(pq)

#         if back_cost < dist[u]:
#             continue

#         for forward_cost, v in adj[u]:
#             if min(back_cost, forward_cost) > dist[v]:
#                 dist[v] = min(back_cost, forward_cost)
#                 heappush(pq, (dist[v], v))

#     print("Scenario #%s\n" % scenario)
#     print("Minimum Number of Trips = %s\n\n" % ceil(t / (dist[d] - 1)))

#     scenario += 1
#     n, r = map(int, input().split())


# D -


# K -
# from collections import defaultdict
# import heapq
# import sys

# input = sys.stdin.readline
# print = sys.stdout.write
# n, m = map(int, input().split())
# adj = defaultdict(list)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     a -= 1
#     b -= 1
#     adj[a].append((c, b))
#     adj[b].append((c, a))

# dist = list(map(int, input().split()))

# pq = []
# for i in range(n):
#     heapq.heappush(pq, (dist[i], i))

# while pq:
#     back_cost, u = heapq.heappop(pq)

#     if back_cost > dist[u]:
#         continue

#     for forward_cost, v in adj[u]:
#         new_cost = 2 * forward_cost + dist[u]
#         if new_cost < dist[v]:
#             dist[v] = new_cost
#             heapq.heappush(pq, (new_cost, v))

# print(' '.join(map(str, dist)))

# F -
# import sys
# import heapq

# lines = [map(int, line.split()) for line in sys.stdin.readlines()]
# deltas = ((1, 2), (1, -2), (-1, 2), (-1, -2),
#           (2, 1), (2, -1), (-2, 1), (-2, -1))
# for line in lines:
#     a, b, d_x, d_y = line
#     dist = [[10**9]*8 for _ in range(8)]
#     dist[a][b] = 0
#     pq = []
#     heapq.heappush(pq, (dist[a][b], a, b))
#     while pq:
#         c, x, y = heapq.heappop(pq)

#         if x == d_x and y == d_y:
#             break
#         if c > dist[x][y]:
#             continue

#         for dx, dy in deltas:
#             nx, ny = x + dx, y + dy
#             if not (nx >= 0 and nx < 8 and ny >= 0 and ny < 8):
#                 continue
#             nc = c + x*nx + y*ny
#             if nc < dist[nx][ny]:
#                 dist[nx][ny] = nc
#                 heapq.heappush(pq, (nc, nx, ny))
#     print(dist[d_x][d_y])

# G -
# UNSOLVABLE IN PYTHON

# H -
# from collections import defaultdict
# import sys
# import heapq
# lines = iter(sys.stdin.readlines())
# while True:
#     try:
#         n, d = map(int, next(lines).split())
#     except:
#         break
#     transition_times = list(map(int, next(lines).split()))
#     allowed = [[False]*100 for _ in range(n)]
#     adj = defaultdict(list)

#     for i in range(n):
#         prev_floor = -1
#         for curr_floor in map(int, next(lines).split()):
#             if prev_floor != -1:
#                 transition_time = (curr_floor - prev_floor) * \
#                     transition_times[i]
#                 adj[(i, prev_floor)].append((transition_time, (i, curr_floor)))
#                 adj[(i, curr_floor)].append((transition_time, (i, prev_floor)))

#             prev_floor = curr_floor
#             allowed[i][curr_floor] = True

#     for j in range(100):
#         for i in range(n):
#             if not allowed[i][j]:
#                 continue
#             for k in range(i+1, n):
#                 if not allowed[k][j]:
#                     continue
#                 adj[(i, j)].append((60, (k, j)))
#                 adj[(k, j)].append((60, (i, j)))
#     dist = [[10**9] * 100 for _ in range(n)]
#     pq = []
#     for i in range(n):
#         if allowed[i][0]:
#             dist[i][0] = 0
#             heapq.heappush(pq, (0, (i, 0)))

#     while pq:
#         temp = heapq.heappop(pq)
#         back_cost = temp[0]
#         u = temp[1]

#         if (back_cost > dist[u[0]][u[1]]):
#             continue

#         for forward_cost, v in adj[u]:
#             if (forward_cost + back_cost < dist[v[0]][v[1]]):
#                 dist[v[0]][v[1]] = forward_cost + back_cost
#                 heapq.heappush(pq, (dist[v[0]][v[1]], v))

#     distance = 10**9
#     for i in range(n):
#         distance = min(distance, dist[i][d])

#     if distance == 10**9:
#         print("IMPOSSIBLE")
#     else:
#         print(distance)

# I -
# from collections import defaultdict
# import heapq
# import sys
# lines = iter(sys.stdin.readlines())
# t = int(next(lines))
# for map_number in range(1, t+1):
#     if map_number > 1:
#         sys.stdout.write('\n')
#     sys.stdout.write("Map #{}\n".format(map_number))
#     map_number += 1
#     next(lines)

#     n = int(next(lines))
#     station_costs = [0]*n
#     i = 0
#     translation = dict()
#     for _ in range(n):
#         station, cost = next(lines).split()
#         translation[station] = i
#         translation[i] = station
#         station_costs[i] = int(cost)
#         i += 1

#     adj = defaultdict(list)
#     m = int(next(lines))
#     for _ in range(m):
#         station_1, station_2, cost = next(lines).split()
#         station_1 = translation[station_1]
#         station_2 = translation[station_2]
#         cost = int(cost)
#         adj[station_1].append((cost*2, station_2))
#         adj[station_2].append((cost*2, station_1))

#     q = int(next(lines))
#     for i in range(1, q+1):
#         sys.stdout.write("Query #{}\n".format(i))
#         station_1, station_2, passenger = next(lines).split()
#         station_1 = translation[station_1]
#         station_2 = translation[station_2]
#         passenger = int(passenger)

#         dist = [10**9]*n
#         parents = [-1]*n
#         dist[station_1] = station_costs[station_1]
#         pq = [(dist[station_1], station_1)]

#         while pq:
#             back_cost, u = heapq.heappop(pq)

#             if (back_cost > dist[u]):
#                 continue

#             for forward_cost, v in adj[u]:
#                 if (back_cost + forward_cost + station_costs[v] < dist[v]):
#                     dist[v] = back_cost + forward_cost + station_costs[v]
#                     parents[v] = u
#                     heapq.heappush(pq, (dist[v], v))

#         total_price = dist[station_2]
#         answer = []
#         while station_2 != -1:
#             answer.append(station_2)
#             station_2 = parents[station_2]

#         sys.stdout.write(
#             ' '.join(map(lambda parent: translation[parent], reversed(answer))))
#         sys.stdout.write('\n')
#         sys.stdout.write("Each passenger has to pay : %.2f taka\n" %
#                          (total_price * 1.10 / passenger))

# J -
# from collections import defaultdict
# import heapq
# import sys
# lines = iter(sys.stdin.readlines())
# print = sys.stdout.write


# def dijkstra(wisdom, n, adj):
#     dist = [-1] * (n+1)
#     dist[1] = 0
#     pq = [(dist[1], 1)]

#     while pq:
#         back_cost, u = heapq.heappop(pq)

#         if u == n:
#             return back_cost
#         if back_cost > dist[u]:
#             continue

#         for forward_cost, w, v in adj[u]:
#             if wisdom >= w and (dist[v] == -1 or back_cost + forward_cost < dist[v]):
#                 dist[v] = back_cost + forward_cost
#                 heapq.heappush(pq, (dist[v], v))

#     return dist[n]


# t = int(next(lines))
# for _ in range(t):
#     n, m, k = map(int, next(lines).split())
#     adj = defaultdict(list)
#     for _ in range(m):
#         s1, s2, c, w = map(int, next(lines).split())
#         adj[s1].append((c, w, s2))
#         adj[s2].append((c, w, s1))

#     l, r, mid, ans = 1, 10**9, 0, -1
#     while l <= r:
#         mid = (l+r) >> 1
#         if dijkstra(mid, n, adj) < k:
#             ans = mid
#             r = mid - 1
#         else:
#             l = mid + 1
#     print(str(ans)+'\n')

