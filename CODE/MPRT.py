#Given: At most 15 UniProt Protein Database access IDs.

#Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

import requests
import Bio
from Bio import SeqIO
from io import StringIO

baseUrl='http://www.uniprot.org/uniprot/'

 
with open("rosalind_mprt.txt") as file:
    seqIDs = file.read().replace("\n", " ").split() #IDs from given txt    
sequences = {}
for proID in seqIDs:
    URL = baseUrl+proID[0:6]+".fasta"
    response = requests.get(URL)
    sequences[proID] = (response.text.split("\n"))
    sequences[proID] = "".join(sequences[proID][1::])


def N_gly_motif(ID, sequence):
    global positions
    positions = []
    for i in range(0,len(sequence)-3):
        if sequence[i] == 'N' and sequence[i+1]!='P' and (sequence[i+2] == 'S' or sequence[i+2]=='T') and sequence[i+3]!='P':
            positions.append(i+1)

for key, value in sequences.items():
    N_gly_motif(key, value)
    if not positions:
        continue
    else:
        print(key)
        print(*positions)
