aList = [1,3,5,6,3,2]
def sortList(myList):
    for i in range(len(myList)):
        minIndex =i
        for j in range(i+1, len(myList)):
            if (myList[minIndex] > myList[j]):
                minIndex = j
        
        myList[i],myList[minIndex] = myList[minIndex], myList[i]

    return myList

newmap = {}
for element in aList:
    if str(element) in newmap:
         print("is")
    else:
        newmap[str(element)] = 1

print(newmap)

print(sortList(aList))
