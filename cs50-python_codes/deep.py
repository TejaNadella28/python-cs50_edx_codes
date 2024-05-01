def main():
    user_input = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    if is_forty_two(user_input) or is_number_42(user_input):
        print("Yes")
    else:
        print("No")

def is_forty_two(input_str):
    return input_str.lower() == "forty two" or input_str.lower() == "forty-two"

def is_number_42(input_str):
    try:
        number = int(input_str)
        return number == 42
    except ValueError:
        return False

if __name__ == "__main__":
    main()
