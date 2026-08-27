name = input("enter a name: ")
output = ""
for i in name:
    if output == "":
        output += i
    else:
        output += "-" + i
print(output)


variable = input("enter a string: ")
print(*variable, sep="-")