"""
Bank Account Simulation

Task:
- Manage simple bank accounts.
- Store accounts in dictionary { "account_number": {"name": str, "balance": float} }
- Deposit, withdraw, transfer between accounts.
- Use *args for batch deposits/withdrawals.
- Use **kwargs for flexible account creation (e.g., overdraft_limit).

// NOT FOR THIS TASK
Future OOP Extension:
- BankAccount class with methods deposit(), withdraw(), transfer().
- Bank class to manage all accounts.
"""
accounts = {}

def create(acc, name, bal=0): accounts[acc]={"name":name,"balance":bal}
def deposit(acc,*amt): accounts[acc]["balance"]+=sum(amt)
def withdraw(acc,*amt): 
    t=sum(amt); 
    if accounts[acc]["balance"]>=t: accounts[acc]["balance"]-=t
def report(): 
    for a,r in accounts.items(): print(f"{a}-{r['name']}: {r['balance']}")

while True:
    c=input("\n1.Create 2.Deposit 3.Withdraw 4.Report 5.Exit: ")
    if c=="1": create(input("Acc:"),input("Name:"),float(input("Bal:")))
    elif c=="2": deposit(input("Acc:"),float(input("Amt:")))
    elif c=="3": withdraw(input("Acc:"),float(input("Amt:")))
    elif c=="4": report()
    elif c=="5": break

