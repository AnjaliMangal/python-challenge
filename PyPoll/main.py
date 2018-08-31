import os
import csv

# Path to collect data from the Resources folder
electionCSV = os.path.join('.', 'Resources', 'election_data.csv')


totalVotes =0
totalCandidates=0
# read the csv file
mydict= {}

with open(electionCSV,'r') as csvfile:
    csvreader =  csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        totalVotes = totalVotes + int(row[0])
        totalCandidates = totalCandidates +1
        if row[2] in mydict :
            mydict[row[2]] =  mydict[row[2]] +1
        else :
            mydict[row[2]] = 1

# printing to file and console
filepath = os.path.join('.', 'Resources', 'election_resutls.txt')
file = open(filepath, 'w')
line0 = "Election Results \n--------------------------------"
line1 = "Total Votes : {}".format(totalCandidates)
print(line0)
print(line1)
file.write(line0 + "\n")
file.write(line1 + "\n")

for key in mydict.keys():
    line2  = "{} : {} % ({}) ".format(key ,round(mydict[key]/totalCandidates*100,3),mydict[key])
    print(line2)
    file.write(line2 + "\n")
winner  = [k for k,v in mydict.items() if v==max(mydict.values())][0]

line3 = "--------------------------------"
print(line3)
file.write(line3+ "\n")
line4 = "Winner : {}".format(winner) + "\n" + line3
print(line4 )
file.write(line4)

