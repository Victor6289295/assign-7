"""
Library Management System

Task:
- Create functions to manage a library using dictionaries and lists.
- Each book is stored in a dictionary with fields: { "id": int, "title": str, "author": str, "available": bool }
- Users can borrow and return books.
- Support *args for searching books by multiple fields (title, author).
- Support **kwargs for adding optional book details like "year", "genre".


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Books as a Book class.
- Library as a Library class with borrow() and return() methods.
"""

library = {}

def add_book(i,t,a,**kw): library[i]={"title":t,"author":a,"available":True,**kw}
def borrow(i):
    if library.get(i) and library[i]["available"]: library[i]["available"]=False
def ret(i):
    if library.get(i): library[i]["available"]=True
def search(*args):
    return [b for b in library.values() if any(str(v).lower() in str(b).lower() for v in args)]
def report():
    for i,b in library.items(): print(i,b)

while True:
    c=input("\n1.Add 2.Borrow 3.Return 4.Search 5.Report 6.Exit: ")
    if c=="1": add_book(input("ID:"),input("Title:"),input("Author:"),year=input("Year:"),genre=input("Genre:"))
    elif c=="2": borrow(input("ID:"))
    elif c=="3": ret(input("ID:"))
    elif c=="4": print(search(input("Search term:")))
    elif c=="5": report()
    elif c=="6": break

