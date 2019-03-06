# Script for analyzing a set of poll data called election_data.csv 
# The dataset is composed of three columns: Voter ID , County , and Candidate. 

#modules to read the csv and write the txt
import os
import csv

def votes_person(elect_list):
    vote_counter = {}
    # Create a dictionary with the name of the candidate and the number of votes    
    for person in elect_list:
        vote_counter[person[2]] = vote_counter.get(person[2],0) + 1

    # Obtain the winner of the election based on popular vote
    winner_key = max(vote_counter, key=lambda key: vote_counter[key])
    
    return vote_counter, winner_key

# The set of financial data called election_data.csv, must be located in the folder Resources
election_csv = os.path.abspath("Resources\\election_data.csv")

try:
    # Code that might cause an exception
    with open(election_csv, newline='') as csvfile:   # or newline='\n'
        csvreader = csv.reader(csvfile, delimiter=',')
        csv_header = next(csvreader)
        elections = list(csvreader)

except FileNotFoundError:
    # Code to be ejecuted in case the FileNotFoundError exception arises
    print("path=" + str(os.path.abspath("Resources\\election_data.csv")))
    print("Please check the path of the file.")

else:
    # Code to be ejecuted if the try block was successful
    vote_results = {}
    total_votes = len(elections)
    vote_results, winner = votes_person(elections)

    # Print the analysis to the terminal 
    print("Election Results\n-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")

    for key, value in vote_results.items():
        # Calculate the percentage of votes each candidate won
        cand_per = float((value / total_votes) * 100)
        print("{}:{}% ({})".format(key, " %2.3f"% (cand_per), value))

    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")

    # Export the results to a text file
    # save the output file path
    output_file = os.path.abspath("Output\\results.txt")

    # open the output file and write the results
    with open(output_file, "w") as text_file:
        print("Election Results\n-------------------------", file=text_file)
        print(f'Total Votes: {total_votes}', file=text_file)
        print("-------------------------", file=text_file)
    
        for key, value in vote_results.items():
            # Calculate the percentage of votes each candidate won
            cand_per = round(float((value / total_votes) * 100),3)
            print("{}:{}% ({})".format(key, " %2.3f"% (cand_per), value), file=text_file)
    
        print("-------------------------", file=text_file)
        print(f'Winner: {winner}', file=text_file)
        print("-------------------------", file=text_file)