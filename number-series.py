'''

Consider the following series:

0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8

This series is a mixture of 2 series all the odd terms in this series form even numbers
in ascending order and every even term is derived from the previous term using the formula (x/2).

'''

n = int(input())
if(n % 2 == 0):
    new = n / 2
    print(new - 1)
else:
    new = (n+1) / 2
    print(2 * (new-1))