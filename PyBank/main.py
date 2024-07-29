# Modules
import os
import csv

# Set path for our file
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Set variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
greatest_increase = {'date': None, 'amount': float('-inf')}
greatest_decrease = {'date': None, 'amount': float('inf')}

# Open the csv file
with open(budget_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    # Skip header row
    csv_header = next(csv_reader)
    # Checking header row
    # print(f"Header: {csv_header}")

    # Iterate through each row in file to find total rows
    for row in csv_reader:

        # Started at 0 months but add one for every month to get the total months
        total_months += 1 

        # Started at 0 net_total but add each net total to the previous until there are no more to get the net_total
        # Convert second column to integer
        net_total += int(row[1])
    
        # Convert the Profit/Losses value to an integer
        current_profit_loss = int(row[1])

        # Calculate the change from the previous month and store it
        if previous_profit_loss != None:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)

            # Check if this change is the greatest increase or decrease
            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = row[0]
                
            if change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = row[0]
            
        
        # Update the previous_profit_loss to the current one
        previous_profit_loss = current_profit_loss

# Calculate the average of the changes
average_change = sum(changes) / len(changes) if changes else 0

# Put analysis results in a list to later export to a text file
analysis = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}", 
    f"Total: ${net_total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})", 
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"]

# Print all results
for lines in analysis:
    print(lines)

# Export to a text file in folder named 'analysis'
output_file = os.path.join("analysis", "budget_data_analysis.txt")

with open(output_file, 'w') as file:
    for lines in analysis:
        file.write(lines + '\n')

        # '\n' used so each result is written on a new line as opposed to a continuation on the same line, for readability