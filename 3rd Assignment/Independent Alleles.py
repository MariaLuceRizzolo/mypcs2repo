from scipy.special import binom  

with open("3rd Assignment/rosalind_lia.txt") as file:
    k, N = [int(i) for i in file.readline().strip().split()]                                                                      
    sum = 0.0  

    for i in range(N):                                                      
        prob = binom(2**k, i) * 0.25**i * 0.75**(2**k - i)                                                      
        sum += prob                                                        
    print(1-sum) 