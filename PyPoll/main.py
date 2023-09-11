import csv
import os

election_data = os.path.join( "Resources", "election_data.csv")
voter_cast= []
candidates=[]
total_candidates =[]



with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    #print (csvreader)
    csv_header = next(csvreader)
    voter_cast =list(csvreader)
    total_vote=len(voter_cast)
    candid=[]
    total_candid=[]
    votes =[]
    percentage=[]

    
    for row in csvreader:
        print("Hey")
        candidate = voter_cast[row][2]
        total_candid.append(candidate)
        if candidate not in candid:
            candid.append(candidate)
    voted_candidate= len(candid)
    
    for row in csvreader:
        names=candid[row]
        votes.append(total_candid.count(names))
        print(votes)
        print("I am here")
        votepercentage= votes[row]/total_vote
        percentage.append(votepercentage)
#winner= votes.index(max(votes))
    

print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_vote:,}")
print("----------------------------")
#for row in csvreader: 
    #print(f"{candid[row]}: {percentage[row]:.3%} ({votes[row]:,})")
print("----------------------------")
print(f"Winner: {candid[winner]}")
print("----------------------------")


print("Election Results", file=open("election_data.txt"))
print("----------------------------", file=open("election_data.txt"))
print(f"Total Votes: {total_vote:,}", file=open("election_data.txt"))
print("----------------------------", file=open("election_data.txt"))
#for row in csvreader: 
    #print(f"{candid[row]}: {percentage[row]:.3%} ({votes[row]:,})", file=open("election_data.txt"))
print("----------------------------", file=open("election_data.txt"))
print(f"Winner: {candid[winner]}", file=open("election_data.txt"))
print("----------------------------", file=open("election_data.txt"))
    










