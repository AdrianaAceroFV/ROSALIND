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




