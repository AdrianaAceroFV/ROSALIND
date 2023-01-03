#Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).
#The position of a symbol in a string is the total number of symbols found to its left, including itself 
#(e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). 
#The symbol at position i of s is denoted by s[i].
#A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; 
#for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
#The location of a substring s[j:k] is its beginning position j; note that t will have 
#multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

#Given: Two DNA strings s and t (each of length at most 1 kbp).

#Return: All locations of t as a substring of s.

def location(s,t):
    positions = []
    for i in range(0,len(s)):
        if s[i:i+len(t)] == t:
            positions.append(i+1)
        else:
            continue
    return print(*positions)


with open('Motif DNA.txt', 'r') as file1:
    s,t = file1.read().split()
        
location(s,t) 
#prints 36 89 134 228 235 251 344 382 426 460 467 525 532 595 604 685 720 727 734 752 777



    