import math


def findMean():

    Prices = []


    with open("input.txt") as file:
        for line in file:
            StrippedLine = line.strip()
            lineArray = StrippedLine.split("\t")
            #First item is the date, second item is the cost associated; we should parse and get rid of the first...10 characters of the second item, its informatoin about time, and /t
            #after that subtract last week cost with current week and chart that, we will use that number as data
            price = float(lineArray[1])#Turn each price into a float version so we can do math
            Prices.append(price)


        if Prices:
            meanCost = sum(Prices) / len(Prices)
            meanCostRounded = math.ceil(meanCost *100) /100
            print("Mean cost: "+str(meanCostRounded))
            return meanCostRounded
        else:
            print("Error in checking if prices exist")
            return "Error"




def findMeanJustPrices(inputArray):
        meanCost = sum(inputArray) / len(inputArray)
        meanCostRounded = math.ceil(meanCost *100) /100
        #print("Mean cost: "+str(meanCostRounded)) _debug functions_
        return meanCostRounded



#temp = findMean()
#print(temp)