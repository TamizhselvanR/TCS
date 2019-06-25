a = list(map(int, raw_input().strip('')))
product = 1;
for i in a:
    product *= i
print "The sum is ", sum(a)
print "The product is ", product
