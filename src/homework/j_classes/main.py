import class_a
def menu():
    print("(1) Roll die\n(2) Exit")
    menu_choice = 0
    while menu_choice != "2":
        menu_choice = input("Please enter menu option: ")

        if menu_choice == "1":
            pass
        elif menu_choice == "2":
            exit()

menu()