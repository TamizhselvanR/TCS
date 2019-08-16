from collections import Counter
a = 'aaabbbddcccc'
max = 0
for i,j in Counter(a).items():
    if(j > max):
        max = j
        big = i
print(big,max)

