'''
**The Shopping List Maker**

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.  

Task 3: Add a function that prints out the entire list in a formatted way.
'''
# Initialize an empty shopping list
your_shopping_list = []

# Task 1: Function to add items to the list
def add_item(item):
    your_shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")
    
# Task 2: Function to remove items from the list
def remove_item(item):
    if item in your_shopping_list:
        your_shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in your inventory")

# Task 3: Function to print the entire list
def print_list():
    if your_shopping_list:
        print("\nYour Shopping List: ")
        index = 1 
        for item in your_shopping_list:
            print(f"{index}. {item}")
            index += 1
    else:
        print("Your Shopping List is empty")

# Main function to manage the shopping list
def shopping_list_manager():
    while True:
        print("\nShopping List Menu")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View your shopping list")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")  
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(item)
                
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(item) 
            
        elif choice == '3':
            print_list()
                
        elif choice == '4':
            print("Goodbye! ")
            break
            
        else:
            print("Invalid input. Choose 1, 2, 3, or 4.")
            
# Run the shopping list manager
shopping_list_manager()
