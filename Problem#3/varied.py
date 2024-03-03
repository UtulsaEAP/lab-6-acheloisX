def process_input(input_string):
      # Split into separate strings
    numbers_as_strings = input_string.split()
    # Convert strings to floats
    numbers = [float(num_str) for num_str in numbers_as_strings if float(num_str) >= 0]

    # Get max and average
    max_value = max(numbers)
    average_value = sum(numbers)/len(numbers) if numbers else 0
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input()

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
