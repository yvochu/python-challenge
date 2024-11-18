# Importing the necessary modules
from pathlib import Path
import csv

# Define the file paths for input and output
file_to_load = Path("C:/Users/chukw/OneDrive/Documents/Data Analytics Bootcamp/Assignments/Module 3/Starter_Code/PyPoll/Resources/election_data.csv")
file_to_output = Path("C:/Users/chukw/OneDrive/Documents/Data Analytics Bootcamp/Assignments/Module 3/Starter_Code/PyPoll/analysis/election_analysis.txt")

# This function loads the election data from the CSV file
def load_election_data(file_path):
    total_votes = 0  # Keeps track of the total number of votes
    candidate_votes = {}  # Dictionary to store each candidate's vote count

    # Open and read the CSV file
    with file_path.open() as election_data:
        reader = csv.reader(election_data)
        next(reader)  # Skip the header row

        # Go through each row in the data
        for row in reader:
            total_votes += 1  # Increase the total vote count
            candidate_name = row[2]  # The candidate's name is in the 3rd column

            # If the candidate is already in the dictionary, increase their vote count
            if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
            else:
                candidate_votes[candidate_name] = 1  # If it's the first vote, add them to the dictionary

    return total_votes, candidate_votes

# This function finds the candidate with the highest votes
def calculate_winner(candidate_votes):
    # Find the candidate with the maximum votes
    winning_candidate = max(candidate_votes, key=candidate_votes.get)
    winning_count = candidate_votes[winning_candidate]
    return winning_candidate, winning_count

# This function formats the election results into a readable string
def format_election_results(total_votes, candidate_votes, winning_candidate):
    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    # For each candidate, calculate their percentage and add it to the results string
    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100  # Calculate the percentage of total votes
        results += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    # Add the winner information
    results += (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )

    return results

# This function saves the results to a text file
def save_results_to_file(results, file_path):
    with file_path.open("w") as txt_file:
        txt_file.write(results)

# Main function to run the analysis
def main():
    # Load the election data and get the total votes and candidate votes
    total_votes, candidate_votes = load_election_data(file_to_load)

    # Find the candidate who won
    winning_candidate, _ = calculate_winner(candidate_votes)

    # Format the results into a nice string
    election_results = format_election_results(total_votes, candidate_votes, winning_candidate)

    # Print the results to the terminal
    print(election_results)

    # Save the results to a text file
    save_results_to_file(election_results, file_to_output)

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
