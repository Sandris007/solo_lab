# This function adds two numbers
def add(variable_1, y):
    return variable_1 + y

# This function subtracts two numbers
def subtract(variable_1, y):
    return variable_1 - y

# This function multiplies two numbers
def multiply(variable_1, y):
    return variable_1 * y

# This function divides two numbers
def divide(variable_1, y):
    return variable_1 / y


# Example usage of the calculator functions without user input
num_1 = 10
num_2 = 5

print(num_1, "+", num_2, "=", add(num_1, num_2))
print(num_1, "-", num_2, "=", subtract(num_1, num_2))
print(num_1, "*", num_2, "=", multiply(num_1, num_2))
print(num_1, "/", num_2, "=", divide(num_1, num_2))
