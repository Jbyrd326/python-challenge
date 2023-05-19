#Dependencies
import os
import csv

#CSV Path 
file_path = '/Users/jbyrd326/Desktop/Home/python-challenge/PyPoll/Resources/election_data.csv'


#Define Variables

total_votes = 0

candidate_options = []
candidates_recieving_votes = {}

winner = " "
total_won_votes = 0
winning_prcentage = 0


#Read CSV File & 
with open(file_path, 'r') as csvfile:
    csvreader =csv.reader(csvfile, delimiter= ',')
    next(csvreader)

    #Print Total votes
    for row in csvreader:

        #Print Total Votes
        total_votes +=1

        #Print Canditdate Names
        candidate_name = row[2]
        #{'name' : 'Charles Casper Stockham' ,
                           #'name' : 'Diana DeGette' ,
                            #'name' :'Raymon Anthony Doane'}

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            candidates_recieving_votes[candidate_name] = 0
        #Add vote    
        candidates_recieving_votes[candidate_name] += 1

#Gather results and add to Txt file
output_file = "Election Results"
with open(output_file, 'w') as file: 
    file.write("\nElection Results\n")
    file.write("\n---------------------------\n")
    file.write(f"\nTotal Votes: {total_votes}\n")
    file.write(f"\n---------------------------\n")

    # Getting % of votes
    for candidates_name in candidates_recieving_votes:
        votes = candidates_recieving_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        canidate_results = (f"{candidate_name}: {vote_percentage} % ({votes:,})\n")
        print(canidate_results)
        file.write (canidate_results)

        if (votes > total_won_votes) and (vote_percentage > winning_prcentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_prcentage = vote_percentage

    #Print the winning Candidate, vote count, and percentage
    
        file.write("\n---------------------------\n")
        file.write(f"\nWinner: {winning_candidate}")
        file.write("\n---------------------------\n")

   