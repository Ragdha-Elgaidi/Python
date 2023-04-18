"""
Read an integer and print if it has 1, 2, 3, 4 or 5+ digits
"""
num = int(input())

if num < 10:
    print("1 digit")
elif num < 100:
    print("2 digits")
elif num < 1000:
    print("3 digits")
elif num < 10000:
    print("4 digits")
else:
    print("5+ digits")
