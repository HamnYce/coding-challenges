# a - boy or girl
# print("IGNORE HIM!") if len(set(input())) % 2 == 1 else print("CHAT WITH HER!")

# b - registration system
# import sys
# lines = sys.stdin.readlines()
# d = {}
# for line in lines[1:]:
#     line = line.strip()
#     if line not in d:
#         d[line] = 0
#         print("OK")
#     else:
#         d[line] += 1
#         print(line + str(d[line]))

# c - cancel the trains
# import sys
# lines = sys.stdin.readlines()
# t = int(lines[0])
# line_len = 1
# for _ in range(t):
#     n, m = map(int, lines[line_len].split())
#     s = set(lines[line_len + 1].split())
#     ans = 0
#     ans = sum([x in s for x in lines[line_len + 2].split()])
#     sys.stdout.write(f'{ans}\n')

#     line_len += 3

# d - anton and letters
# print(len(set(filter(len, input()[1:-1].split(', ')))))

# e - andy's first dictionary
# import sys
# import re
# lines = sys.stdin.readlines()
# d = dict()
# for line in lines:
#     for word in re.split(r'[^a-z]', line.lower()):
#         d[word] = None

# if '' in d:
#     d.pop('')

# for k in sorted(d):
#     print(k)

# f - keyboard
# keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'
# let_to_ind = dict(zip(keyboard, range(len(keyboard))))
# offset = 1 if input() == 'L' else -1
# print(''.join([keyboard[let_to_ind[letter] + offset] for letter in input()]))

# g - two strings
# for _ in range(int(input())):
#     s1 = set(input())
#     has = False
#     for letter in input():
#         if letter in s1:
#             has = True
#             break
#     print("YES" if has else "NO")

# h - chat order
# import sys
# lines = sys.stdin.readlines()
# chat = dict()
# for line in lines[1:]:
#     if line in chat:
#         chat.pop(line)

#     chat[line] = None

# for k in reversed(chat):
#     sys.stdout.write(k)

# i - launch of collider
# import sys
# lines = sys.stdin.readlines()
# dirs = lines[1]
# parts = map(int, lines[2].split())
# diff = 10**10
# right_most = None
# for part, dir in zip(parts, dirs):
#     if dir == 'R':
#         right_most = part
#     if dir == 'L' and right_most is not None:
#         diff = min(diff, part - right_most)
#         right_most = None

# print(-1 if diff == 10**10 else diff // 2)

# j - potions (hard version)
# int main() {
#   priority_queue<int> pq;
#   int n, temp;
#   long long health = 0;
#   scanf("%d", &n);
#   while (n--) {
#     scanf("%d", &temp);
#     health += temp;
#     pq.push(-temp);
#     while (health < 0) {
#       health += pq.top();
#       pq.pop();
#     }

#   }
#   printf("%d\n", int(pq.size()));

#   return 0;
# }

# k - equalize array
# import sys
# from collections import Counter
# lines = sys.stdin.readlines()
# t = int(lines[0])
# line_offset = 1
# for _ in range(t):
#     counter = Counter(lines[line_offset + 1].split())
#     freq = Counter(counter.values())
#     sorted_freq = sorted(freq.items())
#     min_sum = 10**20
#     for i in range(len(sorted_freq)):
#         backward_sum = sum(k * v for k, v in sorted_freq[:i])
#         forward_sum = sum(
#             [(k - sorted_freq[i][0]) * v for k, v in sorted_freq[i:]])
#         min_sum = min(min_sum, backward_sum + forward_sum)

#     print(min_sum)

#     line_offset += 2

# l - sorting queries
# from collections import deque
# from queue import PriorityQueue
# import sys
# dq = deque()
# pq = PriorityQueue()
# lines = sys.stdin.readlines()
# for line in lines[1:]:
#     if line[0] == '1':
#         dq.append(int(line[2:]))
#     elif line[0] == '2':
#         if not pq.empty():
#             print(pq.get())
#         else:
#             print(dq.popleft())
#     else:
#         for _ in range(len(dq)):
#             pq.put(dq.pop())

