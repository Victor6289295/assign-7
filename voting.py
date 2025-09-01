"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates, voters = {}, set()

def register(*names,**kw): [candidates.setdefault(n,{"votes":0,**kw}) for n in names]
def vote(voter,cand):
    if voter not in voters and cand in candidates:
        candidates[cand]["votes"]+=1; voters.add(voter)
def report(): [print(n,"-",c["votes"],c) for n,c in candidates.items()]

while True:
    c=input("\n1.Register 2.Vote 3.Report 4.Exit: ")
    if c=="1": register(*input("Names(comma): ").split(","),party=input("Party:"),region=input("Region:"))
    elif c=="2": vote(input("VoterID:"),input("Candidate:"))
    elif c=="3": report()
    elif c=="4": break

