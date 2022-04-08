import dictionary
from dictionary import list1
choice = "y"

while choice == "y":
    choice = str(input("(1) Get p distance matrix \n (2) Exit"))
    if choice == "1":
        print(dictionary.get_p_distance_matrix(list1))
    elif choice == "2":
        exit("Exiting...")
    else:
        choice = str(input("Error... \n Please enter a valid choice between: \n (1) Get p distance matrix \n (2) Exit"))

