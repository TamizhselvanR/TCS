'''

For Example, consider the given series:

1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, …

This series is a mixture of 2 series – all the odd terms in this series form a Fibonacci series and all the even terms
are the prime numbers in ascending order.

Now write a program to find the Nth term in this series.

'''
def primefn(n):
    new_term = n // 2
    count = 0
    for i in range(1, 1000):
        flag = 1
        if (i > 1):
            for j in range(2, i):
                if (i % j == 0):
                    flag = 0
                    break
            if (flag == 1):
                prime = i
                count += 1
            if (count == new_term):
                print(prime)
                break
def fibbo(n):
    new_term = (n+1) // 2
    t1 = 0
    t2 = 1
    for i in range(1, new_term + 1):
        next = t1 + t2
        t1 = t2
        t2 = next
    print(t1)
n = int(input())
if(n % 2 == 0):
    primefn(n)
else:
    fibbo(n)