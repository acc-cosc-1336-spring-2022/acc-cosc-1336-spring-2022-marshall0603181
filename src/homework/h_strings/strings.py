from re import X
def reverse_string(string):
    rstr1 = ""
    indx = len(string)
    while indx > 0:
        rstr1 += string[ indx - 1]
        indx = indx - 1
    return rstr1

def list_to_string(s):
    str1 = ""
    for  ltr in s:
        str1 += ltr
    return str1

def get_hamming_distance(dna1, dna2):
    lt_dna1 = list(dna1)
    lt_dna2 = list(dna2)
    cnt = 0
    for i in range(17):
        if lt_dna1[i] != lt_dna2[i]:
            cnt += 1
    return cnt



def get_dna_complement(dna):
    reverse = reverse_string(dna)
    n_rvrs = list(reverse)
    for i in range(10):
        if n_rvrs[i] == "T":
            n_rvrs[i] = "A"
        elif n_rvrs[i] == "A":
            n_rvrs[i] = "T"
        elif n_rvrs[i] == "G":
            n_rvrs[i] = "C"
        elif n_rvrs[i] == "C":
            n_rvrs[i] = "G"
            i += 1

    n_rvrs1 = list_to_string(n_rvrs)

    return n_rvrs1
