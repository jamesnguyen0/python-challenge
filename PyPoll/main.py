#libraries
import os
import csv

#variables
totalVotes = 0
winner = ""
myCandidates = {}

#read files
pybank_csv = os.path.join("Resources","election_data.csv")
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #skip header   
    header = next(csvreader)
    
    #loop through each row
    for row in csvreader:
        #if candidate is not already in dict key list, create key and increment voter totals
        if not(row[2] in myCandidates.keys()):    
            myCandidates[row[2]] = 1
            totalVotes += 1
        #else if candidate is already in dict key list, just increment voter totals
        else:
            myCandidates[row[2]] += 1
            totalVotes += 1

    #calculate winner
    temp = 0
    for i in myCandidates:
        if myCandidates[i] > temp:
            temp = myCandidates[i]
            winner = i

    #output to console
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")
    for i in myCandidates:
        print(f"{i}: {str('{:.3%}'.format(myCandidates[i]/totalVotes))} ({myCandidates[i]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    #prep text for output to .txt
    text = []

    text.append("Election Results")
    text.append("-------------------------")
    text.append("Total Votes: " + str(totalVotes))
    text.append("-------------------------")
    for i in myCandidates:
        text.append(i + ": " + str("{:.3%}".format(myCandidates[i]/totalVotes)) + " (" + str(myCandidates[i])  + ")")
    text.append("-------------------------")
    text.append("Winner: " + winner)
    text.append("-------------------------")
    
    outputtext = zip(text)

#write files
output_file = os.path.join("Analysis","PyPoll_analysis.txt")    
with open(output_file, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerows(outputtext)
