# Modules
import os
import csv

# Set path for our file
election_data_csv = os.path.join("Resources", "election_data.csv")

# Set variables
total_votes = 0 
# Create an empty dictionary to store votes for each candidate
candidate_votes = {}

# Open the csv file
with open(election_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # Skip header row
    csv_header = next(csv_reader)
    # Checking header row
    # print(f"Header: {csv_header}")

    # Iterate through each row in file to find total votes
    for row in csv_reader:

        # Started at 0 votes but add one for every vote to get the total votes
        total_votes += 1 

        # Initialize the candidate row
        candidate = row[2]

        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        candidate_votes[candidate] += 1

# Using a dictionary comprehension to calculate the percentage of votes each candidate received
candidate_percentages = {candidate: (votes/ total_votes) * 100 for candidate, votes in candidate_votes.items()}
candidate_percentages

# Determine the winner
winner = max(candidate_votes, key = candidate_votes.get)

# Put analysis results in a list to later export to a text file
analysis = []
analysis.append("Election Result")
analysis.append("-------------------------")
analysis.append(f"Total Votes: {total_votes}")
analysis.append("-------------------------")
for candidate in candidate_votes:
    percentage = candidate_percentages[candidate]
    votes = candidate_votes[candidate]
    analysis.append(f"{candidate}: {percentage:.3f}% ({votes})")
analysis.append("-------------------------")
analysis.append(f"Winner: {winner}")
analysis.append("-------------------------")

# Print all results
for lines in analysis:
    print(lines)

# Export to a text file in folder named 'analysis'
output_file = os.path.join("analysis", "election_data_analysis.txt")

with open(output_file, 'w') as file:
    for lines in analysis:
        file.write(lines + '\n')

        # '\n' used so each result is written on a new line as opposed to a continuation on the same line, for readability