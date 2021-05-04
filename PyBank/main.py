import os
import csv

#WHY ARE YOU NOT WORKING?!? 
budgetpath = os.path.join('Resources','budget_data.csv')
print(budgetpath)
#outputpath = os.path.join('Output','budget_analysis.csv')
#Month Count
mnthcount = 0
#Net total sum storer
nettotal = 0
#Greatest Increase in Profits storer
grtstgain = 0
#Greatest Decrease in Profits storer
grtstlss = 0
#Previous Profit/Loss
prevprft=0

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(csvfile,delimiter=',')
    budget_header = next(budgetreader)
    for row in budgetreader:
        mnthcount = mnthcount + 1
        nettotal = nettotal + int(row[1])
        if mnthcount == 1:
            prft0 = int(row[1])
        else:
            prftf = int(row[1])
        if int(row[1]) - prevprft > grtstgain:
            grtstgain = int(row[1])-prevprft
        if grtstlss > int(row[1]) - prevprft:
            grtstlss = int(row[1])-prevprft
        prevprft = int(row[1])
    avrgdelta = (prftf - prft0) / (mnthcount - 1)
#print(f"Financial Analysis\n----------------------------\nTotal Months: {mnthcount}\nGreatest Increase in Profits: {grtstgain[0]} (${grtstgain[1]})\nGreatest Decrease in Profits: {grtstlss[0]} (${grtstlss[1]})")
print(mnthcount)
print(nettotal)
print(grtstgain)
print(grtstlss)
print(avrgdelta)