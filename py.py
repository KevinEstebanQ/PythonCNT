

ul = [9,8,7,6,5,4,3,2,1]

def sortList(ul):
    n=len(ul)

    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if ul[minIndex]> ul[j]:
                minIndex = j
        ul[i],ul[minIndex] = ul[minIndex], ul[i]

    return ul


def binarySearch(sortedList, target):
    left, Right = 0, len(sortedList)-1
    
    mid = (left+ Right)//2

    while(left <= Right):


        if sortedList[mid]== target:
            return sortedList[mid] == target, "target: " + str(target), "pos: " + str(mid), sortedList
        
        elif target < sortedList[mid]:
            Right = mid-1

        else:
            left = mid+1
        
        mid = (left+Right)//2

    
    return "not Found"


print(binarySearch(sortList(ul), 8))
