import os
import csv

# Path to collect data from the Resources folder
budgetCSV = os.path.join('.', 'Resources', 'budget_data.csv')

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    totalMonths  =0
    totalNetAmount = 0
    monthList = []
    profitLossList = []

    # Loop through the data
    for row in csvreader:
        totalMonths =  totalMonths +1
        totalNetAmount = totalNetAmount + int(row[1])
        monthList.append(row[0])
        profitLossList.append(int(row[1]))


netChangeList = [profitLossList[n+1]-profitLossList[n] for n in range(0,len(profitLossList)-1)]
averageChange = round(average(netChangeList),2)

monthList.pop(0)
minIndex = netChangeList.index(min(netChangeList))
maxIndex = netChangeList.index(max(netChangeList))

line0 = "Financial Analysis \n--------------------------------"
line1 = "Total Number of Months :: {}".format(totalMonths)
line2 = "Total NetAmount  :: ${}".format(totalNetAmount)
line3 = "Average  Change: ${}".format(averageChange)
line4 = "Greatest Increase in Profits : {}  (${})".format(monthList[maxIndex],max(netChangeList))
line5 = "Greatest Decrease in Profits: {} (${})".format(monthList[minIndex],min(netChangeList))

outputString = line0+"\n"+line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5
#printing on console
print(outputString)

#printing in file

budgetfile = os.path.join('.', 'Resources', 'budget_information.txt')
file = open(budgetfile, 'w')
file.write(outputString)
