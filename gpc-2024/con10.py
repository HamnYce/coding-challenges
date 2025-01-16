ans = sorted([int(input()) for _ in range(int(input()))]);print(min([x+y for x, y in zip(ans, reversed(ans))]))
