import pandas as pd
import re
import datetime as dt
from us_state_abbrev import * 

f = open("C:\\BootCamp\\python-challenge\\PyBoss\\Resources\\employee_data.csv","r")
results = pd.read_csv(f)
total_employees = len(results)


#for row in results.iterrows():
    

for i, row in results.iterrows():
    

    for key, value in list(us_state_abbrev.items()):
        
        if row[4] == key:
            #print(f'value = {value} key= {key} and row[4] {row[4]}')
            #print(f'{row[4]} before the change')
            row[4] = value
            #print(f'{row[4]} after the change')
            #print(f'{key} value = {value}')
            #print(f'{row[4]}')

            row[1]=row[1].replace(' ', ',') 
            row[2] =pd.to_datetime(row[2])
            row[2]=row[2].strftime('%Y-%m-%d')
            
        
        
        
            row[3] = list(row[3])
            row[3][0] = '*'
            row[3][1] = '*'
            row[3][2] = '*'
            row[3][4] = '*'
            row[3][5] = '*'
            row[3] = ''.join(row[3]) 
    


            print(row)





    #print(f"Total Employees: {total_employees}")