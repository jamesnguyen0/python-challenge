#libraries
import os
import csv

#variables
totalVotes = 0
winner = ""

candidateID = 0
candidateList = []
candidateVotes = []
candidatePercent = []

#read files
pybank_csv = os.path.join("Resources","election_data.csv")
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header   
    header = next(csvreader)
    
    #loop through each row
    for row in csvreader:
        #if candidate is not in list already, add to list and increment voter total
        if not(row[2] in candidateList):
            candidateList.append(row[2])
            candidateVotes.append(1)
            totalVotes += 1
        
        #if candidate is already in list, just increment voter total
        else:
            candidateVotes[candidateList.index(row[2])] += 1
            totalVotes += 1

    #calculate voter %s
    for i in range(len(candidateList)):
        candidatePercent.append(str("{:.3%}".format(candidateVotes[i]/totalVotes))) 

    #calculate winner
    temp = 0
    for i in range(len(candidateVotes)):
        if candidateVotes[i] > temp:
            temp = candidateVotes[i]
            candidateID = i
    
    winner = candidateList[candidateID]

    #output to console
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")
    for i in range(len(candidateList)):
        print(f"{candidateList[i]}: {candidatePercent[i]} ({candidateVotes[i]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #prep text for output to .txt
    text = []

    text.append("Election Results")
    text.append("-------------------------")
    text.append("Total Votes: " + str(totalVotes))
    text.append("-------------------------")
    for i in range(len(candidateList)):
        text.append(candidateList[i] + ": " + candidatePercent[i] + " (" + str(candidateVotes[i]) + ")")
    text.append("-------------------------")
    text.append("Winner: " + winner)
    text.append("-------------------------")
    
    outputtext = zip(text)

#write files
output_file = os.path.join("Analysis","PyPoll_analysis.txt")    
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(outputtext)
