a = float(input("Enter 1st number: "))
operation = input("Enter the operation: ")
b = float(input("Enter 2nd number: "))

if operation == '+':
  result = a + b
elif operation == '-':
  result = a - b
elif operation == '*':
  result = a * b
elif operation == '/':
  result = a / b
else:
  result = "Invalid operation"
# Print the result
print(f"The result of {a} {operation} {b} is: {result}")
