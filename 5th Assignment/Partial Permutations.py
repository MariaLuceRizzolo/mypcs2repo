with open("5th Assignment/rosalind_pper.txt") as file:
    n, k = [int(i) for i in file.readline().strip().split()]

    perm = 1
    for i in range(k):
        perm *= (n - i) 

    print(perm % 1000000)

    