new = []
string = "The quick brown fox jumps over the lazy dog"
string = string.lower()
print(string)
for i in string:
    if i != " ":
        if i not in new:
            new.append(i)
if len(new) == 26:
    print("It is a panagram")
else:
    print("Its not a panagram")