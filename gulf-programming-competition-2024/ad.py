n, k = map(int, input().split())

total_pipes = (k - 1) * k // 2 + 1  # + 1 for the starting pipe


def splitter_to_pipes(num_splitters):
    global k, total_pipes
    remove_splitters = k - num_splitters
    remove_pipes = (remove_splitters - 1) * remove_splitters // 2
    return total_pipes - remove_pipes


if total_pipes < n:
    print(-1)
else:
    left = -1
    right = k
    mid = 0
    while left + 4 < right:
        mid = (left + right) // 2
        pipes = splitter_to_pipes(mid)
        if pipes < n:
            left = mid
        elif pipes > n:
            right = mid
        else:
            break

    left -= 10
    while splitter_to_pipes(left) < n:
        left += 1

    print(left)
