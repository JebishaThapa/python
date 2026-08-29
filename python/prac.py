name = input("Enter your name: ")
output =""
for i in name:
    if i == name[-1]:
        output = output +  i + name[-1]
    else:
        output = output + i + name[-1] + "-"
        
print(output)

