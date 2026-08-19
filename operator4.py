# Arithmatic operator (+,-,*,/)
x=10
y=5
u=x+y
v=x-y
w=x*y
o=x/y
p=x%y
print("Addition: ",u)
print("Subtraction: ",v)
print("Multiplication: ",w)
print("Division: ",o)
print("Modulus: ",p)    

# Assignment operator (=+,-=,*=,/=)
a=10
print("Value of a: ",a)
a+=5 # a=a+5
print("Value of a: ",a)
a-=5 # a=a-5
print("Value of a: ",a)
a*=5 # a=a*5
print("Value of a: ",a)

# comparison operator (>=, <=, ==, !=)
x= int(input("Enter any Number: "))
print(x)
y= int(input("Enter any Number: "))
print(y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)

# logical operator (AND OR NOT)
x = int(input("Enter any number: "))
print(x>5 and x<5)
print(x>5 or x<5)

# Identity Operator
x=["mango","apple"]
y=["mango","apple"]
z=x
print("z: ",z)
print(x is y)
print(x is z)
print(x is not y)

# Membership Operator
x=["mango","apple"]
print("banana" in x)
print("mango" in x)

# Operator Precedence
x = (1+1)*2**4//3+4-1
print("x: ",x)