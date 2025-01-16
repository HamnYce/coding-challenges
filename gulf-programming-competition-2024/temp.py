from math import ceil
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    print("NO" if ceil(n/m) + k >= n else "YES")
