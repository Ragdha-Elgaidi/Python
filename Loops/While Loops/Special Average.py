"""
● Read integer N, followed by reading N numbers
○ Each on separate lines
● Print 2 values
○ The average of the numbers in odd positions (1st, 3rd, 5th, …)
○ The average of the numbers in even positions (2nd, 4th, 6th, …)
● Explantation
○ (10+20+30)/3 = 20
○ (100+200+600)/3 = 300
"""
even_sum, odd_sum, even_count, odd_count = 0, 0, 0, 0
n = int(input())

cnt = 1
while cnt <= n:
    value = float(input())

    if cnt % 2 == 0:    # even position
        even_sum += value
        even_count += 1
    else:               # odd position
        odd_sum += value
        odd_count += 1

    cnt += 1

print(odd_sum / odd_count, even_sum / even_count)
