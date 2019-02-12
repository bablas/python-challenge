import os
import csv

inputfile = os.path.join("election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []


with open(inputfile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
        
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
       

        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
 
print(f"-"*25)
print(f"Election Results")   
print(f"-"*25)
print(f"Total Votes: {count}")    
print(f"-"*25)

for i in range(len(unique_candidate)):
            print(f"{unique_candidate[i]}: {round(vote_percent[i],3)}% ({vote_count[i]})")
print(f"-"*25)
print(f"Winner: {winner}")
print(f"-"*25)

with open('election_results.txt', 'w') as text:
    
    text.write("\n")
    text.write(f"Election Results")
    text.write("\n")
    text.write(f"-"*25)
    text.write("\n")
    text.write(f"Total Vote: {(count)}")
    text.write("\n")
    text.write(f"-"*25)
    text.write("\n")
    for i in range(len(set(unique_candidate))):
        text.write(f"{unique_candidate[i]}: {round(vote_percent[i],3)}% ({vote_count[i]})\n")
    text.write(f"-"*25)
    text.write("\n")
    text.write(f"Winner: {winner}\n")
    text.write(f"-"*25)
    text.write("\n")