import os
import csv
#path to election data in a [vote count, "county", "candidate"]
lctnData_path = os.path.join("Resources","election_data.csv")
#path to output data
lctnResults_path = os.path.join("Output","election_results.txt")
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

with open(lctnData_path) as lctnData_file:
    lctnReader = csv.reader(lctnData_file, delimiter=',')
    lctnHeader = next(lctnReader)
    for row in lctnReader:
        totalvts = totalvts + int(row[0])
        #Want to check for unique candidates and to update both lists when necessary.
        for candidate in cnddtList:
            if row[2] == candidate:
                uniCnddtCheck = False
                cnddtListIndex = cnddtList.index(candidate)
        if uniCnddtCheck == True:
            cnddtList.append(row[2])
            cnddtVtList.append(int(row[0]))
        else:
            cnddtVtList[cnddtListIndex]=cnddtVtList[cnddtListIndex]+int(row[0])
            uniCnddtCheck = True     
print(cnddtList)
print(cnddtVtList)          
print(totalvts)