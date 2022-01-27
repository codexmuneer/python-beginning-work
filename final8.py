'''two lists into dictionay'''
list1 = ["p218021","p218022","p218021"]
list2 = [100,20,30]
d = dict()

for i in range(3):
    a = list1[i]
    b = list2[i]
    d.update({a:b})

print(d)
    
