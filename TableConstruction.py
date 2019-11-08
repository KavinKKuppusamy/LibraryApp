import pymysql

def createTableBook(db_conn):
    connect_cur = db_conn.cursor()
    query = 'CREATE TABLE Book(ISBN VARCHAR(10) NOT NULL, Title VARCHAR(255), Availability INT NOT NULL DEFAULT 1,PRIMARY KEY(ISBN));'
    connect_cur.execute(query)
    print("Tabel-Book Created!")

def createTableAuthors(db_conn):
    connect_cur = db_conn.cursor()
    query = 'CREATE TABLE Authors(Author_id INT NOT NULL AUTO_INCREMENT, Name VARCHAR(255) NOT NULL, PRIMARY KEY(Author_id));'
    connect_cur.execute(query)
    print("Table-Authors Created")

def createTableBookAuthors(db_conn):
    connect_cur = db_conn.cursor()
    query = 'CREATE TABLE Book_Authors(Author_id INT NOT NULL AUTO_INCREMENT, ISBN VARCHAR(10), PRIMARY KEY(Author_id,ISBN), CONSTRAINT consrt1 FOREIGN KEY(ISBN) REFERENCES Book(ISBN) ON DELETE CASCADE, CONSTRAINT consrt2 FOREIGN KEY(Author_id) REFERENCES Authors(Author_id) ON DELETE CASCADE);'
    connect_cur.execute(query)
    print("Table-Book_Authors Created ")

def createTableBorrower(db_conn):
    connect_cur = db_conn.cursor()
    query = 'CREATE TABLE Borrower(Card_id INT NOT NULL AUTO_INCREMENT, Ssn VARCHAR(11) NOT NULL UNIQUE, Bname VARCHAR(255), Address VARCHAR(255), Phone VARCHAR(14), PRIMARY KEY(Card_id));'
    connect_cur.execute(query)
    print("Table-BorrowerCreated")

def createTableBookLoans(db_conn):
    connect_cur = db_conn.cursor()
    query = 'CREATE TABLE Book_Loans(Loan_id INT NOT NULL AUTO_INCREMENT, ISBN VARCHAR(10),Card_id INT, Date_out DATE, Due_date DATE, Date_in DATE, PRIMARY KEY(Loan_id), CONSTRAINT consrt3 FOREIGN KEY(ISBN) REFERENCES Book(ISBN) ON DELETE SET NULL, CONSTRAINT consrt4 FOREIGN KEY(Card_id) REFERENCES Borrower(Card_id) ON DELETE SET NULL);'
    connect_cur.execute(query)
    print("Table-Book_Loans Created")

def createTableFines(db_conn):
    connect_cur = db_conn.cursor()
    query = 'CREATE TABLE Fines(Loan_id INT NOT NULL , Fine_amt DECIMAL(9,2) NOT NULL DEFAULT 0, Paid INT DEFAULT 0, PRIMARY KEY(Loan_id), CONSTRAINT FOREIGN KEY(Loan_id) REFERENCES Book_Loans(Loan_id) ON DELETE CASCADE);'
    connect_cur.execute(query)
    print("Table-Fines Created")

def auto_increment_col(db_conn):
    connect_cur = db_conn.cursor()
    connect_cur.execute("ALTER TABLE Authors AUTO_INCREMENT = 1;")
    connect_cur.execute("ALTER TABLE Borrower AUTO_INCREMENT = 1;")
    connect_cur.execute("ALTER TABLE Book_Loans AUTO_INCREMENT = 1;")
    print("Auto Increment of Columns Completed")

hostname = 'localhost'
username = 'root'
password = 'kavin'
database = 'library'

DB_Connect = pymysql.connect( host=hostname, user=username, passwd=password, db=database)

cursor = DB_Connect.cursor()
cursor.execute("DROP SCHEMA library;")
cursor.execute("CREATE SCHEMA library;")
cursor.execute("USE library;")
print("Library Schema Created Successfully!")

createTableBook(DB_Connect)
createTableAuthors(DB_Connect)
createTableBookAuthors(DB_Connect)
createTableBorrower(DB_Connect)
createTableBookLoans(DB_Connect)
createTableFines(DB_Connect)
auto_increment_col(DB_Connect)
DB_Connect.close()
