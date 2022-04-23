import files

choice1 = 'y'
while choice1 == 'y':
    choice2 = str(input("Homework 7 Menu\n(1) Write text into a file\n(2) Display text in file\n(3) Delete a file (possible bonus points)\n(4) Exit\n"))
    if choice2 == "1":
        try:
            file_name = str(input("Enter file path without quotes: \n"))
            while file_name == '':
                file_name = str(input("Enter file path without quotes: \n"))
            file_write = str(input("What would you like to write into this file?\n"))
            files.edit_file(file_name, file_write)
        except:
            file_name.strip('"')

    elif choice2 == "2":
        try:
            file_name = str(input("Enter file path without quotes: \n"))
            while file_name == '':
                file_name = str(input("Enter file path without quotes: \n"))
            files.read_from_file(file_name)
        except:
            file_name.strip('"')
  
    elif choice2 == "3":
        try:
            file_name = str(input("Enter file path without quotes: \n"))
            while file_name == '':
                file_name = str(input("Enter file path without quotes: \n"))
            files.delete_file(file_name)
        except:
            file_name.strip('"')

    elif choice2 == "4":
        exit("Exiting...")

    else:
        print("Invalid entry")

    choice1 = str(input("Back to Main Menu?\ny for yes or n for no:\n"))
    if choice1 == 'n':
        exit("Exiting...")


