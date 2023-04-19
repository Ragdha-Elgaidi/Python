"""
● Read 3 integers N, M, SUM.
● Find total number of pairs that satisfy
A + B == SUM where
○ 1 <= A <= N
○ 1 <= B <= M
"""

n, m, sum = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    for j in range(1, m + 1):
        if i + j == sum:
            cnt += 1

print(cnt)
