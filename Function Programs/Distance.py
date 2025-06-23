import math

# Read input values
x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

# Calculate Euclidean distance using math.pow and math.sqrt
distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# Print the result
print(f"Distance from (0,0) to ({x},{y}) is: {distance}")
