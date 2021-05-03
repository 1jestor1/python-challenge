import os
import csv

#WHY ARE YOU NOT WORKING?
budgetpath = os.path.join('Resources','budget_data.csv')
#outputpath = os.path.join('Output','budget_analysis.csv')
mnthcount = 0
nettotal = 0
grtstgain = []
grtstlss = []

with open(budgetpath) as csvfile:
    budgetreader = csv.reader(budgetpath,delimiter=',')
    budget_header = next(budgetreader)
    for row in budgetreader:
        mnthcount = mnthcount + 1
        nettotal = nettotal + row[1]
        if row - grtstgain > 0:
            grtstgain = row
        if grtstlss - row > 0:
            grtstlss = row
print(f"Financial Analysis\n----------------------------\nTotal Months: {mnthcount}\nTotal: ${nettotal}\nGreatest Increase in Profits: {grtstgain[0]} (${grtstgain[1]})\nGreatest Decrease in Profits: {grtstlss[0]} (${grtstlss[1]})")
