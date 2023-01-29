#A signed permutation of length n is some ordering of the positive integers {1,2,…,n} in which each integer is then provided 
#with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4)
#is a signed permutation of length 5.

#Given: A positive integer n≤6.

#Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed 
#permutations in any order).

import itertools as it


def signed_perms(n):
    list_elements = [i for i in range(-n,n+1) if i!=0] #
    l = len(list_elements)
    fact = 1
    
    result_rep = list(it.permutations(list_elements,n))

    result = list(filter(lambda x: all(i != -j for i in x for j in x), result_rep))
    for j in range(l,0,-2):
        fact *=j
    with open("solution26.txt","w") as solution:
        solution.write(str(fact))
        for i in result:
            solution.write('\n'+' '.join(map(str,i)))
    solution.close()


signed_perms(3) 