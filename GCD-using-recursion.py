def gcd(a,b):
    rem = a%b
    if(rem == 0):
        return b
    else:
        return gcd(b,rem)

if __name__ == '__main__':
    a = 21
    b = 6
    print(gcd(a,b))