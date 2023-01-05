#Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 
#and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
#Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. 

#Given: Positive integers n≤100 and m≤20.

#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

def mortal_fib(n,m):
    rabbits = []
    rabbits.extend([1,1]) #initial conditions [1,1,2] 
    for j in range(2,m):
        j_n = rabbits[j-1]+rabbits[j-2]
        rabbits.append(j_n)
    rabbits.extend([0]*(n-m))
    for i in range(m,n):
        k = 2 
        while k <= m:
            rabbits[i] = rabbits[i] + rabbits[i-k]
            k+=1      
    return print(rabbits[n-1])

mortal_fib(92,16)
