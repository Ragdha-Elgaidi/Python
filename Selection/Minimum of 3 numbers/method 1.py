num1, num2, num3 = map(float, input().split())

if num1 < num2:  # Then either num1 or num3 is the answer
    if num1 < num3:
        print(num1)
    else:
        print(num3)

else:  # Then either num2 or num3 is the answer
    if num2 < num3:
        print(num2)
    else:
        print(num3)
