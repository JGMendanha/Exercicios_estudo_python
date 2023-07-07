def reverter(list):
    lis = []
    for i in range(len(list)):
        if i != 0:
            lis.append(list[i*-1])
    lis.append(list[0])
    return lis

print(reverter("Python"))