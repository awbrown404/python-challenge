# Import os and CSV
import os
import csv

# Set CSV path
csvpath = os.path.join("../PyPoll/election_data.csv")

# Set Variables
total_votes = 0
candidates_list = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

# open CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # skip header
    csv_header = next(csvreader)
    
    # Loop through to count total votes and create candidate list
    for row in csvreader: 
        total_votes = total_votes + 1
        
        candidates_list.append(row[2])

# loop through candidate list to count votes for each candidate        
for candidates in candidates_list:
    if candidates == "Khan":
        Khan_votes = Khan_votes + 1
    elif candidates == "Correy":
        Correy_votes = Correy_votes + 1
    elif candidates == "Li":
        Li_votes = Li_votes + 1
    else:
        Otooley_votes = Otooley_votes + 1

# calculate percentages for each candidate 
Khan_percentage = round((Khan_votes/total_votes) * 100, 2)
Correy_percentage = round((Correy_votes/total_votes) * 100, 2)
Li_percentage = round((Li_votes/total_votes) * 100, 2)
Otooley_percentage = round((Otooley_votes/total_votes) * 100, 2)

# determine who has the greatest number of votes
if Khan_votes > Correy_votes > Li_votes > Otooley_votes:
    winning_candidate = "Khan"
elif Correy_votes > Khan_votes > Li_votes > Otooley_votes:
    winning_candidate = "Correy"
elif Li_votes > Khan_votes > Correy_votes > Otooley_votes:
    winning_candidate = "Li"
else:
    winning_candidate = "O'tooley"
        
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {Khan_percentage}% ({Khan_votes})")
print(f"Correy: {Correy_percentage}% ({Correy_votes})")
print(f"Li: {Li_percentage}% ({Li_votes})")
print(f"O'Tooley: {Otooley_percentage} ({Otooley_votes})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

