pre_list = [4599, 3102, 1024, 9980, 2912, 1569, 4205, 9811, 1001, 7638, 4733, 1989, 5555, 5000, 3861]

def binary_search(pre_list, find_item):
    print("Binary Search")
    print("Searching...\n")
    pre_list.sort()
    start = 0
    end = len(pre_list) - 1
    found = False

    while start <= end and not found:
        midpoint = (start + end) // 2
        if find_item == pre_list[midpoint]:
            found = True
        elif find_item < pre_list[midpoint]:
            end = midpoint - 1
        else:
            start = midpoint + 1

    if found:
        print(f"The item {find_item} was found.\n")
    else:
        print(f"The item {find_item} was not found.\n")

def linear_search(pre_list, find_item):
    print("Linear Search")
    print("Searching...\n")
    if find_item in pre_list:
        print(f"The item {find_item} was found.\n")
    else:
        print(f"The item {find_item} was not found.\n")

def main():
    print("WELCOME TO OUR SHOP")
    print("--------------------")
    try:
        find_item = int(input("Find an item: "))
        linear_search(pre_list, find_item)
        binary_search(pre_list, find_item)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

main()