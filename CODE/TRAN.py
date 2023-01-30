#Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

#Return: The transition/transversion ratio R(s1,s2).

import Bio
from Bio import SeqIO

sequences = []
for records in SeqIO.parse("C:/Users/Usuario/Documents/GitHub/ROSALIND/CODE/rosalind_tran.txt","fasta"):
    sequences.append(str(records.seq))

s1 = sequences[0]
s2 = sequences[1]


def ratio(a, b):
    n = len(b)
    transversions = 0.0
    transitions = 0.0
    for i in range(n):
        if ((a[i] == 'A' and b[i]=='G') or (a[i] == 'G' and b[i]=='A') or (a[i] == 'C' and b[i]=='T') or (a[i] == 'T' and b[i]=='C')) :
            transitions +=1
        elif (a[i] == 'A' and b[i]=='T') or (a[i] == 'T' and b[i]=='A') or (a[i] == 'C' and b[i]=='G') or (a[i] == 'G' and b[i]=='C') :
            transversions +=1
        elif (a[i] == 'A' and b[i]=='C') or (a[i] == 'C' and b[i]=='A') or (a[i] == 'T' and b[i]=='G') or (a[i] == 'G' and b[i]=='T') :
            transversions +=1
        else:
            continue
    return print(transitions/transversions)

ratio(s1,s2) #2.507042253521127
