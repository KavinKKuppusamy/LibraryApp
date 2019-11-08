import pandas as pd
import pymysql

def insertIntoBook(conn, data, key):
    isbn10 = data.at[key,'ISBN10']
    isbn10 = isbn10.zfill(10)
    title = data.at[key,'Title']
    authors = str(data.at[key,'Author']).split(',')
    availabitity = 1
    cur = conn.cursor()
    query = 'INSERT INTO Book VALUES("'+ str(isbn10) +'","'+ str(title) +'","'+ str(availabitity) +'");'
    cur.execute(query)
    for author in authors:
        query2 = 'INSERT INTO Authors(Name) VALUES("'+ author +'");'
        cur.execute(query2)

    for author in authors:
        query1 = 'INSERT INTO Book_Authors(Isbn) VALUES("'+ str(isbn10) +'");'
        cur.execute(query1)

def insertIntoBorrower(conn, data, key):
    ssn = str(data.at[key,'ssn'])
    bname = str(data.at[key,'first_name']) +" "+ str(data.at[key,'last_name'])
    address = str(data.at[key,'address']) +","+ str(data.at[key,'city']) +","+ str(data.at[key,'state'])
    phone = str(data.at[key,'phone'])

    query = 'INSERT INTO Borrower(Ssn,Bname,Address,Phone) VALUES("'+ ssn +'","'+ bname +'","'+ address +'","'+ phone +'");'
    cur.execute(query)


hostname = 'localhost'
username = 'root'
password = 'kavin'
database = 'library'
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database)
cur = myConnection.cursor()

books = pd.read_csv('books.csv')
borrowers = pd.read_csv('borrowers1.csv')

#for i in range(1,len(books)+1):
#    insertIntoBook(myConnection,books[i-1:i],i-1)

for i in range(1,len(borrowers)+1):
	insertIntoBorrower(myConnection,borrowers[i-1:i],i-1)

print("Successfully initialized all tables")

myConnection.commit()
myConnection.close()
