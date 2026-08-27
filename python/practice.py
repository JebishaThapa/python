name = input("enter a name: ")
output = ""
for index in name, enumerate(name):
    
    if index!= len(name)[-1]:
        output += index + "-"
    else:
        output == index + ""
print(output)