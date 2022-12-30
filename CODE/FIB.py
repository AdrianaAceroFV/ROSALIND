#When finding the n-th term of a sequence defined by a recurrence relation, 
#we can simply use the recurrence relation to generate terms for progressively larger values of n. 
#This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

#Given: Positive integers n≤40 and k≤5.

#Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
#every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

#Let's show some terms of the sequence for 5 months and k = 3:
#{1,1,4,7,19}
#it is defined by the recurrence F(n) = F(n-1) + 3F(n-2),
#more generally: F(n) = F(n-1) + k*F(n-2)

def pairs_rabbits(n, k): #let n be the nth-month,k rabbit pairs
    if n <= 40 and k<=5:
        rabbits = []
        rabbits.extend([1,1]) # initial conditions for n = 1, 2
        for i in range(2,n):
            i_n = rabbits[i-1] + k*rabbits[i-2]
            rabbits.append(i_n)
        return rabbits[n-1]
    else:
        print("Invalid arguments")


pairs_rabbits(5,3) # prints 19 
    