n=int(input())
sum= float(0)
listOfShares=[]

for i in range(n):
    listOfShares.append(float(input()));
    sum+=listOfShares[i]

for i in range(len(listOfShares)):
    share=round((listOfShares[i])/sum,3)
    print(share)

#print(listOfShares)
#print(sum)
