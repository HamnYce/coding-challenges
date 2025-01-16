# A-
# n, d = map(int, input().split())
# ns = list(map(int, input().split()))

# for i in range(n):
#     print(ns[(i + d) % n], end=" ")

# B-
# import sys
# lines = sys.stdin.readlines()
# t = int(lines[0])
# stack = []
# i = 0
# for line in lines[1:t + 1]:
#     if line[0] == '1':
#         i += 1
#         stack.append(line)
#     elif line[0] == '2':
#         if i > 0:
#             stack.pop()
#             i -= 1
#     elif line[0] == '3':
#         if i > 0:
#             sys.stdout.write(stack[-1][2:])
#         else:
#             print("Empty!")

# H-
# import sys
# lines = sys.stdin.readlines()
# states = ['']
# for line in lines[1:]:
#     last_state = states[-1]
#     op = line[0]
#     if op == '1':
#         states.append(last_state + line[2:].strip())
#     elif op == '2':
#         k = int(line[2:])
#         states.append(last_state[:len(last_state) - k])
#     elif op == '3':
#         ind = int(line[2:])
#         print(last_state[ind - 1])
#     elif op == '4':
#         states.pop()

# I-
# import sys
# lines = sys.stdin.readlines()
# xs = lines[1].split()
# nums = []
# for i in range(1, len(xs)):
#     if xs[i] == '1':
#         nums.append(xs[i - 1])
# nums.append(xs[-1])
# print(len(nums))
# for num in nums:
#     print(num, end=" ")

# K-
