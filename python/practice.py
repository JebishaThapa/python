#write a python program to find the sum of natural numbers
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))
total_sum = 0
for i in range(lower, upper +1 ):
    total_sum+=i
print(total_sum)