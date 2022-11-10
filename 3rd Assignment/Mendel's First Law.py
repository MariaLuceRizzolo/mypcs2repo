with open("3rd Assignment/rosalind_iprb.txt") as file:
    k, m, n = [int(i) for i in file.readline().strip().split()]
   
    tot = k + m + n
    p1 = (k/tot)*((k-1)/(tot-1))+((k/tot)*(m/(tot-1))+(m/tot)*(k/(tot-1))+(k/tot)*(n/(tot-1))+(n/tot)*(k/(tot-1)))
    p2 = 0.75*(m/tot*((m-1)/(tot-1)))
    p3 = 0.5*(m/tot*(n/(tot-1))+(n/tot)*(m/(tot-1)))
    prob = p1 + p2 + p3
    print(prob)