with open("3rd Assignment/rosalind_iev.txt") as file:
    couples = [int(i) for i in file.readline().strip().split()]

    offspring = 0
    prob = [1, 1, 1, 3/4, 1/2, 0]
    for i in range (len(prob)):
        offspring += couples[i]*prob[i]

    print(2*offspring)
 