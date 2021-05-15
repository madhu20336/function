# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# sum(4,5)

# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)



# function multi(a,b):
#     multiply=a*b
#     return multiply
# print(multi(3,4)) 

# def multi(a,b):
#     multiply=a*b
#     return multiply
# print(multi(3,4)) 

# Def Avg(number1,number2,number3):
#     avg=number1+number2+number3/3
#     print(sum)
# Avg(1,3,2)
 

# def Avg(number1,number2,number3):
#     avg=(number1+number2+number3)//3
#     return(avg)
# print(Avg(10,10,10))
 

# def voter(age):
# if age < 18:
#     print("eligible")
# else:
#     print("not eligible")
#     voter(20)
 

# def voter(age):
#     if age < 18:
#         print("eligible")
#     else:
#         print("not eligible")
# age1=int(input("enter a age: "))
# voter(age1)
 
#  def distance(kms):
#         if kms < 20:
#             print("close")
#         elif kms < 50:
#             print(median)
#         else:
#             Print(far)
#     distance(20,30) 


# def distance(kms):
#     if kms < 20:
#         print("close")
#     elif kms < 50:
#         print("median")
#     else:
#         print("far")
# distance1=int(input("enter a kms: "))
# distance(distance1) 


def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    if item > 20:
      list.remove(item)
    else:
      counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", num_list)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)