square_lambda=lambda n:n*n
print(square_lambda(5))
add_lambda=lambda x,y:x+y
print(add_lambda(3,4))
sub_lambda=lambda x,y:x-y
print(sub_lambda(10,4))
max_lambda=lambda x,y:x if x>y else y
print(max_lambda(10,20))
# with map
numbers=[1,2,3,4,5]
square=list(map(lambda x:x*x,numbers))
print(square)
