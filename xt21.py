def add(a,b):
    print(f"adding: {a} + {b}")
    return a+b

def subtract(a,b):
    print(f"sybtracting {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"multiplying: {a} * {b}")
    return a*b

def divide(a,b):
    print(f"dividing: {a} / {b}")
    return a/b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Wight: {weight}, Iq: {iq}")

#A puzzle for the extra credit,type it in anyway.
print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes: ",what,"\nCan you do it by hand?")