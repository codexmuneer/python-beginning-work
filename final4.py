'''3. Write a Python function to get unique values from a list. (DONOT use SETS)
Your function take list as a parameter.
Return a new_list having unique numbers.'''

def unique_list(x):
    new = []
    for i in x:
        if i not in new:
            new.append(i)
            
    
    return new


a = [1,2,3,2,4,5,1,2,3,6]
c = unique_list(a)
print(c)