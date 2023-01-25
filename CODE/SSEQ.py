#Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

#Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

import Bio
from Bio import SeqIO

sequences = []
for records in SeqIO.parse("rosalind_sseq.txt","fasta"):
    sequences.append(str(records.seq))

s = sequences[0]
t = sequences[1]

positions = []
for i in t: 
    positions.append([pos for pos, char in enumerate(s) if char == i ])

solution = []
solution.append(positions[0][0]+1)

n = len(positions)

for pos in range(1,n):
    for element in positions[pos][:]:
        if element + 1 > solution[-1]:
            solution.append(element+1)
            break
        
print(*solution)
