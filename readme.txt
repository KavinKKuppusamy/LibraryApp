Requirements

1)	Windows 10
2)	Google Chrome
3)	Python 3.8
4)	MySQL  – All Packages (Server, Client)
5)	Pymysql (pip install pymysql)
	Add Cryptography (pip install PyMySQL[rsa])
6)	Mysqlclient or MYSQL-python (pip install mysqlclient-1.4.4-cp38-cp38-win32.whl)- Binary file is attached in Zip file
7)	Pandas (pip install pandas)
8)	Django (pip install Django)

Steps to follow:
----------------
1)Make sure your MYSQL service is up and running. 
2)Extract the file provided(kxk190026_cs6360.zip)
3)In any of Python editor, import the Library Portal folder into the editor.
4)Run TableConstruction.py to construct the database
5)Run DBInitialization.py to populate the database.
6)Initialize the Django virtual environment if required
7)Run manage.py in the Library portal to start the server.
-Type, python manage.py makemigrations
-Type, python manage.py migrate
-Type, python manage.py createsuperuser, to create a superuser. Enter user name and password.
-To run server, type, python manage.py runserver
8)After you run the developement server, go the link (127.0.0.1:8000) in the google chrome and start using the application for library operations.
