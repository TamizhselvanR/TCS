lis = [4,7,8,12,45,78,99]
l = 0
val = 99
u = len(lis) - 1
while(l <= u):
    mid = (l+u)//2
    if(lis[mid] == val):
        pos = mid
        break
    else:
        if(val < lis[mid]):
            u = mid - 1
        else:
            l = mid + 1
print(pos)