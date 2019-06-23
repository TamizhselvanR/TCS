def fibo(i):
    if(i <= 1):
        return i
    else:
        return (fibo(i-1) + fibo(i-2))
if __name__ == '__main__':
    a = 17
    for i in range(a):
        print fibo(i)