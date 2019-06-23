if __name__ == '__main__':
    a = 12
    b = 3
    flag = 0
    for i in range(2,min(a,b)+1):
        if(a % i == 0 and b % i == 0):
            result = i
            flag = 1
            break
    if(flag != 1):
        result  = 1
    print(result)