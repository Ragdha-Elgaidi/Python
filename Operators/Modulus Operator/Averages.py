"""
Write a program that reads 5 numbers and print the following:
○ A) Their average
○ B) The sum of the first 3 numbers divided by the sum of the last 2 numbers
○ C) The average of the first 3 numbers divided by the average of the last 2 numbers.
○ What is the math relation between B and C?
"""
a, b, c, d, e = map(float, input().split())

avg1 = (a + b + c + d + e) / 5.0 #A
sum = (a + b + c) / (d + e)      #B
first_avg = (a + b + c) / 3.0
last_avg = (e + d) / 2.0
avg2 = first_avg / last_avg      #C

print(avg1, sum, avg2)
print(sum * 2/3)
