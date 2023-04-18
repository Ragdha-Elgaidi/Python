T = int(input()) # test cases count

# Outer loop: iterate T times for T test cases

while T > 0:
    num = int(input())
    sum = 0
    start = 1

    # Inner loop: sum from 1 to N
    while start <= num:
        sum += start
        start += 1

    T -= 1
    print("Sum from 1 to ", num, '=', sum)
