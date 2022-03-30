import strings
dna1 = 0
dna2 = 0
dna = 0
choice1 = 'y'
while choice1 != '3':
    choice1 = str(input("1-Hamming Distance \n 2-Dna Complement \n 3-Exit \n"))
    if choice1 == '1':
        dna1 = str(input('enter dna1: '))
        dna2 = str(input('enter dna2: '))
        strings.get_hamming_distance(dna1, dna2)
    elif choice1 == '2':
        strings.get_dna_complement(dna)
    elif choice1 == '3':
        exit("Exiting...")
    else:
        print("Error")
        choice1 = str(input("1-Hamming Distance \n 2-Dna Complement \n 3-Exit \n"))