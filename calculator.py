def add_numbers(numbers):
    result = sum(numbers)
    return result


def subtract_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def divide_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero is not allowed."
        result /= num
    return result


def get_numbers():
    while True:
        try:
            count = int(input("How many integers do you want to enter? "))

            if count < 0:
                print("Only positive integer values are allowed.")
                continue

            if count < 2:
                print("This calculator only supports basic calculator functions as of now. Please enter at least 2 numbers to continue using the calculator.")
                continue

            numbers = []

            for i in range(count):
                num = int(input(f"Enter integer {i + 1}: "))

                if num < 0:
                    print("Only positive integer values are allowed.")
                    break

                numbers.append(num)

            else:
                return numbers

        except ValueError:
            print("Only positive integer values are allowed.")


def main():
    print("Welcome to the Calculator App")

    numbers = get_numbers()

    choice = input("Do you want to perform a specific function? (yes/no): ").strip().lower()

    if choice == "yes":
        function = input("Which function do you want? (add/subtract/multiply/divide): ").strip().lower()

        if function == "add":
            print("Add:", add_numbers(numbers))
        elif function == "subtract":
            print("Subtract:", subtract_numbers(numbers))
        elif function == "multiply":
            print("Multiply:", multiply_numbers(numbers))
        elif function == "divide":
            print("Divide:", divide_numbers(numbers))
        else:
            print("Invalid function selected.")

    elif choice == "no":
        print("Add:", add_numbers(numbers))
        print("Subtract:", subtract_numbers(numbers))
        print("Multiply:", multiply_numbers(numbers))
        print("Divide:", divide_numbers(numbers))

    else:
        print("Invalid choice. Please enter yes or no.")


if __name__ == "__main__":
    main()