import dictionary

# choice1 = "y"
# while choice1 == "y":
#     choice1 = str(input("Homework 6 Menu\n(1) Get p distance matrix\n(2) Exit\nEnter 1 or 2: \n"))

#     if choice1 == "1": # the choice for the get_p_distance matrix function
#         print("Enter two DNA strings of 10 characters or less. \nYou must only enter the letters of the DNA strings with no spaces between them.\n")
#         list1 = []
#         continue_ = "y"
#         while continue_ == "y":
#             dna_string = str(input("Enter a DNA string using the format: XXXXXX\n"))
#             dna_list = list(dna_string)
#             list1.append(dna_list)
#             print("Do you wish to add an additional DNA string?")
#             continue_ = str(input("Enter y for yes or n for no: "))
#         print("You have entered: ")
#         for string in list1:
#             print(string)
#         print("The following is the p distance matrix for the entered strings: ")
#         p_distance_matrix = dictionary.get_p_distance_matrix(list1)
#         for row in p_distance_matrix:
#             for item in row:
#                 print(format(item, '8.3f'), end = '')
#             print('')

#     elif choice1 == "2": # the choice to exit the program
#         print("You have chosen exit.\n")
#         exit("Exiting...")

#     else:
#         print("Invalid entry...\nHomework 6 Menu\n(1) Get p distance matrix\n(2) Exit")
#         choice1 = str(input("Invalid entry...\nHomework 6 Menu\n(1) Get p distance matrix\n(2) Exit\nEnter 1 or 2: \n"))
#     choice1 = 'y'

# Dave helped me with this via GroupMe.

choice1 = 'y'
while choice1 == 'y':
    choice1 = str(input("Homework 7 Menu\n(1) Add or Update Item\n(2) Delete Item\n(3) Exit\n"))
    if choice1 == "1":
        print('Please add or update your widgets item.')
        widget_name = str(input('Enter name of item: '))
        widget_quantity = int(input('Enter quantity of item added to widgets (as a positive number) or subtracted from widgets (as a negative number): '))
        widgets = {}
        dictionary.add_inventory(widgets, widget_name, widget_quantity)

    elif choice1 == 2:
        widget_name = input("Enter name for the item to be deleted: ")
        dictionary.remove_inventory_widget(widgets, widget_name)

    elif choice1 == 3:
        exit("Exiting...")

    else:
        print("invalid entry")

    choice1 = str(input("Would you like to continue back to the menu? y for yes or n for no"))
    if choice1 == 'n':
        exit("Exiting...")