# m - heap operations
# int main() {
#   priority_queue<int, vector<int>, greater<>> pq;
#   int n, num;
#   string ins;
#   scanf("%d", &n);
#   vector<char> output_codes;
#   queue<int> output_nums;
#   while (n--) {
#     scanf("%s", &ins[0]);
#     switch (ins[0]) {
#     case 'i':
#       scanf("%d", &num);
#       pq.push(num);
#       output_codes.push_back('i');
#       output_nums.push(num);
#       break;
#     case 'g':
#       scanf("%d", &num);
#       while (!pq.empty() && pq.top() < num) {
#         pq.pop();
#         output_codes.push_back('r');
#       }

#       if (pq.empty() || pq.top() > num) {
#         pq.push(num);
#         output_codes.push_back('i');
#         output_nums.push(num);
#       }

#       output_codes.push_back('g');
#       output_nums.push(num);

#       break;
#     case 'r':
#       if (pq.empty()) {
#         output_codes.push_back('i');
#         output_nums.push(1);
#       } else {
#         pq.pop();
#       }
#       output_codes.push_back('r');
#       break;
#     }
#   }

#   printf("%lu\n", output_codes.size());

#   for (int i = 0; i < output_codes.size(); i++) {
#     if (i)
#       printf("\n");

#     char c = output_codes[i];
#     switch (c) {
#     case 'i':
#       printf("insert %d", output_nums.front());
#       output_nums.pop();
#       break;
#     case 'r':
#       printf("removeMin");
#       break;
#     case 'g':
#       printf("getMin %d", output_nums.front());
#       output_nums.pop();
#       break;
#     }
#   }

#   return 0;
# }

# n - berpizza
# class Compare {
# public:
#   bool operator()(pair<int, int> a, pair<int, int> b) {
#     if (a.first == b.first) {
#       return b.second < a.second;
#     } else
#       return a.first < b.first;
#   }
# };

# int main() {
#   queue<int> q;
#   priority_queue<pair<int, int>, vector<pair<int, int> >, Compare> pq;

#   set<int> custs;

#   int n, ins, cus_num = 1, cus_value, temp_cust, temp_money;
#   cin >> n;
#   while (n--) {
#     cin >> ins;
#     if (ins == 1) {
#       cin >> cus_value;
#       q.push(cus_num);
#       pq.push(make_pair(cus_value, cus_num));
#       cus_num++;
#     } else if (ins == 2) {
#       while (custs.count(q.front()))
#         q.pop();
#       printf("%d ", q.front());
#       custs.insert(q.front());
#       q.pop();
#     } else {
#       while (custs.count(pq.top().second))
#         pq.pop();
#       printf("%d ", pq.top().second);
#       custs.insert(pq.top().second);
#       pq.pop();
#     }
#   }
#   return 0;
# }

# O - Three Sevens
# import sys

# # NOTE: this question is sorting one array based on another
# t = int(sys.stdin.readline())
# for _ in range(t):
#     m = int(sys.stdin.readline())
#     day_to_lot = dict()
#     lot_to_day = dict()
#     for day in range(m):
#         n = int(sys.stdin.readline())
#         lots = map(int, sys.stdin.readline().split())
#         for lot in lots:
#             lot_to_day[lot] = day

#     for lot, day in lot_to_day.items():
#         day_to_lot[day] = lot

#     if len(day_to_lot) != m:
#         print(-1)
#     else:
#         for day, lot in sorted(day_to_lot.items()):
#             print(f"{lot} ", end="")
#         print()

# P - F1 Champions
# pts = dict(zip(range(1, 11), [25, 18, 15, 12, 10, 8, 6, 4, 2, 1],))

# t = int(input())
# players = dict()

# for _ in range(t):
#     n = int(input())
#     for place in range(1, n + 1):
#         name = input()
#         if name not in players:
#             players[name] = [0] * 54

#         players[name][place] += 1

#         if place in pts:
#             players[name][0] += pts[place]

# print(max(players.items(), key=lambda a: a[1])[0])

# for name in players:
#     temp = players[name][0]
#     players[name][0] = players[name][1]
#     players[name][1] = temp

# print(max(players.items(), key=lambda a: a[1])[0])

# Q - Playlist
import sys
from queue import PriorityQueue
n, k = map(int, sys.stdin.readline().split())
playlist: dict[int, set[int]] = dict()
max_pleasure = 0

for _ in range(n):
    time, beauty = map(int, sys.stdin.readline())
    if beauty not in playlist:
        playlist[beauty] = set()

    playlist[beauty].add(time)

sorted_playlist = reversed(sorted(playlist))
print(list(sorted_playlist))
