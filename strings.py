# String in Python

name = "Tanmay"
homie1 = "Vaibhav"
homie2 = "Naman"

print("Hello," + name)

msg = """Me: Hello
Homie: Hi
Me: GYM aa ra h?
Homie: Na bhai
"""

print(name + " said to " + homie1 + "\n" + msg)


# Accessing Characters of a string

print(name[0])  # Index
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
# print(name[6])  # Index error


# Looping strings

# For loop

print("Using for loop on strings")

for character in homie1:
    print(character)
