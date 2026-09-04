
"""
Input: [1,2,3,1]
Output: True

Input: [3,4]
Output: False

Input: [4,3,2,3]
Output: True
"""

def repitition(num):
    storage=set()
    for i in num:
        if i in storage:
            return True
        storage.add(i)
    else: 
        return(False)

testnums = [2, 7, 11, 7]

result = repitition(testnums)
print(result)

"""
def repitition(num):
       return len(num) != len(set(num)
"""