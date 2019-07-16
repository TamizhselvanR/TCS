'''

Consider the following series:

1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187…

This series is a mixture of 2 series – all the odd terms in this series form a geometric series and all the e
ven terms form yet another geometric series.

Write a program to find the Nth term in the series.

'''
n = int(input())
if(n % 2 == 0):
    new = n / 2
    print(3 ** (new-1))
else:
    new = (n+1) / 2
    print(2 ** (new-1))