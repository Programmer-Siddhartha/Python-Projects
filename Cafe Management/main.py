def display_menu():
    print("Welcome to the Cafe!")
    print("Here is the menu:")
    print("1. Coffee - $3")
    print("2. Tea - $2")
    print("3. Sandwich - $5")
    print("4. Quit")

def get_order():
    order = int(input("What would you like to buy? (1-4): "))
    return order

def process_order(order, total):
    if order == 1:
        total += 3
        print("You ordered a Coffee.")
    elif order == 2:
        total += 2
        print("You ordered a Tea.")
    elif order == 3:
        total += 5
        print("You ordered a Sandwich.")
    elif order == 4:
        print("Thank you for visiting the Cafe!")
    else:
        print("Invalid option. Please choose from the menu.")
    return total

def main():
    total = 0
    while True:
        display_menu()
        order = get_order()
        if order == 4:
            break
        total = process_order(order, total)
        print(f"Your current total is: ${total}")
    print(f"Your final total is: ${total}. Have a great day!")

if __name__ == "__main__":
    main()
def display_menu():
    print("Welcome to the Cafe!")
    print("Here is the menu:")
    print("1. Coffee - $3")
    print("2. Tea - $2")
    print("3. Sandwich - $5")
    print("4. Quit")

def get_order():
    order = int(input("What would you like to buy? (1-4): "))
    return order

def process_order(order, total):
    if order == 1:
        total += 3
        print("You ordered a Coffee.")
    elif order == 2:
        total += 2
        print("You ordered a Tea.")
    elif order == 3:
        total += 5
        print("You ordered a Sandwich.")
    elif order == 4:
        print("Thank you for visiting the Cafe!")
    else:
        print("Invalid option. Please choose from the menu.")
    return total

def main():
    total = 0
    while True:
        display_menu()
        order = get_order()
        if order == 4:
            break
        total = process_order(order, total)
        print(f"Your current total is: ${total}")
    print(f"Your final total is: ${total}. Have a great day!")

if __name__ == "__main__":
    main()
