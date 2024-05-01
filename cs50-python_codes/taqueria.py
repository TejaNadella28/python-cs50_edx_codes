MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def display_total(items):
    total = sum(MENU[item] for item in items)
    return "${:.2f}".format(total)

def main():
    ordered_items = []
    print("Welcome to Felipe's Taqueria!")
    print("Menu:")
    for item in MENU:
        print("-", item)
    print("Please enter your order (press Ctrl-D to finish):")
    try:
        while True:
            user_input = input().strip().title()
            if user_input in MENU:
                ordered_items.append(user_input)
                print("Total:", display_total(ordered_items))
            else:
                print("Item not found in menu. Please try again.")
    except EOFError:
        print("Thank you for your order!")
        print("Total:", display_total(ordered_items))
main()
