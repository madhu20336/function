def numbers(num):
    sum=0
    b=num
    length=len(str(num))
    while num>0:
        digit=num%10
        sum=sum+(digit**length)
        print(sum)
        number=number//10
if sum==num:
    print(num)
else:
    print(b,"is not armstrong number")
number=int(input("enter a number: "))
numbers(number)