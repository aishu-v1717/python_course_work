tup=()
print(tup)
tup=1,2,3
print(tup)
print(type(tup))
tup=(1,2,3,4,5)
print(tup)
print(tup[0])  # first element
print(tup[-1])
print(tup[1:3])  # slicing
print(tup[::2])  # every second element     
print(tup[::-1])  # reverse the tuple
print(2 in tup)  # membership
print(6 not in tup)  # membership       
print(tup.count(2))  # count occurrences of an element
print(tup.index(3))  # index of an element
# concatenation
tup2 = (6, 7, 8)
tup3 = tup + tup2
print(tup3)  # (1, 2, 3, 4, 5, 6, 7, 8)
# repetition
tup4 = tup * 2
print(tup4)  # (1, 2, 3, 4,
# 5, 1, 2, 3, 4, 5)
# unpacking
a, b, c, d, e = tup
print(a, b, c, d, e)  # 1 2 3 4 5
#tuple methods
print(tup.index(4))  # index of element 4
print(tup.count(2))  # count of element 2
#built-in functions
print(len(tup))  # length of tuple
print(max(tup))  # maximum element
print(min(tup))  # minimum element
print(sorted(tup))  # sorted tuple
print(sum(tup))  # sum of elements
print(tup[0:3])  # slicing
print(tup[::-1])  # reverse the tuple

