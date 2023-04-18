n = int(input())
row = 1

while row <= n:
    start_count = 1

    while start_count <= row:
        print("*", end="")
        start_count +=1

    print()
    row += 1
