"""Input: "jebisha"
Output:

jeb
"""
name = input("Enter a name: ")
for i in name:
    if i == name[-1]:
        print(i, end="")
    else: 
        print(i, end="-")



