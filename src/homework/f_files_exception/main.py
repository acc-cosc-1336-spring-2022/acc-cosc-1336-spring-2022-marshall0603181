import files

items = {}
choice1 = 'y'
while choice1 == 'y':
    choice2 = str(input("Homework 7 Menu\n(1) Write text into a file\n(2) Display text in file\n(3) Exit\n"))
    if choice2 == "1":
        try:
            valid_file_path_example = "C:/Folder/Folder/file.txt"
            print(valid_file_path_example)
            file_name = str(input("Enter file path without quotes: \n"))
            while file_name == '':
                file_name = str(input("Enter file path without quotes: \n"))
            file_write = str(input("What would you like to write into this file?\n"))
        except:
            if '"' in file_name:
                file_name.strip()
            elif "'" in file_name:
                file_name.strip()
            files.edit_file(file_name, file_write)
    
    elif choice2 == "2":
        try:
            file_name = str(input("Enter file path without quotes: \n"))
            while file_name == '':
                file_name = str(input("Enter file path without quotes: \n"))
            files.read_from_file(file_name)
        except:
            if '"' in file_name:
                file_name.strip()
            elif "'" in file_name:
                file_name.strip()
            files.read_from_file(file_name)

    elif choice2 == "3":
        exit("Exiting...")

    else:
        print("invalid entry")

    choice1 = str(input("Would you like to navigate back to the main menu? y for yes or n for no:\n"))
    if choice1 == 'n':
        exit("Exiting...")
