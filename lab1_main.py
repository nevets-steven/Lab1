print("Exercise 1.1 Echo String\n")
divider = '=' * 30 + '\n'
enter_text = input('Enter some text: ')
print(enter_text)
print(divider)

print("Exercise 1.2 Adding Number to Integer\n")
enter_num = input("Enter a number: ")
print(int(enter_num)+1)
print(divider)

print("Exercise 1.3 Adding a Number to Float\n")
float_num = input("Enter a number: ")
print(float(float_num)+0.5)
print(divider)

print("Exercise 1.4 Adding Two Floats\n")
enter_float = input("Enter a number: ")
enter_float_2 = input("Enter another number: ")
sum = float(enter_float) + float(enter_float_2)
print(f"The sum is {sum}")
print(divider)

print("Exercise 1.5 Multiplying Floats\n")
a = input("Enter a number: ")
b = input("Enter another number: ")
product = float(a) * float(b)
print("The product is {}".format(product))
print(divider)

print("Exercise 1.6 Dividing Integers\n")
x = input("Enter a number: ")
y = input("Enter another number: ")
divided = int(x) / int(y)
print(f"The result is {int(divided)}")
print(divider)

print("Exercise 1.7: Entering Booleans\n")
bool_val = input("Enter a boolean: ")
if (bool_val == "True"):
    opposite = False
elif (bool_val == "False"):
    opposite = True
print(f"You entered {bool_val}")
print(f'The opposite of what you entered is: {opposite}')
print(divider)