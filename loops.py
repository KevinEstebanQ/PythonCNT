def exponential():
    base = int(input("base of the number:"))
    exp = int(input("exponent: "))
    newInt = 1
    if exp == 0:
        return 1
    else:
        for i in range(exp):
            newInt = newInt*base
    print(newInt)
    return 0

def AskDiv2():
    while True:
        a = int(input("input a number divisible by 2: "))
        if a%2==0:
             print("you are such a wondeful being, thank you!")
             return 0
        else:
            print("why would you do this to me? you are now trapped in my infinite loop until you answer correctly")

def main():
    answer = int(input("choose program to run: 1.exponential   2.ask for a number divisible by  2  3.quit: "))
    while True:
        if answer == 1:
            exponential()
            main()
        elif answer == 2:
            AskDiv2()
            main()
        elif answer == 3:
            exit()
        else:
            print("wrong type of answer, try again.")
    return 0

main()