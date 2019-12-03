#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os
import csv

csvpath_load = os.path.join('.','election_data.csv')
file_to_output = os.path.join("election_analysis.txt")

with open(csvpath_load, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    total_votes_cast = 0
    
    # Dict to store candidate_name -> num of votes
    d = {}
    
    for row in csvreader: 
        total_votes_cast = total_votes_cast + 1
        candidate_name = row[2]
        if candidate_name in d:
            d[candidate_name] = d[candidate_name] + 1
        else:
            d[candidate_name] = 1
        
        
    #print(total_votes_cast)
    #print(d)
    
    winner_count = 0
    winner_name = ""
    results_string = ""
    
    # Khan: 63.000% (2218231)
    # Loop through Dict
    for k in d:
#         print(k, (d[k]/total_votes_cast)*100)
        voter_percent = (d[k]/total_votes_cast)*100
        results_string = results_string + k + ": " + "{:.2f}".format(voter_percent) + "% (" + str(d[k]) + ")\n"
        if d[k] >= winner_count:
            winner_count = d[k]
            winner_name = k
            
    #print (winner_count)
    #print (winner_name)
    
    output = (
    f"\nElection Results\n"
    f"--------------------\n"
    f"Total Votes: {total_votes_cast}\n"
    f"--------------------\n"
    f"{results_string}"
    f"--------------------\n"
    f"Winner: {winner_name}\n"
    f"--------------------\n"
    )
    
    print(output)
    
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
        
    
    


# In[ ]:





# In[ ]:




