class NumberStorage:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def input_integer(self, input_prompt="Enter an integer: "):
        while True:
            try:
                num = int(input(input_prompt))
                break 
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        return num

    def search(self, number):
        if number in self.numbers:
            print(f"The index for {number} is: {self.numbers.index(number) + 1}")
        else:
            print("-1")

    def get_numbers(self):
        for num in self.numbers:
            print(num)




number_storage = NumberStorage()

number = number_storage.input_integer()
print(f"You entered: {number}")
for i in range(number):
    result = number_storage.input_integer()
    number_storage.insert_number(result)
    print(f"Number {i + 1} is: {result}")


result = number_storage.input_integer("Enter another integer to search: ")
number_storage.search(result)
