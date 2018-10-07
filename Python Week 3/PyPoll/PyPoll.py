import os
import csv
import math

poll_data = os.path.join("..","Resources","election_data.csv")
result_data = os.path.join("..","Results", "Results_PyPoll.txt")
candidates = {}
total_votes = 0
percent_vote = {}
max_vote = 0


with open(poll_data, "r") as election_data_csv:
    csv_reader = csv.reader(election_data_csv)
    header_csv = next(csv_reader)
    for row in csv_reader:
        candidate = row[2]
        total_votes+=1
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1


    for candidate in candidates:
        percent_vote[candidate] = 100 * (candidates[candidate] / total_votes)
        #print(percent_vote)
        if candidates[candidate] > max_vote:
            max_vote = candidates[candidate]
            win = candidate


print (win)
print (candidates)
print(percent_vote)
print (total_votes)

print_results = f"""Results of the Election:
Total Votes:
----------------------------------
{total_votes}
==================================
Votes Per Candidates:
----------------------------------
{candidates}
==================================
Percentage of Votes per Candidate:
----------------------------------
{percent_vote}
==================================
WINNER!!
----------------------------------
{win}
"""

print(print_results)
with open(result_data, 'w') as r:
    r.write(print_results)
