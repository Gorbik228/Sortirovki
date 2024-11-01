list_1 = [3,4,1,9,5,7,3]
stop_flag = True
while stop_flag is True:
    stop_flag = False
    for i in range (0,len(list_1)-1):
        if list_1[i] > list_1 [i+1]:
            change = list_1[i]
            list_1[i] = list_1[i+1]
            list_1[i+1] = change
            stop_flag = True
print(list_1)
        