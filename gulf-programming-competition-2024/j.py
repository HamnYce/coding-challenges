# A -
# n, k = map(int, input().split())

# ans = []
# while n != 1 and len(ans) != k:
#     for x in range(2, n + 1):
#         if n % x == 0:
#             ans.append(x)
#             n //= x
#             break

# ans[-1] *= n
# if len(ans) == k:
#     for a in ans:
#         print(a, end=" ")
# else:
#     print(-1)

# B -
# sieve = [1] * 3001
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)


# def prime_factorise(n):
#     global primes
#     factors = set()
#     while n != 1:
#         for prime in primes:
#             if n % prime == 0:
#                 factors.add(prime)
#                 n //= prime
#                 break
#     return factors

# n = int(input())
# t = 0
# for i in range(2, n + 1):
#     if len(prime_factorise(i)) == 2:
#         t += 1
# print(t)


# C -
# sieve = [1] * 1000
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)

# total_divisors = dict()


# def prime_factorise(n):
#     global total_divisors
#     if n == 1:
#         return 1
#     global primes
#     factors = []
#     while n != 1:
#         for prime in primes:
#             if n % prime == 0:

#                 if prime not in total_divisors:
#                     total_divisors[prime] = 0
#                 total_divisors[prime] += 1

#                 factors.append(prime)
#                 n //= prime
#                 break
#     return factors


# n = int(input())
# total = 1
# for i in range(1, n + 1):
#     prime_factorise(i)

# for _, v in total_divisors.items():
#     total *= v + 1
#     total %= (1e9+7)
# print(int(total))

# D -
# sieve = [1] * 1000
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)


# def number_of_divisors(n):
#     global primes
#     factors = dict()
#     while n != 1:
#         for prime in primes:
#             if n % prime == 0:
#                 if prime not in factors:
#                     factors[prime] = 0
#                 factors[prime] += 1
#                 n //= prime
#                 break

#     total_factors = 1
#     for v in factors.values():
#         total_factors *= v + 1

#     return total_factors


# a, b, c = map(int, input().split())
# memo = dict()
# total = 0
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         for k in range(1, c+1):
#             prod = i*j*k
#             if prod not in memo:
#                 memo[prod] = number_of_divisors(prod)
#             total += memo[prod]
# print(total)

# E -
# import sys
# sieve = [1] * 1100
# sieve[0] = 0

# good = "It is a prime word."
# bad = "It is not a prime word."

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = {i for i, b in enumerate(sieve) if b}

# trans = dict()

# for c in range(97, 97+26):
#     trans[chr(c)] = c - 96

# for c in range(65, 65+26):
#     trans[chr(c)] = c - 38

# trans['\n'] = 0

# def conv(c): return trans[c]

# lines = sys.stdin.readlines()


# i = 0
# for line in lines:
#     if sum(map(conv, line)) in primes:
#         print(good)
#     else:
#         print(bad)

# F -
# sieve = [1] * 1100
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = [i for i, b in enumerate(sieve) if b]
# primes_set = set(primes)

# n, k = map(int, input().split())
# total = 0
# for i in range(len(primes) - 1):
#     test = primes[i] + primes[i + 1] + 1
#     if test > n:
#         break
#     if test in primes_set:
#         total += 1


# print("YES" if total >= k else "NO")

# G -
# sieve = [1] * (int(1e6) + 10)
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = [i for i, b in enumerate(sieve) if b]
# sqrd_primes = set(map(lambda x: x*x, primes))

# n = input()
# xs = map(int, input().split())
# for x in xs:
#     print("YES" if x in sqrd_primes else "NO")


# H -
# NOTE: prime factors find the count of the higest amount of primes factors
# then just put that many of them (-1 so that a_k is disivisble by it)
# and n divided by them
# import sys
# from collections import Counter
# sieve = [1] * (int(1e5) + 10)
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)


# def prime_factorise(n):
#     global primes
#     factors = Counter()
#     possible = True
#     while possible:
#         possible = False
#         if n == 1:
#             break
#         for prime in primes:
#             if n % prime == 0:
#                 factors[prime] += 1
#                 n //= prime
#                 possible = True
#                 break

#     return factors


# lines = sys.stdin.readlines()
# for line in lines[1:]:
#     n = int(line)
#     factors: Counter = prime_factorise(n)
#     seq = []
#     if len(factors) == 0 or factors.most_common(1)[0] == 1:
#         seq.append(n)
#     else:
#         prime, amount = factors.most_common(1)[0]
#         amount -= 1
#         seq = [prime] * amount
#         seq.append(n // (prime ** amount))

