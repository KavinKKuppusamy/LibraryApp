# Library Management Portal

Frontend : HTML, CSS, Bootstrap, Javascript 
Backend : Django, pymysql, mysqlclient, pandas 
Database: MySQL

 
 The Library Management System has been designed for Librarians to carry out various services in a library. Each functionality has been explained as follows: 

1) Search for a Book 
a. The Librarian can enter either an ISBN, Title Name or Author Name to search for a book. 
b. Substring matching is performed to obtain all possible matches. 
c. Availability of book is also mentioned with the respective book. 
d. If either nothing or a space is entered in the text box, the search results in all the books that are present in the library. 

2) Check Out Books 
a. The Librarian can check out books for a borrower. 
b. A borrower cannot check out books if the book is unavailable or he/she has already issued 3 books or he/she has a fine pending. 
c. Once checked out, the system automatically sets the due date to be 14 days from the issue date. 

3) Check In Books 
a. The Librarian can check in books for a borrower. 
b. To search the book loan entry, the librarian can enter either the ISBN, Card Id or part of the borrower’s name to check-in the book.

4) Fines 
a. Given the Card Id of the borrower, the system helps the librarian retrieve the history of fines for that borrower. 
b. It provides option to display all the fines that are due for each book issued by the borrower, the current total fine the borrower has to pay and the fines that have been paid by the borrower in the past. 
c. Every time a fine is paid, the system will update the data base indicating that that particular fine has been paid. 

5) Add new Borrowers 
a. The system allows the Librarian to enter new borrowers into the system. 
b. Basic details (Full Name, Ssn, Address, Phone) are entered to generate a new Card Id for the borrower. 
c. A person is allowed to have only one Card Id. 

Design Overview 
This application is a website that can run on local web server inside a library and possibly on internet. The front-end is developed in HTML and CSS along with Bootstrap, JQuery and Javascript. The backend is developed in python using Django. MYSQL database is used as a DBMS. Django uses MVC framework.

