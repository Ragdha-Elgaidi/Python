num1, num2, num3 = map(float, input().split())

# just check if num less than all other choices one by one

if num1 <= num2 and num1 <= num3:
    print(num1)
elif num2 <= num1 and num2 <= num3:
    print(num2)
else:
    print(num3)

