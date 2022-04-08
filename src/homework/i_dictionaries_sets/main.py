import dictionary
from dictionary import list1

choice = ""

while choice != "2":
    choice = str(input("(1) Get p distance matrix \n(2) Exit \nEnter choice here: "))
    if choice == "1":
        list1 = str(input("Please enter list: "))
        print(dictionary.get_p_distance_matrix(list1))
    elif choice == "2":
        exit("Exiting...")
    else:
        choice = str(input("Error... \nPlease enter a valid choice between: \n(1) Get p distance matrix \n(2) Exit \nEnter choice here: "))
