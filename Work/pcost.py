# pcost.py
#
# Exercise 1.27
import os
import csv
import sys 
print (os.getcwd())




def portfolio_cost(filename):
    TotalCost = 0
    with open(filename ,'rt') as file :
        header = next(file)
        for line in file:
            row = line.split(',')
            #row = csv.reader(file)
            
            try:
                ShareValue = int(row[1])
                SharePrice = float(row[2])
                ShareCost = ShareValue * SharePrice
            except:
                print('Missing Values found.Skipping row!!!')
            TotalCost = TotalCost + ShareCost
    return TotalCost


if len(sys.argv)  == 2:
    filename =sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'


Cost = portfolio_cost(filename)

print ('TotalCost:' , Cost)