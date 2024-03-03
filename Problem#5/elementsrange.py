def filter_and_print_range(input_list, min_val, max_val):
    input_numbers = [int(num) for num in input_list]
    filtered_numbers = [num for num in input_numbers if min_val <= num <= max_val]
    for num in filtered_numbers:
        print(num, end=',')

if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split()

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    min_val, max_val =  map(int, user_input.split())

    # Call the function to filter and print the numbers in the given range
    filter_and_print_range(integer_list, min_val, max_val)
