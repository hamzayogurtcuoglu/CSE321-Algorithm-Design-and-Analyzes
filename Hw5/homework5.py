import sys

#part1
def findOptimalCost(n, M, NY, SF):
    optimumNewYork = [0]*n
    optimumSanFrancisco = [0]*n
    optimumNewYork[0] = NY[0]
    optimumSanFrancisco[0] = SF[0]
    planNewYork = ["NY"]*n
    planSanFrancisco = ["SF"]*n

    for i in range(1,n):
        optimumNewYork[i] = NY[i] + min(optimumNewYork[i-1], M + optimumSanFrancisco[i-1])
        optimumSanFrancisco[i] = SF[i] + min(optimumSanFrancisco[i-1], M + optimumNewYork[i-1])

    for i in range(1,n):
        if optimumNewYork[i-1] < M + optimumSanFrancisco[i-1]:
            optimumNewYork[i] = NY[i] + optimumNewYork[i-1]
            planNewYork[i-1] = "NY"
        else:
            optimumNewYork[i] = NY[i] + M + optimumSanFrancisco[i-1]
            planNewYork[i-1] = "SF"

        if optimumSanFrancisco[i-1] < M + optimumNewYork[i-1]:
            optimumSanFrancisco[i-1] = SF[i] + optimumSanFrancisco[i-1]
            planSanFrancisco[i-1] = "SF"
        else:
            optimumSanFrancisco[i] = SF[i] + M + optimumNewYork[i-1]
            planSanFrancisco[i-1] = "NY"


    if optimumNewYork[n-1] < optimumSanFrancisco[n-1]:
        return optimumNewYork[n-1], planNewYork
    return optimumSanFrancisco[n-1], planSanFrancisco

def printResult(SF,NY,M,costOfOptimalPlan,optimalPlan):
    print("-----------------------------------------------")
    print("Switch city cost : ", M)
    print("New York : ", NY)
    print("San Francisco : ", SF)
    print("Optimal Plan with minimum cost : ", optimalPlan)
    print("Cost of optimal plan : ", costOfOptimalPlan)
    print("-----------------------------------------------")

# part2
def OptimalListOfSessions(start, finish):

    for i in range(len(finish)):
        for j in range(len(finish) - i - 1):
            if finish[j] > finish[j + 1]:
                finish[j], finish[j + 1], start[j], start[j + 1] = finish[j + 1], finish[j], start[j + 1], start[j]
    print("-------------------------------------")
    print("We are sorting according to finish of sessions")
    print("Start :  ", start)
    print("Finish : " , finish)
    n = len(finish)
    print("The following sessions are selected ")
    i = 0
    print("Session No :" , i , " start : " ,start[i], " finish : " , finish[i] )
    for j in range(n):
        if start[j] >= finish[i]:
            print("Session No :" , j, " start : ", start[j], " finish : ", finish[j])
            i = j
    print("-------------------------------------")

#part3
def dynamicProgrammingSubset(S,index,subarr):

    sumZeroArray ,dynamicSubArray= [] , []
    if index == len(S):
        if sum(subarr) == 0:
            return subarr
    else:
        sumZeroArray = dynamicProgrammingSubset(S,index + 1, subarr)
        dynamicSubArray = dynamicProgrammingSubset(S, index + 1, \
                          subarr + [S[index]])
    findOptimal(sumZeroArray,dynamicSubArray)

def findOptimal(sumZeroArray,dynamicSubArray):
    if(sumZeroArray != None and sum(sumZeroArray) == 0 and len(sumZeroArray) != 0):
        print("I found a such a subset that's total sum of elements equal to zero :")
        print(sumZeroArray)
        print("------------------------------------------------------------------------")

        sys.exit(0)
    if(dynamicSubArray != None and sum(dynamicSubArray) == 0 and len(dynamicSubArray) != 0):
        print("------------------------------------------------------------------------")
        print("I found a such a subset that's total sum of elements equal to zero :")
        print(dynamicSubArray)
        print("------------------------------------------------------------------------")
        sys.exit(0)

def findSubArray(S):
    print("------------------------------------------------------------------------")
    print("S : " , S)
    dynamicProgrammingSubset(S,0,[])
    print("No subset from given set can form required sum")

#part4
def calculateCountOfAlignment(interval, resultA, resultB, n,l):
    matchCount = 0
    misMatchCount = 0
    gapCount = 0
    BCount = 0
    A = ""
    B = ""
    for i in range (interval,l+1):
        if(chr(resultB[i]) == '-'):
            if BCount<n:
                gapCount = gapCount + 1
                B = B + chr(resultB[i])
            A = A + chr(resultA[i])
        else:
            if resultA[i] == resultB[i]:
                matchCount = matchCount + 1
                B = B + chr(resultB[i])
                A = A + chr(resultA[i])
            else:
                misMatchCount = misMatchCount + 1
                B = B + chr(resultB[i])
                A = A + chr(resultA[i])
            BCount = BCount + 1
    return misMatchCount,matchCount,gapCount,A,B

