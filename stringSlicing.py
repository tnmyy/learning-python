# String slicing and Operations on string

names = "Tanmay, Naman"

# Starting 6 letters
print(names[0:6])

# Length of a string
print(len(names))
print(len("Tanmay"))

# Slicing

# variable[0:4] = Including 0 but not 4
name = "Tanmay"
print(len(name))

print(name[0:3])
# OR
print(name[:3])

print(name[3:6])

print(name[0:6])
# OR
print(name[:])

print(name[0:-3])
# OR
print(name[0 : len(name) - 3])

print(name[-3:-2])  # => 3:4
