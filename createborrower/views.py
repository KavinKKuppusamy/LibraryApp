from django.shortcuts import render
from django.db import connection
from createborrower.models import Borrower
import re
def index(request):
	check_ssn = False
	msg = ""
	cursor = connection.cursor()
	if(request.method == "POST"):
		first_name = request.POST['fname']
		ssn = request.POST['ssn']
		print(ssn)
		if re.match(r"^[0-9]{2}-{1}[0-9]{2}-{1}[0-9]{4}$", ssn):
			check_ssn = True
			print("SSN is in wrong format!")
			return render(request,'createborrower/index.html',{'check_ssn':check_ssn,'msg':msg})
		address = request.POST['address']
		phone = request.POST['phone']
		phone = '('+phone[0:3]+') '+phone[3:6]+'-'+phone[6:]
		query = "SELECT Ssn FROM Borrower WHERE Ssn = '" + ssn + "'"
		cursor.execute(query)
		if(cursor.fetchone() != None):
			check_ssn = True
		else:
			query = 'INSERT INTO Borrower(Ssn,Bname,Address,Phone) VALUES("'+ ssn +'","'+ first_name +'","'+ address +'","'+ phone +'");'
			cursor.execute(query)
			msg = "Hey " +first_name + "! You have become a member of this Library!"

	return render(request,'createborrower/index.html',{'check_ssn':check_ssn,'msg':msg})
