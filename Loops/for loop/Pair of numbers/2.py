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
    j = sum - i      # i + j == sum

    if 1 <= j <= m:    # make sure valid pos
        cnt += 1

print(cnt)
