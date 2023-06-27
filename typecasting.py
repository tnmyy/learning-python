# Typecasting in Python


a = "6"
b = "9"
print(a + b)

c = "Tanmay "
d = "Upreti"
print(c + d)

# String to Number

print(int(a) + int(b))
# print(int(a) + int(c))  # Invalid

# Number to String

e = 6
f = 9
print(str(e) + str(f))


# Explicit TypeCasting (Mene kaha to typeCasting hogi wrna nhi)

print(int(a) + int(b))

# Implicit TypeCasting (Python Devta na apne aap meri help kr di)

g = 6  # Number
print(type(g))

h = 0.9  # Float
print(type(h))

print(g + h)  # Float
print(type(g + h))  # Float
