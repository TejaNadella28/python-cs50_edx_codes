def main():
    user_input = input("Greeting: ")
    balance = check_balance(user_input)
    print(f"${balance}")

def check_balance(input_str):
    if "How you doing?" in input_str:
        return 20
    elif "What's happening?" in input_str:
        return 100
    elif "What's up?" in input_str:
        return 100
    else:
        return 0

if __name__ == "__main__":
    main()
