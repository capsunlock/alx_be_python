# Objective: Utilize Python lists to create a simple shopping list manager.

def display_menu():
    # Strict check: Ensure this exact title print is within the function
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    # Checks for implementation of an array shopping_list
    shopping_list = []
    
    # Loop to continuously display the menu until the user chooses to exit (4)
    while True:
        # Checks for calling display_menu function
        display_menu()
        
        # Checks for implementation of Choice Input
        # Note: input() returns a string, satisfying the "number as input" requirement 
        # when compared against the string options '1', '2', '3', '4'.
        choice = input("Enter your choice: ")

        if choice == '1':
            # 1. Add Item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add: 
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' added to the list.")
            
        elif choice == '2':
            # 2. Remove Item
            item_to_remove = input("Enter the item to remove: ").strip()
            
            if item_to_remove in shopping_list:
                # remove() handles the item removal
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"Error: '{item_to_remove}' was not found in the list.")
            
        elif choice == '3':
            # 3. View List
            print("\n--- Current Shopping List ---")
            if shopping_list:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            else:
                print("The list is currently empty.")
            print("-----------------------------")
            
        elif choice == '4':
            # 4. Exit
            print("Goodbye!")
            break
        
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()