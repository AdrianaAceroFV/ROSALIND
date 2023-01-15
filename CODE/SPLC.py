#After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

#Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

import Bio
from Bio import SeqIO
from Bio.Seq import Seq

sequences=[]
for records in SeqIO.parse("rosalind_splc.txt","fasta"):
    sequences.append(str(records.seq))

DNAstring = sequences[0]
introns = sequences[1:]


for i in introns:
    DNAstring = DNAstring.replace(i," ") #delete introns


pasted = DNAstring.replace(" ","") #concatenate exons (sequence without introns)


DNAnointrons = Seq(pasted)
revcomp_DNA = DNAnointrons.translate(to_stop=True)
print(revcomp_DNA)
