def check_palindrome(user_input):
    input_string = user_input.replace(" ", "").lower()
    if input_string == input_string[::-1]:
     print("palindrome: " + user_input)
    else: 
     print("not a palindrome: " + user_input)
if __name__ == "__main__":
        user_input = input()
        check_palindrome(user_input)
