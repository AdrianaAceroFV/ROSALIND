#Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing 
#for a given factor. In order, the six given integers represent the number of couples having the following genotypes:
#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa
#Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

"""Dominant phenotype probabilities:"""

p_AAAA = 1
p_AAAa = 1
p_aaaa = 0
p_AAaa = 1
p_AaAa = 0.75
p_Aaaa = 0.5

def dominant_offspring(a,b,c,d,e,f):
    expectancy = (a*p_AAAA+b*p_AAAa+c*p_AAaa+d*p_AaAa+e*p_Aaaa+f*p_aaaa)*2 #assumption: that every couple has exactly two offspring
    return print(expectancy)

dominant_offspring(18373,18618,18852,18680,17445,16197)

