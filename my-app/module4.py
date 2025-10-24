def input_integer(input_prompt="Enter an integer: "):
    while True:
        try:
            num = int(input(input_prompt))
            break 
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    return num


number = input_integer()
print(f"You entered: {number}")
number_array = []
for i in range(number):
    result = input_integer()
    print(f"Number {i + 1} is: {result}")
    number_array.append(result)

result = input_integer("Enter another integer to search: ")
if result in number_array:
    print(number_array.index(result) + 1)
else:
    print("-1")
