my_set={}
print(my_set)
my_set={1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))
my_set={1, 2, 3, 4, 5, 6}
print(my_set)
print(1 in my_set)  # membership
print(6 not in my_set)  # membership
print(len(my_set))  # length of set
print(max(my_set))  # maximum element
print(min(my_set))  # minimum element
print(sorted(my_set))  # sorted set
print(sum(my_set))  # sum of elements
print(my_set.union({7, 8, 9}))  # union with another set
print(my_set.intersection({3, 4, 5}))  # intersection with another set
print(my_set.difference({2, 3}))  # difference with another set
print(my_set.symmetric_difference({4, 5, 6}))  # symmetric difference with another set
print(my_set.add(10))  # add an element
print(my_set.remove(1))  # remove an element
print(my_set.discard(2))  # discard an element
print(my_set.pop())  # remove and return an arbitrary element
print(my_set.clear())  # clear the set
print(my_set)  # print the modified set
print(my_set.copy())  # copy the set
print(my_set == {1, 2, 3, 4, 5, 6})  # equality check
print(my_set != {1, 2, 3})  # inequality check