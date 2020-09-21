import pandas as pd

#from csv import reader

f = open("C:\\BootCamp\\python-challenge\\PyBank\\Resources\\budget_data.csv","r")
o = open('C:\\BootCamp\\python-challenge\\PyBank\\analysis\\PyBank_outfile','w') ## preparing text file for print

#reader = csv.reader(f,delimiter = ",")
total = 0
results = pd.read_csv(f)
number_of_months = len(results)
count = 0
maxprofit = 0
maxdecrease = 0
for i, row in results.iterrows():
    count = 1 + count
    #print(i, row)
    total = total + int(row[1])
    if count == 1:
        first_Month_PL = int(row[1])
    if count == number_of_months:
        last_Month_PL = int(row[1])
    if int(row[1]) > maxprofit:
        maxprofit = int(row[1])
        date_increase = str(row[0])
    if int(row[1]) < maxdecrease:
        maxdecrease = int(row[1])
        date_decrease = str(row[0])
average_change = (last_Month_PL - first_Month_PL)/86
rounding_of_average_change = float("{:.2f}".format(average_change)) 
print("")
print("financial Analysis")
print("---------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: ${total}")
#print(f"first month profit loses: {first_Month_PL}")
#print(f"last month profit loses: {last_Month_PL}")
print(f"The average change: ${rounding_of_average_change}")
print(f"Greatest Increase in Profits: {date_increase} and profit (${maxprofit})")
print(f"Greatest Decrease in Profits: {date_decrease} and profit (${maxdecrease})")


#### output file commands
print("financial Analysis", file=o)
print("---------------------------", file=o)
print(f"Total Months: {number_of_months}", file=o)
print(f"Total: ${total}", file=o)
#print(f"first month profit loses: {first_Month_PL}")
#print(f"last month profit loses: {last_Month_PL}")
print(f"The average change: ${rounding_of_average_change}", file=o)
print(f"Greatest Increase in Profits: {date_increase} and profit (${maxprofit})", file=o)
print(f"Greatest Decrease in Profits: {date_decrease} and profit (${maxdecrease})", file=o)
o.close()