list_1  = [38,52,74,89,91,8,6,8,9,4]
sorted_list = []
while len(list_1) > 0:
    min = list_1[0]
    for i in range(0,len(list_1)):
        if min > list_1[i]:
            min = list_1[i]
        
    sorted_list.append(min) #записываем в новый список min
    list_1.remove(min) # удаляем min из старого списка

print(list_1)
print(sorted_list)
