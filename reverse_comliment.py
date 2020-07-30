#!/usr/bin/env python3

# Taking DNA input
right_dna = False
while right_dna == False:
    dna_input = input("Enter DNA sequence or RNA sequence: ")

    # Converting DNA in uppercase.
    dna = dna_input.upper()
    # Checking for wrong input.
    nt_abbreviations = [ "A", "T", "G", "C", "U", "Y", "R", "S", "W", "M", "K", "B", "D", "H", "V", "N"]
    for nt in dna:
        if nt not in nt_abbreviations:
            print("Wrong input, Please enter again.")
            break
        else:
            right_dna = True

# Making a list out of nucleotides in dna_list.
# Definig DNA list.
dna_list = []
for nt in dna:
    dna_list.append(nt)

# Reverse
def reverse(dna_list):
    reverse_list = dna_list[::-1]
    reverse_dna = "".join(str(nt) for nt in reverse_list)
    return reverse_dna


# Complement
def complement(dna_list):
    complement_list = []
    for nt in dna_list:
        if nt == "A":
            complement_list.append("T")
        elif nt == "T":
            complement_list.append("A")
        elif nt == "U":
            complement_list.append("A")
        elif nt == "G":
            complement_list.append("C")
        elif nt == "C":
            complement_list.append("G")
        elif nt == "Y":
            complement_list.append("R")
        elif nt == "R":
            complement_list.append("Y")
        elif nt == "S":
            complement_list.append("S")
        elif nt == "W":
            complement_list.append("W")
        elif nt == "K":
            complement_list.append("M")
        elif nt == "M":
            complement_list.append("K")
        elif nt == "B":
            complement_list.append("V")
        elif nt == "D":
            complement_list.append("H")
        elif nt == "H":
            complement_list.append("D")
        elif nt == "V":
            complement_list.append("B")
        elif nt == "N":
            complement_list.append("N")

        complement_dna = "".join(nt for nt in complement_list)
    return complement_dna


# Reverse-Compliment
def reverse_complement(dna_list):
    rev_comp_list = []
    temp = complement(dna_list)
    rev_comp_list = reverse(temp)
    rev_comp = "".join(nt for nt in rev_comp_list)
    return rev_comp


# Driver code
print("{:>} {:<}".format("Reverse:", reverse(dna_list)))
print("{:>} {:<}".format("Complement:", complement(dna_list)))
print("{:>} {:<}".format("Reverse-complement:", reverse_complement(dna_list)))
