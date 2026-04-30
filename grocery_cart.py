grocery_dict = {'product': [], 'price': [], 'quantity': []}
add_product = grocery_dict['product']
add_price = grocery_dict['price']
add_quantity = grocery_dict['quantity']

def exit_program():
    print("===============================")
    print("Thank you for shopping!")
    print("Exiting program...")
    print("===============================")
    exit()

def calculate_cost():
    print("===============================")
    print("PRINTING GROCERY LIST...\n")
    print(f"{'Item':<10}{'Price':^10}{'Quantity':^12}")
    for i in range(len(add_product)):
        print(f"{add_product[i]:<10}{add_price[i]:^10.2f}{add_quantity[i]:^12}")
    total_price = sum(add_price[i] * add_quantity[i] for i in range(len(add_price)))
    print(f"{'TOTAL COST:':<10}{total_price:^10.2f}")
    print("===============================")
    sub_main()

def print_list():
    print("===============================")
    if not add_product:
        print("There's nothing on the list...")
    else:
        print(f"{'Item':<10}{'Price':^10}{'Quantity':^12}")
        for i in range(len(add_product)):
            print(f"{add_product[i]:<10}{add_price[i]:^10.2f}{add_quantity[i]:^12}")
    print("===============================")
    sub_main()

def remove_item():
    print("===============================")
    print("REMOVE AN ITEM\n")
    remove_item = input("Item Name: ").strip()
    for i in range(len(add_product)):
        if add_product[i].lower() == remove_item.lower():
            add_product.pop(i)
            add_price.pop(i)
            add_quantity.pop(i)
            print(f"'{remove_item}' has been removed from the list.")
            break
    else:
        print(f"'{remove_item}' was not found in the list.")
    print("===============================")
    sub_main()

def add_item():
    print("===============================")
    print("ADD AN ITEM\n")
    while True:
        new_product = input("Name: ").strip()
        if new_product.lower() in (item.lower() for item in add_product):
            print("Item already in the list. Please enter a new item.")
        else:
            add_product.append(new_product.title())
            break
    while True:
        try:
            new_price = float(input("Price: "))
            if new_price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            add_price.append(new_price)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for price.")
    while True:
        try:
            new_quantity = int(input("Quantity: "))
            if new_quantity <= 0:
                print("Quantity must be greater than zero. Please enter a valid quantity.")
                continue
            add_quantity.append(new_quantity)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for quantity.")
    print(f"'{new_product}' has been added to the list.")
    print("===============================")
    sub_main()

def sub_main():
    print("===============================")
    print("What would you like to do?")
    print("1 - Add an Item")
    print("2 - Remove an Item")
    print("3 - Print Entire List")
    print("4 - Calculate Cost")
    print("5 - Exit Program")
    print("===============================")
    try:
        input_choice = int(input("Choice: "))
        if input_choice == 1:
            add_item()
        elif input_choice == 2:
            remove_item()
        elif input_choice == 3:
            print_list()
        elif input_choice == 4:
            calculate_cost()
        elif input_choice == 5:
            exit_program()
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
            sub_main()
    except ValueError:
        print("Invalid input. Please enter a number.")
        sub_main()

def main():
    print("===============================")
    print("MY NEW AND IMPROVED GROCERY LIST")
    print("===============================")
    sub_main()

main()