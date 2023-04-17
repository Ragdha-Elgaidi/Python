"""
Write a program that reads 2 numbers a, b and divides them (a/b), but prints
only the fraction part
"""
a, b = map(float, input().split())
result1 = a / b
result2 = a // b
result = result1 - result2

print(result)
