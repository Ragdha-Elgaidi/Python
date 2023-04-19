"""
● Read T for number of test cases.
● For each test case read integer N.
● Then read N integers a, b, c, ….. On seperate lines
● Compute the sum of:
○ (a, b*b, c*c*c, d*d*d*d, e*e*e*e*e……)
○ That is the k-th number is repeated k times
"""
total_cases = int(input())

for case in range(total_cases):
    N, sum = int(input()), 0

    for pos in range(N):
        value, result = int(input()), 1

        # Loop to compute the sum: a, b*b, c*c*c
        for it in range(pos + 1):
            result *= value

        sum += result

    print('Sum is', sum)