#     sys.stdout.write(f"{len(seq)}\n")
#     for x in seq:
#         sys.stdout.write(f"{x} ")
#     sys.stdout.write("\n")

# I -
# from bisect import bisect_left
# sieve = [1] * (int(1e5) + 10)
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)

# n, m = map(int, input().split())
# board = []
# diff_matrix = []
# for _ in range(n):
#     board.append(list(map(int, input().split())))
#     diff_matrix.append([0] * m)


# for i in range(n):
#     for j in range(m):
#         k = bisect_left(primes, board[i][j])
#         diff_matrix[i][j] = primes[k] - board[i][j]

# best = sum(diff_matrix[0])
# for i in range(1, n):
#     best = min(best, sum(diff_matrix[i]))

# for j in range(m):
#     total = 0
#     for i in range(n):
#         total += diff_matrix[i][j]
#     best = min(best, total)
# print(best)

# J -
# sieve = [1] * int(1e6 + 10)
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)


# def prime_factorise(n):
#     global primes
#     biggest_factor = 1
#     possible = True
#     while possible:
#         possible = False
#         for prime in primes:
#             if n % prime == 0:
#                 biggest_factor = prime
#                 n //= prime
#                 possible = True
#                 break
#     return max(biggest_factor, n)


# for _ in range(int(input())):
#     print(prime_factorise(int(input())))

# K -
# sieve = [1] * int(1e6 + 10)
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)

# for _ in range(int(input())):
#     print(primes[int(input()) - 1])

# L -
# from bisect import bisect_right
# sieve = [1] * int(1e6 + 10)
# sieve[0] = 0
# sieve[1] = 0

# for i in range(2, len(sieve)):
#     if sieve[i]:
#         for j in range(i + i, len(sieve), i):
#             sieve[j] = 0

# primes = []
# for i, b in enumerate(sieve):
#     if b:
#         primes.append(i)

# px = [2]
# for prime in primes[1:]:
#     px.append(prime + px[-1])

# for _ in range(int(input())):
#     k = bisect_right(primes, int(input())) - 1
#     print(px[k])

# M -
# using namespace std;
# typedef long long ll;
# const int MAX_LIMIT = 1e4;
# const int MAX_SIEVE = 1e8;
# bool sieve[MAX_SIEVE] = {0};
# set<int> primes;

# int main() {
#   sieve[0] = 1;
#   sieve[1] = 1;
#   for (int i = 4; i < MAX_SIEVE; i += 2) {
#     sieve[i] = 1;
#   }

#   for (int i = 3; i < MAX_LIMIT; i += 2) {
#     if (sieve[i])
#       continue;
#     for (int j = i + i; j < MAX_SIEVE; j += i) {
#       sieve[j] = 1;
#     }
#   }

#   printf("2\n");
#   int prime_count = 1;
#   for (int i = 3; i < MAX_SIEVE; i += 2) {
#     if (sieve[i])
#       continue;
#     if (prime_count % 100 == 0) {
#       printf("%d\n", i);
#     }
#     prime_count++;
#   }

#   return 0;
# }

# N -
# import sys
# MAX_SIEVE = int(1e6 + 10)
# MAX_LIMIT = int(MAX_SIEVE // 2)
# sieve = [0] * MAX_SIEVE

# for i in range(4, MAX_SIEVE, 2):
#     sieve[i] += 1

# for i in range(3, MAX_LIMIT, 2):
#     if sieve[i]:
#         continue
#     for j in range(i + i, MAX_SIEVE, i):
#         sieve[j] += 1

# for i in range(2, MAX_SIEVE):
#     if sieve[i] == 0:
#         sieve[i] = 1


# ans = [[]]
# for n in range(1, 8):
#     temp = [0] * MAX_SIEVE
#     for j in range(1, MAX_SIEVE):
#         temp[j] = 1 if sieve[j] == n else 0
#         temp[j] += temp[j - 1]
#     ans.append(temp)

# lines = sys.stdin.readlines()

# for i, line in enumerate(lines[1:]):
#     if i:
#         sys.stdout.write("\n")
#     a, b, n = map(int, line.split())
#     if n == 0:
#         if a == 1:
#             sys.stdout.write("1")
#         else:
#             sys.stdout.write("0")
#     elif n > 7:
#         sys.stdout.write("0")
#     else:
#         sys.stdout.write(f"{ans[n][b] - ans[n][a - 1]}")

# O -
# using namespace std;
# typedef long long ll;
# const int MAX_SIEVE = 3e7 + 2e6;
# const int MAX_LIMIT = sqrt(MAX_SIEVE);
# int sieve[MAX_SIEVE];
# vector<int> primes;

