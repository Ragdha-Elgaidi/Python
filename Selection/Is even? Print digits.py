"""
Read an integer N, then do the following
○ If the number is even: print the last digit of it
○ If the number is odd: do the following:
■ If number < 1000, print last 2 digits
■ If number >= 1000 and number < 1000000, print last 4 digits
■ Otherwise, print its negative value
"""
num = int(input())

if num % 2 == 0:
    print(num % 10)
else:
    if num < 1000:
        print(num % 100)
    elif 1000 <= num < 1000000:
        print(num % 10000)
    else:
        print(- num)
        
