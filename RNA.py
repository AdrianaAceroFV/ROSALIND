#An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
#Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

#Given: A DNA string t having length at most 1000 nt.
#Return: The transcribed RNA string of t.

def transcriptor(dna):
    if len(dna)<=1000:
        if set(dna)=={'A','C','G','T'}:
            rna = dna.replace("T","U")
            return rna
        else:
            print("DNA string has invalid nucleotides")    
    else:
        print("DNA string too long")

t = "GATGGAACTTGACTACGTAAATT"

u = transcriptor(t)
print(u)