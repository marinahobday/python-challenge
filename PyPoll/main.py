import os
import csv
pypoll_csv = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
#making output for .txt file for analysis folder
pypoll_output = os.path.join("analysis", "pypoll_analysis.txt")

#clarifying our variables
total = 0
vote_counts = []
vote_percent = []
unique_candidates = []

#reading our csvfile to perform coding
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #header set
    header = next(csvreader)

    #starting our first loop to find total
    for row in csvreader:
        total += 1

        #looping through names to find the candidates and count how many votes they received to put into a list
        # they lists are: unique_candidates and vote_counts
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
            index = unique_candidates.index(row[2])
            vote_counts.append(1)
        else:
            index = unique_candidates.index(row[2])
            vote_counts[index] += 1

    #outside of first loop, new loop to find the percentage and put it in a list called vote_percent
    for votes in vote_counts:
        percent = (votes/total) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        vote_percent.append(percent)

    #outside of all loops, now must find winner through the one with the max vote counts
    #need to match the max vote counts with the name of candidate
    winner = max(vote_counts)
    index = vote_counts.index(winner)
    winner = unique_candidates[index]

#print to terminal
print("Election Results")
print("-------------------")
print(f"Total Votes: {total}")
print("-------------------")
print(f"{unique_candidates[0]}: {str(vote_percent[0])} ({str(vote_counts[0])})")
print(f"{unique_candidates[1]}: {str(vote_percent[1])} ({str(vote_counts[1])})")
print(f"{unique_candidates[2]}: {str(vote_percent[2])} ({str(vote_counts[2])})")
print(f"{unique_candidates[3]}: {str(vote_percent[3])} ({str(vote_counts[3])})")
print("-------------------")
print(f"Winner: {winner}")
print("-------------------")

#print to .txt file
with open(pypoll_output, "a") as txt_file:
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------")
    txt_file.write("\n")   
    txt_file.write("Total Votes " + str(total))
    txt_file.write("\n")   
    txt_file.write("-------------------")
    txt_file.write("\n")   
    txt_file.write(unique_candidates[0] + ": " + str(vote_percent[0]) + " (" + str(vote_counts[0]) + ")")
    txt_file.write("\n")
    txt_file.write(unique_candidates[1] + ": " + str(vote_percent[1]) + " (" + str(vote_counts[1]) + ")")
    txt_file.write("\n")
    txt_file.write(unique_candidates[2] + ": " + str(vote_percent[2]) + " (" + str(vote_counts[2]) + ")")
    txt_file.write("\n")
    txt_file.write(unique_candidates[3] + ": " + str(vote_percent[3]) + " (" + str(vote_counts[3]) + ")")
    txt_file.write("\n")   
    txt_file.write("-------------------")
    txt_file.write("\n")   
    txt_file.write("Winner: " + str(winner))
    txt_file.write("\n")   
    txt_file.write("-------------------")
    txt_file.write("\n") 
    txt_file.close()  

#tried two different ways of printing to .txt output file for practice :)