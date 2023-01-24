#Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

#Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k]
#will match s exactly.

from math import log10

with open('rosalind_prob.txt') as input_data:
	dna, gc_content = input_data.readlines()

gc_content = map(float, gc_content.split())

codon_count = [0, 0]
for codon in dna:
	if codon in ['C', 'G']:
		codon_count[0] += 1
	elif codon in ['A', 'T']:
		codon_count[1] += 1

gc_prob = []
for gc_value in gc_content:
	log_prob = codon_count[0]*log10(0.5*gc_value) + codon_count[1]*log10(0.5*(1-gc_value))
	gc_prob.append(str(log_prob))

print(' '.join(gc_prob))
