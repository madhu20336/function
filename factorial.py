def numbers(num):
    fact=1
    while num>0:
        fact=fact*num
        num-=1
    return (number,"factorial value is",fact)
number=int(input("enter the number: "))
print(numbers(number))