def show_number(limit):
    a=1
    while a<=number:
        if a%2==0:
            print(a,"even")
        else:
            print(a,"odd")
        a+=1
   
number=int(input("enter a number: "))
show_number(number)