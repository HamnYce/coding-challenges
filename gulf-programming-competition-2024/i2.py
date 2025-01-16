import sys


digits = [False] * 10
anses = dict()
have = [False] * 10
nums = []


def gen_nums(x=0, i=0):
    if i == 5:
        nums.append(x)
        return
    for num in range(0, 10):
        if have[num]:
            continue
        have[num] = True
        gen_nums(x * 10 + num, i + 1)
        have[num] = False


gen_nums()
nums = sorted(nums)


for i in range(10):
    have[i] = False


def good(x, y):
    for _ in range(5):
        d, k = x % 10, y % 10
        if have[d] or have[k]:
            return False
        have[d] = True
        have[k] = True
        x //= 10
        y //= 10

    for i in range(10):
        have[i] = False

    return True


def gen(n):
    for num in nums:
        y = n * num
        if y > 98765:
            return
        if y not in nums:
            continue

        if good(num, y):
            anses[n].append((y, num))


for n in range(2, 80):
    anses[n] = []
    gen(n)

for k in anses:
    anses[k] = sorted(anses[k])

# lines = sys.stdin.readlines()
lines = [61, 2, 62, 0]
b = False
for line in lines[:-1]:
    if b:
        sys.stdout.write("\n")

    n = int(line)
    if len(anses[n]) == 0:
        sys.stdout.write("There are no solutions for {}.\n".format(n))
    else:
        for ans in anses[n]:
            sys.stdout.write(
                "{:0>5} / {:0>5} = {}\n".format(ans[0], ans[1], n))
    b = True
