import files


items = {}
choice1 = 'y'
while choice1 == 'y':
    choice2 = str(input("Homework 7 Menu\n(1) Write text into a file\n(2) Display text in file\n(3) Exit\n"))
    if choice2 == "1":
        file_name = str(input("Enter name of file: \n"))
        file_write = str(input("What would you like to write into this file?\n"))
        files.write_to_file(file_name, file_write)

    elif choice2 == "2":
        file_name = input("Enter file path (without quotes) of the file you wish to be displayed: \n")
        files.read_from_file(file_name)

    elif choice2 == "3":
        exit("Exiting...")

    else:
        print("invalid entry")

    choice3 = str(input("Would you like to continue back to the main menu? y for yes or n for no:\n"))
    if choice3 == 'n':
        exit("Exiting...")
