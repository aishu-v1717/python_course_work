s="hello"
h='world'
print(s)
print(h)
#concatination
result=s+h
print(result)
#repetation
print("hello!.."*7)
#indexing
str="aishwarya"
print(str[0])  # first character
print(("python\n"*3).strip())
text="python"
print(text[0])
print(text[1])
print(text[2])
print(text[-1])
print(text[-6])
#slicing
text="python"
print(text[0:4])
print(text[::])
print(text[::-1])
print(text[0::])
print(text[-5:-1])
#membership
print("pyt" in text)
print("pyt" not in text)
#built-in functions
print(len(text))
print(max(text))
print(min(text))
print(sorted(text))
print(chr(65))
print(ord("A"))
#case conversion
msg="hello"
msg.upper()
msg.lower()
msg.capitalize()
msg.swapcase()
msg="hi!...hello"
msg.title()
msg="PyTHon"
msg.swapcase()
msg="ß"
msg.casefold()
#alignment methods
msg="python course"
msg.center(20)
msg.center(20,"_")
msg.ljust(20,"-")
msg.rjust(20,"-")
str="1223"
print(str.zfill(10))
print("name:{},age:{}".format("tom",25))
name="aishu"
age=21
print(f"name:{name},age:{age}")
#search methods
msg="hello"
msg.find("o")
msg.find("a")#a is not present in msg
msg.rfind("o")
msg="aishwarya"
print(msg.rfind("a"))
msg.index("a")
msg.rindex("a")
msg.count("a")
#string methods
msg="python"
msg.startswith("py")
msg.endswith("th")
msg.isalpha()
msg.isalnum()
msg.islower()
msg.isupper()
" ".isspace()
"Hello World".istitle()
"python".isidentifier()
"123".isdigit()
"124.45".isdecimal()
"1/2".isnumeric()
#replace
"hello".replace("l","a")
"abcd".translate(str.maketrans("abc", "xyz"))
"python".maketrans("pyth","_3s%")
msg="hello"
msg.split()  # Default split by whitespace
msg.split(",")  # Split by comma    
msg.rsplit()
msg.splitlines()  # Split by line breaks
msg.join(["hello", "world"])  # Join with space
"ice cream".partition("-")
"ice cream".rpartition("-")
"hello".strip()
"hello".lstrip()
"hello".rstrip()
"hello".encode("utf-8")  # Encode to bytes
b"hello".decode("utf-8")  # Decode from bytes
