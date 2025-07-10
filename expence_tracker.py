print("Welcome to the Daily Expence Tracker!")
print("\nMenu:")
print("1. Add a new expence")
print("2. View all expence")
print("3. Calculate total and average expense")
print("4. Clear all expense")
print("5. Exit")

expence_list = []

while True:
    choice = input("Make your choice: ")

    if choice == "5":
        print("Exiting the Daily Expence Tracker. Goodbye!")
        break
    elif choice == "1":
        expence = float(input("Add your expence: "))
        expence_list.append(expence)
        print("Expence added successfully")
    elif choice == "2":
        if len(expence_list) == 0:
            print("No expence recorded yet.")
        else:
            print("Your expences:")
            for i in range(len(expence_list)):
                print(f"{i+1}. {expence_list[i]}")
    elif choice == "3":
        if len(expence_list) == 0:
            print("No expences recorded yet")
        else:
            total = sum(expence_list)
            average = sum(expence_list) / len(expence_list)
            print(f"Total expence: {total}")
            print(f"Average expence: {average}")
    elif choice == "4":
        ask = input("Are you sure You want to CLEAR all expence(Yes/No): ").lower()
        if ask == "Yes":
            expence_list.clear()
            print("All expences cleared.")
        elif ask == "No":
            print("Thanks for conformition.")
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid choice. Please try again.")