def minimumCost(SequenceA,SequenceB,mistmatch_score,gap_score,match_score):

    Alength = len(SequenceA)
    n = len(SequenceB)
    resultMatching = []

    for i in range(n+Alength+1):
        resultMatching.append([])
        for j in range((n+Alength+1)):
            resultMatching[i].append(0)

    for i in range(n + Alength + 1):
        resultMatching[i][0] = i * 2
        resultMatching[0][i] = i * 2

    for i in range(1,Alength+1):
        for j in range(1,n+1):
            if SequenceA[i-1] == SequenceB[j - 1]:
                resultMatching[i][j] = resultMatching[i - 1][j - 1]
            else:
                resultMatching[i][j] = min(min(resultMatching[i - 1][j - 1] + 3, resultMatching[i - 1][j] + 2), resultMatching[i][j - 1] + 2)
    l = n + Alength
    i = Alength
    j = n
    Acount = l
    BAcount = l
    resultA = []
    resultB = []
    for t in range(l+1):
        resultA.append(0)
        resultB.append(0)
    while not(i == 0 or j == 0):
        if SequenceA[i-1] == SequenceB[j-1]:
            resultA[Acount] = ord(SequenceA[i - 1])
            Acount = Acount - 1
            resultB[BAcount] = ord(SequenceB[j - 1])
            BAcount = BAcount - 1
            i = i - 1
            j = j - 1
        elif resultMatching[i - 1][j - 1] + 3 == resultMatching[i][j]:
            resultA[Acount] = ord(SequenceA[i - 1])
            Acount = Acount - 1
            resultB[BAcount] = ord(SequenceB[j - 1])
            BAcount = BAcount - 1
            i = i - 1
            j = j - 1
        elif resultMatching[i - 1][j] + 2 == resultMatching[i][j]:
            resultA[Acount] = ord(SequenceA[i-1])
            Acount = Acount - 1
            resultB[BAcount] =ord('-')
            BAcount = BAcount - 1
            i = i - 1
        elif resultMatching[i][j - 1] + 2 == resultMatching[i][j]:
            resultA[Acount] =ord('-')
            Acount = Acount - 1
            resultB[BAcount] = ord(SequenceB[j-1])
            BAcount = BAcount - 1
            j = j - 1

    while Acount > 0:
        if i>0:
            i = i - 1
            resultA[Acount] = ord(SequenceA[i])
            Acount = Acount - 1
        else:
            resultA[Acount] = ord('-')
            Acount = Acount - 1
    while BAcount > 0:
        if j > 0:
            j = j - 1
            resultB[BAcount] = ord(SequenceA[j])
            BAcount = BAcount - 1
        else:
            resultB[BAcount] = ord('-')
            BAcount = BAcount - 1

    interval = 1
    i = l
    while i >= 1:
        if chr(resultB[i]) == '-' and chr(resultA[i]) == '-':
            interval = i + 1
            break
        i = i - 1

    misMatchCount, matchCount, gapCount, A, B = calculateCountOfAlignment(interval,resultA,resultB,n,l)
    Cost = matchCount*match_score + misMatchCount*mistmatch_score + gapCount*gap_score
    print("---------------------------------------------------------------")
    print("Sequence A = " , SequenceA , ", Sequence B = ",SequenceB)
    print("match_score = ",match_score ,", mistmatch_score = ",mistmatch_score, ", gap_score = ",gap_score )
    print("matchCount = ",matchCount , ", misMatchCount = ",misMatchCount, ", gapCount = ",gapCount)
    print("Alignment of sequence A and B : ")
    print(A)
    print(B)
    print("Cost = ", Cost)
    print("---------------------------------------------------------------")

#part5
# I operate Greedy Algorithm Option 2.
# I select 2 minimum operation elements.
# then I calculate all array.
def sumOfElementsList(array):
    print("-------------------------------------")
    print("You are given array : " , array)
    if len(array) == 1:
        print(array[0])
    totalOperationCount = 0
    for i in range(len(array)):
        if len(array) == 1:
            break
        A = min(array)
        array.remove(A)
        B = min(array)
        array.remove(B)
        sum = A+B
        array.append(sum)
        totalOperationCount = totalOperationCount + sum
        print("A = ",A ,", B = ",B , ", A+B = ",sum)

    print("\nSum of array's elements = " , sum)
    print("Total Operation : " , totalOperationCount)
    print("-------------------------------------")



def main():


	print("QUESTION 1")

	# # Q1 Driver:
	SF = [1, 3, 20, 30]
	NY = [50, 20, 2, 4]
	M = 10
	costOfOptimalPlan, optimalPlan = findOptimalCost(len(NY), M, NY, SF)
	printResult(SF,NY,M,costOfOptimalPlan,optimalPlan)

	SF = [47, 45, 26, 2, 3, 99, 67]
	NY = [20, 3, 4, 69, 99, 6, 19]
	M = 10
	costOfOptimalPlan, optimalPlan = findOptimalCost(len(NY), M, NY, SF)
	printResult(SF,NY,M,costOfOptimalPlan,optimalPlan)



	print("QUESTION 2")

	# # Q2 Driver
	start = [0 , 0 , 6 , 2 , 6 , 5]
	finish = [2 , 3 , 10 , 5 , 7 , 60]
	OptimalListOfSessions(start, finish)

	start = [0 , 15 , 20 , 30 ,25]
	finish = [100 , 20 , 30 , 50 ,45 ]
	OptimalListOfSessions(start, finish)


	print("QUESTION 4")

	##Q4 Driver
	match_score = 2
	mistmatch_score = -2
	gap_score = -1

	SequenceA = "ALIGNMENT"
	SequenceB = "SLIME"
	minimumCost(SequenceA,SequenceB,mistmatch_score,gap_score,match_score)

	SequenceA = "HAMZAAY"
	SequenceB = "HEZYAAY"
	minimumCost(SequenceA,SequenceB,mistmatch_score,gap_score,match_score) 


	print("QUESTION 5")
	# Q5 Driver
	array = [10, 20, 25, 26, 30]
	sumOfElementsList(array)

	array = [5,4,3,2,1]
	sumOfElementsList(array)

	print("QUESTION 3")
	## Q3 Driver
	#Q3 is terminated in function if found zero sum of array.
	S = [-1, 6, 4, 2, 3, -7, -5]
	findSubArray(S)

if __name__ == '__main__':
    sys.exit(main())


