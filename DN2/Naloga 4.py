for i in range(2,50):
    flag = 0
    for j in range(2,int(i/2+1)):
        if(i % j == 0):
            flag = 1
    if flag == 0:
        print(i)