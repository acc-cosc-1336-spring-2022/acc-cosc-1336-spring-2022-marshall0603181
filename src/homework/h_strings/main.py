import strings
choice1 = str(input("1-Hamming Distance \n 2-Dna Complement \n 3-Exit \n"))
while choice1 != "3":
    choice1 = str(input("1-Hamming Distance \n 2-Dna Complement \n 3-Exit \n"))
    if choice1 == 1:
        strings.get_hamming_distance()
    elif choice1 == 2:
        strings.get_dna_complement()
    elif choice1 == 3:
        exit("Exiting...")
    else:
        print("Error")
        choice1 = str(input("1-Hamming Distance \n 2-Dna Complement \n 3-Exit \n"))