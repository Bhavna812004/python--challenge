import os
import csv
import collections


#input file + path
input_file = os.getcwd()+"\PyPoll\Resources\election_data.csv"
output_file = os.getcwd()+"\PyPoll\Summary.txt"
# Arrays to store all the variables from the file
voter_id = []
county = []
candidate= []

#unique candidate count calculation arrays
unique_candidates = []
unique_candidates_vote = []
unique_candidates_percent = []

with open(input_file, newline='') as cast_election_data:
    reader = csv.reader(cast_election_data, delimiter=',')
    next (reader)
    for row in reader:
        #store total votes in array
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    for x in set(candidate):
        unique_candidates.append(x)

        votes = candidate.count(x)
        unique_candidates_vote.append(votes)

        votes_percent = (votes/(len(voter_id)))*100
        unique_candidates_percent.append (votes_percent)

winning_count = max(unique_candidates_vote)
winner = unique_candidates[unique_candidates_vote.index(winning_count)]

# Header & Summary
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(len(voter_id)))
print("-------------------------")
for i in range(len(unique_candidates)):
    print (unique_candidates[i] + ": " + str(format(unique_candidates_percent[i], '.3f')) + "% (" + str(unique_candidates_vote[i]) + ")" )
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

#Print to text file:Election Results

with open(output_file, 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(len(voter_id)) + "\n")
    text.write("-------------------------\n")
    for i in range(len(unique_candidates)):
        text.write(unique_candidates[i] + ": " + str(format(unique_candidates_percent[i], '.3f')) + "% (" + str(unique_candidates_vote[i]) + ")\n" )
    text.write("-------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("-------------------------\n")
