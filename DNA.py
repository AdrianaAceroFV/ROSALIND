# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; 
# the length of a string is the number of symbols that it contains. An example of a length 21 DNA string 
# (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA string s of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def counting_nt(s):
    if len(s) <= 1000:
        if set(s)=={'A','C','G','T'}:
            A = s.count("A")
            C = s.count("C")
            G = s.count("G")
            T = s.count("T")
            total = [A,C,G,T]
            return print(*total)
        else:
            print("Invalid nucleotides in DNA string")
    else:
        print("DNA string with more than 1000 nucleotides")


# As personal preference, I'd rather show the nucleotides symbols and numbers:

def counting_nt2(s):
    if len(s) <= 1000:
        if set(s)=={'A','C','G','T'}:
            total = {n : s.count(n) for n in set(s)} 
            return total
        else:
            print("Invalid nucleotides in DNA string")
    else:
        print("DNA string with more than 1000 nucleotides")
