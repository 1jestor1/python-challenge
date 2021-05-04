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
grtstgain = []
#Greatest Decrease in Profits storer
grtstlss = []

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(budgetpath,delimiter=',')
    budget_header = next(budgetreader)
    for row in budgetreader:
        print(row)
    #    mnthcount = mnthcount + 1
    #    nettotal = nettotal + int(row[0])
    #    if row - grtstgain > 0:
    #        grtstgain = row
    #    if grtstlss - row > 0:
    #        grtstlss = row
#print(f"Financial Analysis\n----------------------------\nTotal Months: {mnthcount}\nTotal: ${nettotal}\nGreatest Increase in Profits: {grtstgain[0]} (${grtstgain[1]})\nGreatest Decrease in Profits: {grtstlss[0]} (${grtstlss[1]})")