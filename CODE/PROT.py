#The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). 
#Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
#The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

#Return: The protein string encoded by s.

with open('RNA codon table.txt','r') as table:
    alphabet = dict(line.split() for line in table)
    print(alphabet)

def rna_decoder(rna):
    protein = ''
    for i in range(0,len(rna)-3,3): #Not computing the last codon (Stop)
        protein += alphabet[rna[i:i+3]]            
    return protein
                
rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
rna_decoder(rna)