import strings
dna1 = 0
dna2 = 0
dna = 0
choice1 = ''
while choice1 != '3':
    choice1 = str(input("1-Hamming Distance \n 2-Dna Complement \n 3-Exit \n"))
    if choice1 == '1':
        dna1 = str(input('enter dna1 17 characters long: '))
        dna2 = str(input('enter dna2 17 characters long: '))
        print(strings.get_hamming_distance(dna1, dna2))
    elif choice1 == '2':
        dna = str(input('enter dna 10 characters long: '))
        print(strings.get_dna_complement(dna))
    elif choice1 == '3':
        exit("Exiting...")
    else:
        print("Error")
        choice1 = str(input("1-Hamming Distance \n 2-Dna Complement \n 3-Exit \n"))