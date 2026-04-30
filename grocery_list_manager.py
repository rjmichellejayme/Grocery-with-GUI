mommy_list = []

def exit_program():
    print("===============================")
    print("Terminating program...")
    exit()

def print_list():
    print("===============================")
    print("PRINTING LIST...\n")
    if not mommy_list:
        print("There's nothing on the list...")
    else:
        for i, item in enumerate(mommy_list, start=1):
            print(f"{i}. {item}")
    sub_main()

def remove_items():
    print("===============================")
    print("REMOVE AN ITEM\n")
    print("What would you like to remove?")
    remove_item = input("Item Name: ").strip()
    if not remove_item:
        print("Invalid input. Please enter a valid item name.")
    else:
        removed = False
        for i in mommy_list[:]:
            if i.lower() == remove_item.lower():
                mommy_list.remove(i)
                removed = True
        if removed:
            print(f"'{remove_item}' has been removed from the list.")
        else:
            print(f"'{remove_item}' was not found in the list.")
    sub_main()

def add_item():
    print("===============================")
    print("ADD AN ITEM\n")
    print("What would you like to add?")
    new_item = input("Item Name: ").strip()
    if not new_item:
        print("Invalid input. Please enter a valid item name.")
    elif new_item.lower() in (item.lower() for item in mommy_list):
        print(f"'{new_item}' is already in the list.")
    else:
        mommy_list.append(new_item)
        print(f"'{new_item}' has been added to the list.")
    sub_main()

def sub_main():
    print("===============================")
    print("What would you like to do?")
    print("1 _ Add an item")
    print("2 _ Remove an item")
    print("3 _ Print entire List")
    print("4 _ Exit program\n")
    try:
        input_choice = int(input("Choice: "))
        if input_choice == 1:
            add_item()
        elif input_choice == 2:
            remove_items()
        elif input_choice == 3:
            print_list()
        elif input_choice == 4:
            exit_program()
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
            sub_main()
    except ValueError:
        print("Invalid input. Please enter a number.")
        sub_main()

def main():
    print("   MY GROCERY LIST")
    sub_main()

main()