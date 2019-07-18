'''


Input:

Hello
Good
Morning

Output:

H”ll”
*oo*
morning


'''


list = ['a','e','i','o','u']
for i in range(3):
    string = raw_input()
    for char in string:
        if(i == 0):
            if char in list:
                print('"'),
            else:
                print(char),
        elif(i == 1):
            if char in list:
                print(char),
            else:
                print('*'),
        else:
            print(char.lower()),
    print("")