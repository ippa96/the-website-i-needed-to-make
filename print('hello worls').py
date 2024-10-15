numbers = []
operations = []
input_type = 'number'
ans = None  # Initialize ans to be used later

# Start the calculator loop
while True:
    if ans is not None:
        choice = input(f"Do you want to start with the previous result ([ans])? (y/n): ").lower()
        if choice == 'y':
            numbers.append(float(ans))
            input_type = 'operation'
        ans = None  # Reset ans after using it

    while True:
        if input_type == 'number':
            try:
                num = input("Enter a number: ")
                if num.lower() == 'd':
                    if len(operations) > 0:
                        operations.pop()
                        print("Last entry deleted. Please enter a new operation.")
                        input_type = 'operation'
                    else:
                        print("No numbers to delete.")
                    continue
                numbers.append(float(num))
                input_type = 'operation'
            except ValueError:
                print("Invalid input. Please try again.")

        elif input_type == 'operation':
            try:
                op = input("Enter an operation (+, -, *, /), or 'c' to calculate or 'd' to delete: ")
                if op.lower() == 'd':
                    if len(numbers) > 0:
                        numbers.pop()
                        print("The number of operations must be one less than the number of numbers.")
                        input_type = 'number'
                    else:
                        print("No operations to delete.")
                    continue
                if op.lower() == 'c':
                    if len(numbers) != len(operations) + 1:
                        print("The number of operations must be one less than the number of numbers.")
                        continue
                    break
                elif op in ('+', '-', '*', '/'):
                    operations.append(op)
                    input_type = 'number'
            except ValueError:
                print("Invalid input. Please try again.")

        else:
            print("Invalid Type")

    # Calculation section
    result = numbers[0]
    for i in range(len(operations)):  # Properly indent this line
        if operations[i] == '+':
            result += numbers[i + 1]
        elif operations[i] == '-':
            result -= numbers[i + 1]
        elif operations[i] == '*':
            result *= numbers[i + 1]
        elif operations[i] == '/':
            if numbers[i + 1] == 0:
                print("Cannot divide by zero.")
                break
            result /= numbers[i + 1]

    print("Result:", result)
    ans = result  # Store the result for the next loop