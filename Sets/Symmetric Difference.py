M,N = input(), input ()

N_splitted= N.split()
N_new = list(map(int,N_splitted))

a,b = input(), input()

b_splitted = b.split()
b_new = list(map(int,b_splitted))

symmetric_difference=set(N_new)^set(b_new)
symmetric_difference_sorted= sorted(list(symmetric_difference))
for i in symmetric_difference_sorted :
    print(i)
