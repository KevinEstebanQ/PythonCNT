


def MyBinarySearch(SortedList, WantedNumber):
      lowerPointer = 0
      UpperPointer = len(SortedList)-1
      while(lowerPointer<=UpperPointer):
            middle = (lowerPointer+UpperPointer)//2
            possibleTarget = SortedList[middle]
            if(possibleTarget == WantedNumber):
                  return middle
            elif (WantedNumber<possibleTarget):
                  UpperPointer = middle-1
            else:
                  lowerPointer = middle+1
      return -1
      

def main():
      myList = [1,2,3,4,5,6,7,8,9]
      print("find 15, in " + str(myList) + " position: " + str(MyBinarySearch(myList, 15)))

main()
