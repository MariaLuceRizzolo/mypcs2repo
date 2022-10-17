if __name__ == '__main__':
    firstlist=[]

    for i in range(int(input())):
        name = input()
        score = float(input())
        
        arr=[]
        arr.append(name)
        arr.append(score)
        
        firstlist.append(arr)
     
    firstlist.sort(key = lambda x: x[1])
    secondlowest=[]
    temp=firstlist[len(firstlist)-1][1]
    
    for i in range(len(firstlist)):
        if firstlist[i][1]>firstlist[0][1] and firstlist[i][1]<=temp:
            temp= firstlist[i][1]
            secondlowest.append(firstlist[i][0])
    
    secondlowest.sort()
    for i in range (len(secondlowest)):
        print(secondlowest[i])

    
  
