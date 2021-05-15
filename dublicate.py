list_1=["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
i=0
new_list=[]
while i<len(list_1):
    if list_1[i]  in new_list:
        new_list.append(list_1)
        print(new_list)
        break
        i+=1