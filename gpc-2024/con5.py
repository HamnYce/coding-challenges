# B -
# n, m = map(int, input().split())
# n = map(int, input().split())
# m = map(int, input().split())


# D -
# n, a, b, s = map(int, input().split())
# base = a+b
# lower_bound = base + a * (n - 2)
# upper_bound = base + b * (n - 2)

# if lower_bound <= s <= upper_bound:
#     print("YES")
# else:
#     print("NO")

# E -
# int main() {
#   int n, m, k;
#   cin >> n >> m >> k;

#   int arr[n];
#   for (int i = 0; i < n; i++) {
#     cin >> arr[i];
#     pq.push(arr[i]);
#   }

#   while (k--) {
#     pq.pop();
#     pq.push(m);
#   }

#   if (pq.top() == m) {
#     cout << "YES" << endl;
#   } else {
#     cout << "NO" << endl;
#   }
# }

# I -
# from math import gcd
# n = int(input())
# xs = list(map(int, input().split()))
# mods = []

# for i in range(n // 2 + 1):
#     diff = abs(xs[i] - xs[-i - 1])
#     if diff != 0:
#         mods.append(diff)

# if len(mods) == 0:
#     print(-1)
# else:
#     best = mods[0]
#     for mod in mods[1:]:
#         best = gcd(best, mod)
#     print(best)


# J -
# n, m = map(int, input().split())
# xs = list(map(int, input().split()))

# px = [0] * n
# sx = [0] * n

# px[0] = xs[0]
# for i in range(1, n):
#     px[i] = xs[i] + px[i - 1]

# sx[n - 1] = xs[n - 1]
# for i in range(n - 2, -1, -1):
#     sx[i] = xs[i] + sx[i + 1]

# if n == 1:
#     print(m)
# else:
#     for i in range(n):
#         if i == 0:
#             print(sx[i + 1], end=" ")
#         elif i == n - 1:
#             print(px[i - 1], end=" ")
#         else:
#             left = px[i - 1]
#             right = sx[i + 1]
#             together = left + right + m
#             print(max([left, right, together]), end=" ")
