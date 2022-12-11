with open("4th Assignment/rosalind_fibd.txt") as file:
    n, m = [int(i) for i in file.readline().strip().split()] 

    pairs = [1, 1]
       
    for i in range(2, n):
        fib = pairs[i - 1] + pairs[i - 2]

        if i == m:
            fib -= 1
        if i > m:
            fib = fib - pairs[i - m - 1]
            
        pairs.append(fib)

    print(pairs[-1])
 
