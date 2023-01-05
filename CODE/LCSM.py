#A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring 
#if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; 
#in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

#Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

#Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

import suffix_tree
from suffix_tree import *
import Bio
from Bio import SeqIO

dict={}
for records in SeqIO.parse("rosalind_lcsm.txt","fasta"):
    dict[records.id]=str(records.seq)

tree = Tree(dict)

with open("resultado.txt", "w") as file:
    for k,length,path in tree.common_substrings():  
        if k == len(dict):
            file.write(str(path))
file.close()

with open("resultado.txt", "r") as file:
   content = file.read()
   print(content.replace(' ',''))

file.close()





