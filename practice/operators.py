# ARTHEMATIC OPERATORS
a=10
b=20
print("Addition:", a + b)  
print("Subtraction:", a - b) 
print("Multiplication:", a * b)  
print("Division:", a / b)  
print("Floor Division:", a // b)    
print("Modulus:", a % b)  
print("Exponentiation:", a ** b)  
#COMPARISON OPERATORS
print("Equal to:", a == b)
print("Not equal to:", a != b)
print("Greater than:", a > b)   
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)
# ASSIGNMENT OPERATORS
a = 10
print("assign value:", a)
a += 5  # a = a + 5
print("Add and assign += :", a)
a -= 3  # a = a - 3
print("subtract and assign-= :", a)
a *= 2  # a = a * 2
print("multiply and assign *= :", a)
a /= 4  # a = a / 4
print("divide and assign /= :", a)
a //= 2 # a = a // 2
print("floor divide and assign //= :", a)   
a %= 3  # a = a % 3
print("modulus and assign %= :", a)
a **= 2 # a = a ** 2
print("exponentiation and assign **= :", a)     
#LOGICAL OPERATORS
X=10
Y=20
print("Logical AND:", X > 5 and Y < 30)
print("Logical OR:", X < 5 or Y > 15)
print("Logical NOT:", not(X > 5))
# MEMBERSHIP OPERATORS
GAMES=["cricket", "football", "hockey"]
print("Membership in list:", "cricket" in GAMES)
print("Membership not in list:", "tennis" not in GAMES)
#IDENTITY OPERATORS
x = [1, 2, 3]
y = X
print("Identity is:", x is y)  
print("Identity is not:", x is not y)  
# BITWISE OPERATORS(binary convertion)
a=6
b=3
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Bitwise Left Shift:", a << 2)
print("Bitwise Right Shift:", a >> 2)