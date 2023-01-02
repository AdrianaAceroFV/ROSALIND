#Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

#Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

#Return: The Hamming distance dH(s,t).

def dH(s,t):
    if len(s)<=1000 and len(t)<=1000:
        return sum(x != y for x, y in zip(s, t))
    else:
        print("DNA string exceeds 1kbp")
  
  
with open('mutations_s.txt', 'r') as file1, open('mutations_t.txt', 'r') as file2: #Let's supose that I have two files, each one contains the DNA strings
    s = file1.read()
    t = file2.read()
    dH(s,t) #prints 480
    