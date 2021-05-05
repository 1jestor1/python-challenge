import os
import csv

#File Path for budget_data.csv
budgetpath = os.path.join('Resources','budget_data.csv')
#File path for the summary output titled budget_analysis as text file.
#outputpath = os.path.join('Output','budget_analysis.txt')
#Month Count start
mnthcount = 0
#Net total sum storer
nettotal = 0
#Greatest Increase in Profits storer in ["Date", Ammount] format
grtstgain = ["",0]
#Greatest Decrease in Profits storer in ["Date", Ammount] format
grtstlss = ["",0]
#Previous Profit/Loss
prevprft=0

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile,delimiter=',')
    budget_header = next(budgetreader)
    for row in budgetreader:
    #Month counter
        mnthcount = mnthcount + 1
    #Net total calculator.    
        nettotal = nettotal + int(row[1])
        #Store the initial profit/loss amount.
        if mnthcount == 1:
            prft0 = int(row[1])
        #Stores the final prifit/loss amount.
        else:
            prftf = int(row[1])
        #Conditional that checks if current change between months is greater than the currently stored greatest profit.
        if int(row[1]) - prevprft > grtstgain[1]:
        #If conditional is met then data from csv is stored in appropriate places in greatest gain list.
            grtstgain[0] = row[0]
            grtstgain[1] = int(row[1])-prevprft
        #The following conditional similar to the above conditonal but greatest loss.
        if grtstlss[1] > int(row[1]) - prevprft:
            grtstlss[0] = row[0]
            grtstlss[1] = int(row[1])-prevprft
        #Stores current cycles' row data for calculations in the upcoming cycle.
        prevprft = int(row[1])
    avrgdelta = (prftf - prft0) / (mnthcount - 1)
#Stores summary message in the required format using the data from the budget_data.csv.
summary = f"Financial Analysis\n----------------------------\nTotal Months: {mnthcount}\nTotal: ${nettotal}\nAverage Change: ${round(avrgdelta,2)}\nGreatest Increase in Profits: {grtstgain[0]} (${grtstgain[1]})\nGreatest Decrease in Profits: {grtstlss[0]} (${grtstlss[1]})"
#print(mnthcount)
#print(nettotal)
#print(grtstgain)
#print(grtstlss)
#print(avrgdelta)
#Prints summary message.
print(summary)