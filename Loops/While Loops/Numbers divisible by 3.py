"""
● Read an integer X
● Print all numbers that are divisible by 3 from
1 to X.
○ These are 3, 6, 9, 12, 15, 18, ….. (multiple of 3)
"""
end = int(input())
num = 1

while num <= end:
    if num % 3 == 0:
        print(num)
    num += 1

