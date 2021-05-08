import os
import csv
#path to election data in a [vote id, "county", "candidate"]
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
#Open data as readeble by code.
with open(lctnData_path) as lctnData_file:
    lctnReader = csv.reader(lctnData_file, delimiter=',')
    lctnHeader = next(lctnReader)
    for row in lctnReader:
        #Total vote count
        totalvts = totalvts + 1
        #Want to check for unique candidates and to update both lists when necessary.
        for candidate in cnddtList:
            #Checks if current candidate is unique. If not pulls the index of the already listed candidate.
            if row[2] == candidate:
                uniCnddtCheck = False
                cnddtListIndex = cnddtList.index(candidate)
        #If the candidate is not already on the list (i.e. unique), then they are added to the candidate list as well as new vote item to the vote list.
        if uniCnddtCheck == True:
            cnddtList.append(row[2])
            cnddtVtList.append(1)
        #If the candidate is already on the list, then their index is used to update their vote count. The uniqueness checker is also reset for the next cycle.
        else:
            cnddtVtList[cnddtListIndex] = cnddtVtList[cnddtListIndex] + 1
            uniCnddtCheck = True     
#After reading the whole csv, we compare the list of votes to determine the greatest number and pull index of that vote number.
for votecount in cnddtVtList:
    if vtWnnrCount < votecount:
        vtWnnrCount = votecount
        vtWnnrIndex = cnddtVtList.index(votecount)
#Stores election winner in case the script needs to be expanded or will be used in other applications.
lctnWinner = cnddtList[vtWnnrIndex]
#Creation of summary message. We only create the first 4 lines because they are least dynamic.
summary = f"Election Results\n-------------------------\nTotal Votes: {totalvts}\n-------------------------\n"
#Since I want this to work as generally as possible, the middle lines of summary are generated via loop using the candidate list.
for candidate in cnddtList:
    percent = "{:.3f}%".format(cnddtVtList[cnddtList.index(candidate)] / totalvts * 100)
    summary = summary + f"{candidate}: {percent} ({cnddtVtList[cnddtList.index(candidate)]})\n"
#Last 3 lines of the summary added.
summary = summary + f"-------------------------\nWinner: {lctnWinner}\n-------------------------"
#The last lines of the code output the summary to the terminal and a text file.
print(summary)
with open(outputpath, "w") as smmryfile:
    smmryfile.write(summary)