# int main() {
#   memset(sieve, 0, MAX_SIEVE);
#   sieve[0] = 1;
#   sieve[1] = 1;

#   for (int i = 4; i < MAX_SIEVE; i += 2) {
#     sieve[i] = 1;
#   }


#   for (int i = 3; i < MAX_LIMIT; i += 2) {
#     if (sieve[i])
#       continue;

#     for (int j = i + i; j < MAX_SIEVE; j += i) {
#       sieve[j] = 1;
#     }
#   }

#   primes.push_back(2);
#   for (int i = 3; i < MAX_SIEVE; i += 2) {
#     if (sieve[i])
#       continue;
#     primes.push_back(i);
#   }

#   ll n = 0;

#   while (true) {
#     cin >> n;
#     int limit = sqrt(n);
#     if (n == 0)
#       break;
#     map<ll, int> factors;
#     for (int prime : primes) {
#       if (prime > limit)
#         break;
#       while (n % prime == 0) {
#         factors[prime]++;
#         n /= prime;
#       }
#     }

#     if (n != 1)
#       factors[n]++;

#     for (auto it = factors.begin(); it != factors.end(); it++) {
#       printf("%lld^%d ", it->first, it->second);
#     }
#     printf("\n");
#   }

#   return 0;
# }

# P -
# from typing import Counter
# import sys


# MAX_SIEVE = int(1e6 + 10)
# MAX_LIMIT = int(MAX_SIEVE**.5)
# sieve = [True] * MAX_SIEVE
# sieve[0] = False
# sieve[1] = False

# primes = []
# factors = Counter()


# for i in range(4, MAX_SIEVE, 2):
#     sieve[i] = False

# primes.append(2)
# for i in range(3, MAX_LIMIT, 2):
#     if sieve[i]:
#         primes.append(i)
#         for j in range(i + i, MAX_SIEVE, i):
#             sieve[j] = False


# def prime_factorise(n):
#     global primes, sieve, factors
#     if sieve[n]:
#         factors[n] += 1
#         return

#     limit = int(n**.5)
#     for prime in primes:
#         if prime > limit:
#             break
#         while n % prime == 0:
#             factors[prime] += 1
#             n //= prime

#     if n != 1:
#         factors[n] += 1

#     return


# lines = sys.stdin.readlines()
# for i in range(1, len(lines), 2):
#     factors = Counter()
#     n = int(lines[i])
#     xs = map(int, lines[i + 1].split())
#     for x in xs:
#         prime_factorise(x)
#     if all([factor_amount % n == 0 for factor_amount in factors.values()]):
#         sys.stdout.write("YES\n")
#     else:
#         sys.stdout.write("NO\n")

# Q -
# import sys
# lines = sys.stdin.readlines()
# def get_factors(n):
#     factors = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             factors.add(i)
#             factors.add(n // i)
#     return factors


# for i in range(1, len(lines), 2):
#     n = int(lines[i])
#     xs = set(map(int, lines[i + 1].split()))
#     good = True
#     num = min(xs) * max(xs)
#     factors = get_factors(num)
#     if xs == factors:
#         sys.stdout.write(f"{num}\n")
#     else:
#         sys.stdout.write(f"-1\n")

# R -
import sys
from collections import Counter

MAX_SIEVE = int(1e7 + 100)
MAX_LIMIT = int(MAX_SIEVE**.5)

lines = sys.stdin.readlines()
n = int(lines[0])
counter_xs = [0] * MAX_SIEVE
for x in map(int, lines[1].split()):
    counter_xs[x] += 1
m = int(lines[2])
qs = lines[3:]

# n = len(range(2, int(1e6)))
# counter_xs = Counter(range(int(1e6), int(1e6 + 1e6)))


sieve = [1] * MAX_SIEVE
sieve[0] = 0
sieve[1] = 0


px = [0] * MAX_SIEVE

for i in range(2, MAX_SIEVE, 2):
    px[i] += counter_xs[i]

for i in range(3, MAX_LIMIT, 2):
    if sieve[i]:
        for j in range(i, MAX_SIEVE, i):
            px[i] += counter_xs[j]

            sieve[j] = 0


for i in range(1, MAX_SIEVE):
    px[i] += px[i - 1]


for q in qs:
    a, b = map(int, q.split())
    b = min(b, int(MAX_SIEVE - 1))
    if a > 1e7:
        sys.stdout.write(f"0\n")
    else:
        sys.stdout.write(f"{px[b] - px[a - 1]}\n")
