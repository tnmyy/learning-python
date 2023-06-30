# String Methods in Python

a = "!TaNmAy??????!!!!"
print(a)
print(len(a))

# To uppercase
print(a.upper())

# To lowercase
print(a.lower())

# To capitalize
print(a.capitalize())

# To remove specific characters from a string from end
print(a.rstrip("!?"))

# To replace a specific occurrence in string
print(a.replace("TaNmAy", "TNMY").rstrip("?!"))
print(a)  # Does not edits the original string

# To make a string item to list
b = "Tanmay ..... Tanmay ..... Tanmay"
print(b)
print(b.split("T"))
print(b.split(" "))

# To capitalize first character
c = "tANMAY"
print(c)
print(c.capitalize())

# To center
d = "Hey! My Name is Tanmay"
print(d)
print(len(d))
print((d.center(44, ".")))
print(len(d.center(44, ".")))

# To count how many times there's an occurrence of a word in string
print(b.count("Tanmay"))
print(b.count("."))

# To check wether a string is ending with a specific character
a = "!TaNmAy??????!!!!"
print(a.endswith("!"))
print(type(a.endswith("!")))
print(a.endswith("?"))

print(a.endswith("?", 3, 8))  # a[3:8]

# To find first  index of a specific character
print(a.find("a"))
print(a.find("t"))  # if not found, it returns -1

# To find first index of a specific character with error
print(a.index("a"))
# print(a.index("t"))  # Returns error

# To find is the string is alphaNumeric {A-Z, a-z, 0-9}
e = "Ab12_][]$#&"
print(e.isalnum())
e = "Ab12"
print(e.isalnum())

# To find is the string is Alpha {A-Z, a-z}
e = "Ab12_][]$#&"
print(e.isalpha())
e = "Ab"
print(e.isalpha())

# To find all characters are in lower case
f = "ABcd"
print(f.islower())
print(f.lower().islower())
