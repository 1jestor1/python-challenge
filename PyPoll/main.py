import os
import csv
#path to election data in a [vote count, "county", "candidate"]
lctnData_path = os.path.join("Resources","election_data.csv")
#path to output data
outputpath = os.path.join("Output","election_results.txt")
#total vote count
totalvts = 0
#List of candidates.
cnddtList = []
#List of vote counts for each candidate.
cnddtVtList = []
#Unique candidate checker.
uniCnddtCheck = True
#Candidate place value
cnddtListIndex = 0
#Winner count for comparisons
vtWnnrCount = 0
#Winer index for storing winner.
vtWnnrIndex = 0
with open(lctnData_path) as lctnData_file:
    lctnReader = csv.reader(lctnData_file, delimiter=',')
    lctnHeader = next(lctnReader)
    for row in lctnReader:
        totalvts = totalvts + 1
        #Want to check for unique candidates and to update both lists when necessary.
        for candidate in cnddtList:
            if row[2] == candidate:
                uniCnddtCheck = False
                cnddtListIndex = cnddtList.index(candidate)
        if uniCnddtCheck == True:
            cnddtList.append(row[2])
            cnddtVtList.append(1)
        else:
            cnddtVtList[cnddtListIndex]=cnddtVtList[cnddtListIndex] + 1
            uniCnddtCheck = True     
for votecount in cnddtVtList:
    if vtWnnrCount < votecount:
        vtWnnrCount = votecount
        vtWnnrIndex = cnddtVtList.index(votecount)
summary = f"Election Results\n-------------------------\nTotal Votes: {totalvts}\n-------------------------\n"
for candidate in cnddtList:
    percent = "{:.3f}%".format(cnddtVtList[cnddtList.index(candidate)] / totalvts * 100)
    summary = summary + f"{candidate}: {percent} ({cnddtVtList[cnddtList.index(candidate)]})\n"
summary = summary + f"-------------------------\nWinner: {cnddtList[vtWnnrIndex]}\n-------------------------"
print(summary)
with open(outputpath, "w") as smmryfile:
    smmryfile.write(summary)