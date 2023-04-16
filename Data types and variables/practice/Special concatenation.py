"""
● Write a program that read 3 strings.
○ For simplicity let’s say input is 3 letters A, B and C
● The output is A’B”C repeated 10 times
○ A’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”C
● Input:
○ I
○ am
○ Mostafa
● Output:
○ I'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'a
m"MostafaI'am"MostafaI'am"Mostafa
"""

a, b, c = map(str, input().split())

combo = a + "'" + b + '"' + c
combo *= 10

print(combo)
