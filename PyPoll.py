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

# Initialize total vote counter.
total_votes = 0

# Declaring a new list 
candidate_options = []

# Declare an emply dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load, 'r') as election_data:

    # to do: read and analyze the data here
    # Read the file object with the reader functin.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    ##print(headers)

    # Add to total vote count.
    for row in file_reader:
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate name doesn't match existing candidate..
        if candidate_name not in candidate_options:
            # Add to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n"
        )
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determin the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of vote.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate.
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    # Print out the winning candidate, vote count and percentage of votes.
    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percetage: {winning_percentage:.1f}\n"
        f"------------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
    print(headers)
