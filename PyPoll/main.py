import os
import csv

#Step 1 Input Files
inputfile = os.path.join("election_data.csv")

#Step 2 Open Input File
with open(inputfile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    totalVotes = 0
    candidate = []
    unique_candidate = []
    vote_count = []
    vote_percent = []   
    
    for row in csvreader:
#Step 3 Total count of votes
        totalVotes = totalVotes + 1
#Step 4 Assign the Column to Candidate
        candidate.append(row[2])
#Step 5 Adding to a set will give Unique candidates        
    for x in set(candidate):
        unique_candidate.append(x)
#Step 6 We count how many times the candidate is in the set
        candidate_vote_total = candidate.count(x)
        vote_count.append(candidate_vote_total)
#Step 7 For the percent we divided the candidate total votes by the total votes and multiplied it by 100
        candidate_percent = (candidate_vote_total/totalVotes)*100
        vote_percent.append(candidate_percent)
#Step 8 We count the max votes        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
#Step 9 Print Results 
print(f"-"*25)
print(f"Election Results")   
print(f"-"*25)
print(f"Total Votes: {totalVotes}")    
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
    text.write(f"Total Vote: {(totalVotes)}")
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