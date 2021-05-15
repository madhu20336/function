def numbers(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    else:
        return num3
number1=int(input("enter the number: "))
number2=int(input("enter the number: "))
number3=int(input("enter the number: "))
print(numbers(number1,number2,number3))