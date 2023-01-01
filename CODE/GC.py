 
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. 
# For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, 
# the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; 
# the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.

import numpy as np
import Bio
from Bio import SeqIO

gc_content = {}
for records in SeqIO.parse("rosalind_gc.txt","fasta"):
        l = len(records.seq)
        gc =records.seq.count("C") + records.seq.count("G")
        content = (gc / l) * 100
        gc_content[records.id]=content

print(max(gc_content, key=gc_content.get),'\n',max(gc_content.values()))

