#In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
#The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, 
#then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

#Given: A DNA string s of length at most 1000 bp.

#Return: The reverse complement sc of s.

def reverse_complement(s):
    if len(s)<=1000:
        if set(s)=={'A','C','G','T'}:
            sc =  s.replace("A","X").replace("T","A").replace("X","T").replace("C","Y").replace("G","C").replace("Y","G")
            return print(sc)
        else:
            print("DNA string has invalid nucleotides")    
    else:
        print("DNA string too long")

s = "AAAACCCGGT"
reverse_complement(s)
