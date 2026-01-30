"""s1 = {1,2,3,4,'hi',1,2,3,'a'}
s1.add(10)
s1.update((5,3,5))
print(s1)
s1.remove(10)
s1.discard('hi')
s1.pop()
print(s1)"""
s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {10,9,8,7,6,5,4,3,2,1}
s3 =  {100}
print(s1.union(s2))  # can use "/"
print(s1.intersection(s2))  # can use "&" 
print(s1.difference(s2))   # can use "-"  we get the whole parts of a
print(s1.symmetric_difference(s2)) # we get the remaining parts of a which are not common to b
print(s1.issuperset(s2))
print(s2.issubset(s1))
print(s3.isdisjoint(s1))
print(s3.isdisjoint(s2))
print({1}.issubset(s1))
print(list({12,4,5}))