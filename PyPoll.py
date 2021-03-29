# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the wineer of the election based on popular vote.

# Add required dependencies.
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:

    # to do: read and analyze the data here
    # Read the file object with the reader functin.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row[i])



# Using the with statement open the file as a text file.
    #outfile = open(file_to_save,"w")

# Write some data to the file.
##outfile.write("Hello there!")

# To do: perform analysis
   # print(election_data)

# Write 3 counties to the file.
#outfile.write("Counties in the Election \n------------------------- \nArapahoe, \nDenver, \nJefferson")

# Close the file
#outfile.close()

