def eligible_for_vote():
    if age>=18:
        return ("you are eligible" )
    else:
        return ("not eligible")
age=int(input("enter a age: "))
print(eligible_for_vote())
