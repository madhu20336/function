#FIRST PART
# def Even_Number(numbers):
#     i=0
#     while i<numbers:
#         if numbers%2==0:
#             print(numbers,"is even number")
#             break
#         else:
#             print(numbers,"is not even number")
#             break
#         i+=0
# Even_Number(13)
# Even_Number(20)

#SECOND PART
# s="madhu"
# def fun():
#     s="shaz"
#     print(s)
# fun()
# print(s)

# city_name="delhi"
# def city():
#     city_name="mumbai"
#     print(city_name)
# city()
# print(city_name)

# def my_function(x):
#   return 5 * x

#print(my_function(3))
#print(my_function(5))
# print(my_function(9))
# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum
# #add_numbers_more(12,56)
# sum6 = add_numbers_more(100, 20) 


# def my_function(x):
#     return 5*x
# print(my_function(5))


# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname, lname):
#   print(fname + " "+ lname)

# my_function("Emil", "Refsnes")


# def my_function(**kid):
#     for kids in kid:
#         print("His last name is " + kids)

# my_function(fname = "Tobias", lname = "Refsnes")



# def my_function(*kids):
#     for kid in kids:
#         print("The youngest child is " + kid)

# my_function("Emil", "Tobias", "Linus")

# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry") 


 
# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     # print(number_sum)
#     return number_sum
# add_numbers(12,34)


# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum

# sum6 = add_numbers_more(100, 20) 
# print(sum6)



  
# def add(a, b): 
  
    # returning sum of a and b 
   # return a + b 
# c=3+5
# print(c)
# print(add(2,4))

# def my_function(name):
#     return(name)
# print(my_function("madhu"))



 
# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     return (number_sum)
# sum4 = add_numbers_print(4, 5)
# print (sum4)
# print (type(sum4)) 

# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     return ("Hello from NavGurukul ;)")
#     print(number_sum)
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum

# sum6 = add_numbers_more(100, 20) 
# print(sum6)
# # sum7=add_numbers_more(12,10)
# # print(sum7)

# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     print ("Kya main print ho payungi? :-(")

# # mon_menu = menu("monday")
# print (menu("monday"))
# # tues_menu = menu("tuesday")
# print (menu("tuesday"))
# # fri_menu = menu("friday")
# print (menu("saturday"))
# print(menu("sunday"))
# print(menu("wednesday")) 




# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print ("Kya main print ho payungi? :-(")
    
#     print ("Lekin main toh pakka nahi print hounga :'(")
#     return food
# print(menu("monday")) 
# print(menu("tuesday"))

# def foo():
#     y = "local"
#     print(y)


# foo()

x = 5

def foo():

    x = 10

    print("local x:",x)


foo()
print("global x:",x)
