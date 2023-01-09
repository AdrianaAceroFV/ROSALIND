#Given: A protein string of length at most 1000 aa.

#Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
#(Don't neglect the importance of the stop codon in protein translation.)

bases = ['U', 'C', 'A', 'G']
codons = [a+b+c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

with open('rosalind_mrna.txt', 'r') as file:
    prot= file.read()

    number =1
    for i in prot:
        number *= amino_acids.count(i)
    print((number * amino_acids.count('*'))%1000000)
    