def lcm(a,b,maxi):
    if(maxi % a == 0 and maxi % b == 0):
        return maxi;
    maxi += 1
    return lcm(a,b,maxi)

if __name__ == '__main__':
    a = 22
    b = 6
    maxi = max(a,b)
    print(lcm(a,b,maxi)) 