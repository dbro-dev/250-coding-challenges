import itertools
     
list1 = [1, 2, 3]
list2 = [4, 5]
     
result = list(itertools.chain(list1, list2))
     
print(result)