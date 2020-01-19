
def findingBestDay(C,P,begin,end):
    mid = (begin+end) // 2

    if end - begin == 1 or end - begin == 0:
        if len(C) > end+2 and end - begin == 1:

            if ((P[begin + 1] - C[begin]) <= 0):
                print("\nREPORT! ZERO MAKE MONEY DAY ->", begin+1,".day")
            if ((P[end + 1] - C[end]) <= 0):
                print("\nREPORT! ZERO MAKE MONEY DAY ->", end+1,".day")

            if ((P[begin+1] - C[begin]) > (P[end+1] - C[end])):
                return begin
            else:
                return end
        return begin

    day1 = findingBestDay(C, P, mid+1, end)
    day2 = findingBestDay(C, P, begin, mid)

    if((P[day1+1]-C[day1]) > (P[day2+1]-C[day2])):

        return day1
    else:
        return day2

def startTrade(C,P):

    print("Cost : ",C)
    print("Price : ",P)
    indexDay = findingBestDay(C, P, 0, len(C) - 1)
    print()
    return "The Best Day To Buy Goods -> {}".format(indexDay + 1), "Gain -> {}".format(P[indexDay+1]-C[indexDay])

print("---------------------------------")
C = [5, 11, 2, 21, 5, 7, 8, 12, 13, "-"]
P = ["-", 1, 9, 5, 21, 7, 13, 10, 14, 20]

print(startTrade(C,P))
print("---------------------------------")
print("---------------------------------")
C = [1, 11, 5, 21, 5, 7, 8, 12, 13, "-"]
P = ["-", 7, 9, 5, 21, 17, 13, 10, 14, 20]

print(startTrade(C,P))
print("---------------------------------")
