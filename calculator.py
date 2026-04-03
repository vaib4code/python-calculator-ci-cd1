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
    count = int(input("How many integers do you want to enter? "))
    numbers = []

    for i in range(count):
        num = int(input(f"Enter integer {i + 1}: "))
        numbers.append(num)

    return numbers


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