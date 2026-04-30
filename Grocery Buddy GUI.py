import tkinter as tk

window = tk.Tk()
window.geometry("600x800")
window.title("Grocery List Calculator")
window.configure(background="antiquewhite1")

grocery_list = {}

def add_item():
    try:
        item = item_name.get().strip()
        price = float(item_price.get())
        quantity = int(item_quantity.get())
        item_name.delete(0, "end")
        item_price.delete(0, "end")
        item_quantity.delete(0, "end")
        output.delete(1.0, tk.END)

        if item.upper() in (key.upper() for key in grocery_list.keys()):
            output.insert(tk.END, "Duplicate item detected. Please enter a unique item.\n")
        else:
            grocery_list[item] = [price, quantity]
            output.insert(tk.END, f"Added: {item} - Price: {price}, Quantity: {quantity}\n")
    except ValueError:
        item_name.delete(0, "end")
        item_price.delete(0, "end")
        item_quantity.delete(0, "end")
        output.insert(tk.END, "Invalid input. Please enter valid price and quantity.\n")

def remove_item():
    item = remove_entry.get().strip()
    remove_entry.delete(0, "end")
    output.delete(1.0, tk.END)

    for key in list(grocery_list.keys()):
        if key.upper() == item.upper():
            del grocery_list[key]
            output.insert(tk.END, f"Removed: {item}\n")
            return
    output.insert(tk.END, f"Item '{item}' not found in the list.\n")

def print_list():
    output.delete(1.0, tk.END)
    if not grocery_list:
        output.insert(tk.END, "The list is empty.\n")
    else:
        output.insert(tk.END, f"{'Item':<15}{'Price':<10}{'Quantity':<10}\n")
        for item, values in grocery_list.items():
            output.insert(tk.END, f"{item:<15}{values[0]:<10.2f}{values[1]:<10}\n")

def calculate_cost():
    output.delete(1.0, tk.END)
    if not grocery_list:
        output.insert(tk.END, "The list is empty.\n")
    else:
        total_cost = sum(price * quantity for price, quantity in grocery_list.values())
        output.insert(tk.END, f"{'Item':<15}{'Price':<10}{'Quantity':<10}\n")
        for item, values in grocery_list.items():
            output.insert(tk.END, f"{item:<15}{values[0]:<10.2f}{values[1]:<10}\n")
        output.insert(tk.END, f"\nTotal Cost: {total_cost:.2f}\n")

def exit_program():
    window.destroy()

tk.Label(window, text="Grocery List Calculator", font=("Arial", 18), bg="antiquewhite1").pack(pady=20)

tk.Label(window, text="Item Name:", font=("Arial", 12), bg="antiquewhite1").pack()
item_name = tk.Entry(window, width=30, bg="ivory2")
item_name.pack(pady=10)

tk.Label(window, text="Item Price:", font=("Arial", 12), bg="antiquewhite1").pack()
item_price = tk.Entry(window, width=30, bg="ivory2")
item_price.pack(pady=10)

tk.Label(window, text="Item Quantity:", font=("Arial", 12), bg="antiquewhite1").pack()
item_quantity = tk.Entry(window, width=30, bg="ivory2")
item_quantity.pack(pady=10)

tk.Button(window, text="Add Item", font=("Arial", 14), command=add_item).pack(pady=10)

tk.Label(window, text="Remove Item:", font=("Arial", 12), bg="antiquewhite1").pack()
remove_entry = tk.Entry(window, width=30, bg="ivory2")
remove_entry.pack(pady=10)
tk.Button(window, text="Remove Item", font=("Arial", 14), command=remove_item).pack(pady=10)

button_frame = tk.Frame(window)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

tk.Button(button_frame, text="Print List", font=("Arial", 14), command=print_list).grid(row=0, column=0, sticky=tk.W + tk.E)
tk.Button(button_frame, text="Calculate Cost", font=("Arial", 14), command=calculate_cost).grid(row=0, column=1, sticky=tk.W + tk.E)
tk.Button(button_frame, text="Exit", font=("Arial", 14), command=exit_program).grid(row=0, column=2, sticky=tk.W + tk.E)

button_frame.pack(pady=10)

tk.Label(window, text="Output:", font=("Arial", 14), bg="antiquewhite1").pack(pady=10)
output = tk.Text(window, font=("Arial", 14), bg="linen", height=15)
output.pack()

window.mainloop()