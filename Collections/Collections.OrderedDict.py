from collections import OrderedDict
N=int(input())

ordered_dictionary = OrderedDict()
for i in range(0,N):
    tmp=input().split()
    if ' '.join(tmp[0:len(tmp)-1]) in ordered_dictionary.keys():
        ordered_dictionary[' '.join(tmp[0:len(tmp)-1])]=ordered_dictionary[' '.join(tmp[0:len(tmp)-1])]+int(tmp[len(tmp)-1])
    else:
        ordered_dictionary[' '.join(tmp[0:len(tmp)-1])]=int(tmp[len(tmp)-1])
   
for i in ordered_dictionary.items():
    print (*i)
