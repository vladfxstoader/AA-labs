#1.1
def readData(filename):
    f=open(filename)
    n=int(f.readline())
    weights=[int(x) for x in f.readline().split()]
    values=[int(x) for x in f.readline().split()]
    indices=[i for i in range(1,n+1)]
    maxWeight=int(f.readline())
    return n,weights,values,indices,maxWeight

#1.2
def sortare(weights,values,indices):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if values[i]/weights[i]<values[j]/weights[j]:
                values[i],values[j]=values[j],values[i]
                weights[i],weights[j]=weights[j],weights[i]
                indices[i],indices[j]=indices[j],indices[i]
    return weights,values,indices

def knapsack(n,weights,values,indices,maxWeight):
    S=0
    ObMax=indices[0]
    WeightMax=weights[0]
    ValueMax=values[0]
    for i in range(0,n):
        if weights[i]<=maxWeight:
            print("Obiectul {} se ia intreg.".format(i+1))
            S=S+values[i]
            maxWeight=maxWeight-weights[i]
        else:
            break
    if i<n:
        fraction = maxWeight / weights[i]
        print("Din obiectul {} luam o fractie de {}.".format(i+1,fraction))
        S=S+fraction*values[i]
    return S

n,weights,values,indices,maxWeight=readData("rucsac.in")
weights,values,indices=sortare(weights,values,indices)
print(weights,values,indices)
print(knapsack(n,weights,values,indices,maxWeight))
