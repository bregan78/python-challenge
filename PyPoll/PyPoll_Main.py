import pandas as pd



#f = open("C:\\BootCamp\\python-challenge\\PyPoll\\Resources\\election_data.csv","r")
f = open("Resources\\election_data.csv","r")
o = open('analysis\\PyPoll_outfile.txt','w') ## preparing text file for print


results = pd.read_csv(f)
total_Votes = len(results)
winner = 0

votes={
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "O'Tooley": 0
}

for i, row in results.iterrows():
    if row[2] == "Khan":
        votes["Khan"] = 1 + votes["Khan"]
    if row[2] == "Correy":
        votes["Correy"] = 1 + votes["Correy"]
    if row[2] == "Li":
        votes["Li"] = 1 + votes["Li"]
    if row[2] == "O'Tooley":
        votes["O'Tooley"] = 1 + votes["O'Tooley"]
    
khan_perc = ((votes["Khan"]/total_Votes)) * 100
correy_perc = (votes["Correy"]/total_Votes) * 100
li_perc = (votes["Li"]/total_Votes) * 100
otooley_perc = (votes["O'Tooley"]/total_Votes) * 100

#briantestpercent = 100.0005
#roudning= float("{:.3f}".format(briantestpercent)) 
#print(roudning)

#print('{0:.3f}'.format(briantestpercent))



rounding_khan_perc = '{0:.3f}'.format(khan_perc) 
#rounding_khan_perc1 = '{0:.2f}'.format(khan_perc)

#rounding_correy_perc = float("{:.3f}".format(correy_perc)) 
#rounding_li_perc = float("{:.3f}".format(li_perc)) 
#rounding_otooley_perc = float("{:.3f}".format(otooley_perc)) 

rounding_correy_perc = '{0:.3f}'.format(correy_perc) 
rounding_li_perc = '{0:.3f}'.format(li_perc) 
rounding_otooley_perc = '{0:.3f}'.format(otooley_perc) 

nameO= "O'Tooley"

print("Election Results")
print("------------------------")
print(f"Total Votes: {total_Votes}")
print("------------------------")
print(f"Khan: {rounding_khan_perc}% ({votes.get('Khan')})")
#print(f"Khan: {rounding_khan_perc1} ({votes.get('Khan')})")
print(f"Correy: {rounding_correy_perc}% ({votes.get('Correy')})")
print(f"Li: {rounding_li_perc}% ({votes.get('Li')})")

print(f"O\'Tooley: {rounding_otooley_perc}% ({votes.get(nameO)})")
print("----------------------------")
print(f"The winner is: {max(votes, key=votes.get)}")
#print(f"Total Months: {total}")


#### print to file "o"

print("Election Results", file=o)
print("------------------------", file=o)
print(f"Total Votes: {total_Votes}", file=o)
print("------------------------", file=o)
print(f"Khan: {rounding_khan_perc}% ({votes.get('Khan')})", file=o)
print(f"Correy: {rounding_correy_perc}% ({votes.get('Correy')})", file=o)
print(f"Li: {rounding_li_perc}% ({votes.get('Li')})", file=o)

print(f"O\'Tooley: {rounding_otooley_perc}% ({votes.get(nameO)})", file=o)
print("----------------------------", file=o)
print(f"The winner is: {max(votes, key=votes.get)}", file=o)