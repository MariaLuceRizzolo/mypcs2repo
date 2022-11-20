def rec_fibonacci (n,k):
    if n == 0:
        return 0
    if n == 1:
        return 1

    rabbit_pairs = rec_fibonacci(n-1, k) + k*rec_fibonacci(n-2, k)  
        
    return rabbit_pairs

with open("4th Assignment/rosalind_fib.txt") as file:
    n, k = [int(i) for i in file.readline().strip().split()] 

    print (rec_fibonacci(n,k))

  