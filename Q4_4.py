def revert_compare(list):
    lis = []
    j = 0
    for i in range(len(list)):
        if i != 0:
            lis.append(list[i*-1])
    lis.append(list[0])

    for i in range(len(list)):
        if list[i] == lis[i]:
            j += 1

    if j == len(list):
        return True
    
    return False

print(revert_compare("arara"))
