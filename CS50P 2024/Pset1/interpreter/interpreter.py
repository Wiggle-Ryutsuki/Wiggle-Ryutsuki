# Maimoona Aziz

# Get user input
expression = input("Expression: ")

# Split integers and operations
x, y, z = expression.split(" ")

# Convert into floats
x = float(x)
z = float(z)

# Calculate
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
