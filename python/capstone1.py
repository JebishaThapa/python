name = input("enter name: ")

max_length = max(len(name))
padding = 4
print("PERSONAL INTRODUCTION CARD".center(50, "-"))
print("^"*max_length* "^"*max_length)
print(f"|", "name: {name}"   )
print("^"* max_length)