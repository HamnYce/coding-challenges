# A -
# import sys

# n, k = map(int, sys.stdin.readline().split())
# ns = sorted(map(int, sys.stdin.readline().split()))
# i = 0
# for c in ns:
#     if k - c < 0:
#         break
#     i += 1
#     k -= c
# print(i)

# B -
# import sys
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     bs = input()
#     prev = '0'
#     for b in bs:
#         if prev == '0':
#             if b == '0':
#                 prev = '1'
#             elif b == '1':
#                 prev = '2'

#             sys.stdout.write('1')

#         elif prev == '1':
#             if b == '0':
#                 prev = '0'
#             elif b == '1':
#                 prev = '2'
#             sys.stdout.write(b)

#         elif prev == '2':
#             if b == '0':
#                 prev = '1'
#             elif b == '1':
#                 prev = '1'
#             sys.stdout.write('1' if b == '0' else '0')

#     sys.stdout.write('\n')

# C -
# import sys
# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     ns = list(map(int, input().split()))
#     for i in range(n - 1):
#         max_sub = min(k, ns[i])
#         ns[i] -= max_sub
#         ns[-1] += max_sub
#         k -= max_sub
#     for x in ns:
#         sys.stdout.write(f'{x} ')
#     print()

# D -
# import sys
# t = int(sys.stdin.readline())
# for _ in range(t):
#     c1, c2, c3 = map(int, sys.stdin.readline().split())
#     a1, a2, a3, a4, a5 = map(int, sys.stdin.readline().split())
#     c1 -= a1
#     c2 -= a2
#     c3 -= a3
#     if c1 < 0 or c2 < 0 or c3 < 0:
#         print("NO")
#         continue

#     max_paper_sub = min(c1, a4)
#     a4 -= max_paper_sub
#     c3 -= a4

#     max_plastic_sub = min(c2, a5)
#     a5 -= max_plastic_sub
#     c3 -= a5

#     if c3 < 0:
#         print("NO")
#     else:
#         print("YES")

# E -
# n, m = map(int, input().split())
# xs = sorted(map(int, input().split()))
# c = 0
# for x in xs:
#     if m < 1 or x > 0:
#         break
#     c -= x
#     m -= 1

# print(c)

# F -
# n, m = map(int, input().split())
# xs = list(sorted(map(int, input().split())))
# min_val = 50_001
# for i in range(0, m - n + 1):
#     min_val = min(min_val, xs[i + n - 1] - xs[i])
# print(min_val)

# G -
# the amount of a will always be the same
# the trick is positive negative type shit

# def num_of_parts(s):
#     parts = 1
#     prev = s[0]
#     for i in range(1, len(s)):
#         if prev != s[i]:
#             parts += 1
#             prev = s[i]
#     return parts


# t = int(input())
# for _ in range(t):
#     n, a, b = map(int, input().split())
#     s = input()
#     total = n * a
#     if b >= 0:
#         total += b * n
#     else:
#         parts = num_of_parts(s)
#         total += b * (parts // 2 + 1)
#     print(total)

# H -
# s = input()
# if '0' in s:
#     i = s.index('0')
#     print(s[:i] + s[i + 1:])
# else:
#     print(s[1:])

# I -
# typedef multiset<pair<int, int> > mspi;
# int main() {
#   int n, m, a, b, x, y;
#   mspi ns, ms;
#   map<int, int> rest;
#   int total = 0, beut = 0;
#   cin >> n >> m;

#   for (int i = 0; i < n; i++) {
#     cin >> a >> b;
#     ns.insert(make_pair(a, b));
#   }

#   for (int i = 0; i < m; i++) {
#     cin >> x >> y;
#     ms.insert(make_pair(x, y));
#   }

#   for (mspi::iterator it = ns.begin(); it != ns.end(); it++) {
#     mspi::iterator maybe = ms.find(*it);
#     if (maybe != ms.end()) {
#       total++;
#       beut++;
#       ms.erase(maybe);
#     } else {
#       rest[it->second]++;
#     }
#   }
#   for (mspi::iterator it = ms.begin(); it != ms.end(); it++) {
#     if (rest[it->second]) {
#       total++;
#       rest[it->second]--;
#     }
#   }
#   printf("%d %d", total, beut);
#   return 0;
# }

