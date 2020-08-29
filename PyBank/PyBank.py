import os
import csv

monthcount = 0
monthcount = int
totalprofit = 0
greatestincrease = 0
greatestdecrease = 0
monthprofit = 0
lastmonthprofit = 0
profitchanges = []
months = []
profitchange = 0



csvpath=os.path.join("Resources", "budget_data.csv")


with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    
    for row in csvreader:
        monthcount = monthcount + 1
        months.append(row[0])
        
        