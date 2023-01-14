#In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, 
#and its weight is equal to the sum of the weights of its symbols.

#The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

#Given: A protein string P of length at most 1000 aa.

#Return: The total weight of P. Consult the monoisotopic mass table.

monoisotopic = {}
with open("monoisotopic.txt") as table:
    for line in table:
       (key, val) = line.split()
       monoisotopic[key] = val
       monoisotopic[key] = float(monoisotopic[key])

def mass(protein):
    m = 0
    for i in protein:
        m += monoisotopic.get(i)
        
    return print(round(m,3))

protein = 'SKADYEK'
mass(protein) #821.392
