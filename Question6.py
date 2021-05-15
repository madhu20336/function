# def calculator(num_x,num_y,add):
#     add_numbers=num_x+num_y
#     return (add_numbers)
# num1=int(input("enter a number: "))
# num2=int(input("enter a number: "))
# print(calculator(24,24,"add"))
# nauber_1=print
# def calculator(num_x,num_y,subtract):
#     add_numbers=num_x-num_y
#     return (add_numbers)
# print(calculator(90,23,"subtract"))
# number_4=print
# def calculator(num_x,num_y,multiply):
#     add_numbers=num_x*num_y
#     return (add_numbers)
# print(calculator(50,60,"multiply"))
# number_2=print
# def calculator(num_x,num_y,divide):
#     add_numbers=num_x/num_y
#     return (add_numbers)
# print(calculator(24,24,"divide"))
# number_3=print
# print(calculator(num1,num2,"add"))
# add_result=print
# print(calculator(num1,num2,"substract"))
# subtract_result=print
# print(calculator(num1,num2,"multiply"))
# multiply_result=print
# print(calculator(num1,num2,"divide"))
# divide_result=print





def change_list(a,b,multiply):
    i=0
    m=0
    lis =[]
    while i<len(a):
        m  = list1[i] * list2[i]
        lis.append(m)
        i+=1
    return lis
list1 =[5, 10, 50, 20]
list2 =[2, 20, 3, 5]
print(change_list(list1,list2,"multiply"))

