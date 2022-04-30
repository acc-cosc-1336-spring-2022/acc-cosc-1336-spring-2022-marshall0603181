from class_a import die
def menu():
    menu_choice = 0
    while menu_choice != "2":
        print("(1) Roll die\n(2) Exit")
        menu_choice = input("Please enter menu option: ")
        

        if menu_choice == "1":
            die.__str__()
        elif menu_choice == "2":
            exit("Exiting...")

menu()