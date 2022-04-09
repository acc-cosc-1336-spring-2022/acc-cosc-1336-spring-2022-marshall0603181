import dictionary

choice = "0"

while choice  != "2":
    choice = str(input("(1) Get p distance matrix \n(2) Exit \n"))
    if choice == "1":
        list1 = list(input("Please enter list: "))
        print(dictionary.get_p_distance_matrix(list1))
    elif choice == "2":
        exit("Exiting...")
    else:
        choice = str(input("Error...Please enter a valid choice: \n(1) Get p distance matrix \n(2) Exit \n"))