# J -
# n, k = map(int, input().split())
# xs = list(sorted(map(int, input().split()), reverse=True))
# rounds = 0
# total = 0
# for i in range(n):
#     if i % k == 0:
#         rounds += 1

#     total += xs[i] * rounds

# print(total)

# K -
# n = int(input())
# xs = sorted(map(int, input().split()))
# total = 0
# for i, x in enumerate(xs):
#     total += abs(i + 1 - x)
# print(total)

# L -
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     xs = map(int, input().split())
#     d = dict()
#     smallest = None
#     for i, x in enumerate(xs):
#         if x not in d:
#             d[x] = []
#         d[x].append(i)
#     for k, v in d.items():
#         v = list(sorted(v))
#         for i in range(1, len(v)):
#             if smallest is None:
#                 smallest = v[i] - v[i - 1]
#             else:
#                 smallest = min(smallest, v[i] - v[i - 1])
#     if smallest is None:
#         print(-1)
#     else:
#         print(smallest + 1)

# M -
# st = []
# cs = input()
# bad = 0
# for c in cs:
#     if c == "(":  # )
#         st.append('(')  # )
#     if c == ')':
#         if len(st) and st[-1] == '(':  # )
#             st.pop()
#         else:
#             bad += 1

# print(len(cs) - (bad + len(st)))

# N -
# from queue import PriorityQueue

# n, k = map(int, input().split())
# xs = list(map(int, input().split()))
# pq = PriorityQueue()

# for i in range(n - 2, -1, -1):
#     xs[i] += xs[i + 1]

# for i in range(n):
#     pq.put([-xs[i], i, n])

# while k != 0:
#     p = pq.get()
#     print(f"{-p[0]} ", end="")
#     p[2] -= 1
#     if p[1] != p[2]:
#         p[0] = -(xs[p[1]] - xs[p[2]])
#         pq.put(p)
#     k -= 1


# M -
# import sys
# lines = sys.stdin.readlines()
# n = int(lines[0])
# times = []
# for line in lines[1:]:
#     l, r = map(int, line.split())
#     times.append([r, l])
# times = sorted(times)

# last_time = -1
# total = 0
# for time in times:
#     r, l = time
#     if l > last_time:
#         last_time = r
#         total += 1
# print(total)


# O -
# import sys
# lines = sys.stdin.readlines()
# n = int(lines[0])
# times = []
# for line in lines[1:]:
#     l, r = map(int, line.split())
#     times.append([r, l])
# times = sorted(times)

# last_time = -1
# total = 0
# for time in times:
#     r, l = time
#     if l > last_time:
#         last_time = r
#         total += 1
# print(total)

# P -
# input()
# qs = map(int, input().split())
# m = min(qs)
# input()
# xs = sorted(map(int, input().split()))
# i = 0
# pay = 0

# while len(xs):
#     pay += xs.pop()
#     i += 1

#     if i == m:
#         if len(xs):
#             xs.pop()
#         if len(xs):
#             xs.pop()
#         i = 0


# print(pay)

# Q -

# n, r = map(int, input().split())
# pos_abs = []
# neg_bas = []
# ok = True

# for i in range(n):
#     a, b = map(int, input().split())
#     if b >= 0:
#         pos_abs.append((a, b))
#     else:
#         neg_bas.append((a, b))

# pos_abs = list(sorted(pos_abs))
# neg_bas = list(sorted(neg_bas, reverse=True, key=lambda ab: ab[0] + ab[1]))


# for a, b in pos_abs:
#     if r < a:
#         ok = False
#         break
#     r += b

# for a, b in neg_bas:
#     if not ok:
#         break

#     if r < a:
#         ok = False
#         break

#     r += b

#     if r < 0:
#         ok = False
#         break


# print("YES" if ok else "NO")
