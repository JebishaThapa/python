"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

1. a list of numbers is given
2. let their be one variable that stores the required index if the target gets mathed we store it there
3. number deko hunxa target hunxa target bata kun kun number milera target baneko xa herxa ani tyo number ko index nikalney
4. target - nums?
5. target 5 xa 
[1,2,3,4]
 nums needs to be  5-1=4
 5-2=3
 5-3=2
 5-4=1
 now which which numbers become five
 if 4+3=5? if not is 4+2=5? no is 4 +1 = 5 yes? then return the index of 1 and 4

index how

nums = [1,2,3,4]
target = 7
target - i
7-3=4
7-4=3
4 and 3 are answer










"""

def twosums(nums, target):
    remaining={}
    for index, i in enumerate(nums):
        minus = target - i
        if minus in remaining:
            return(remaining[minus],index)
        remaining[i]=index
test_nums = [2, 7, 11, 15]
test_target = 9


result = twosums(test_nums, test_target)
print("The indices are:", result)





