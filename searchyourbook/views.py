from django.shortcuts import render
from django.db import connection
from .models import Book, Authors, BookAuthors
from datetime import datetime, timedelta


end_date = datetime.today() + timedelta(days=14)
end_date = end_date.strftime("%m/%d/%y")

cursor = connection.cursor()
cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
def index(request):
    books = ""
    msg = ""
    fetch = True
    if(request.method == "POST"):
        if('search' in request.POST):
            fetch = False
            seach_keys = request.POST['search'].split(',')
            print(seach_keys)
            check_cond = ""
            select_query = "select BA.Isbn, BA.Title, BA.Authors, BA.Availability from (select Book.Isbn, Book.Title, GROUP_CONCAT(Authors.Name) Authors, Book.Availability from Book,Book_Authors,Authors where Book_Authors.Author_id = Authors.Author_id AND Book.Isbn = Book_Authors.Isbn GROUP BY Book.Isbn) as BA where "
            for key in seach_keys:
                key = key.strip()
                key = "%" + key + "%"
                if(check_cond != ""):
                    check_cond += " AND "
                check_cond += "(BA.Isbn LIKE '"+key+"' OR BA.Title LIKE '"+key+"' OR BA.authors LIKE '"+key+"')"

            query = select_query + check_cond
            print(query)
            cursor.execute(query)
            books = cursor.fetchall()
            print(books)
            ret_msg = {'books':books,'msg':"",'fetch':fetch}
            return render(request,'searchyourbook/index.html',context = ret_msg)

        elif('cardno' in request.POST):
#            print("the card no is " + request.GET['cardno'])
#            print(request.POST['cardno'])
#            search_keys = request.POST['cardno'].split(',')
#            print(search_keys)
            cardno = request.POST['cardno']
            isbn = request.POST['isbn']
            print(cardno,isbn)
            query = "SELECT COUNT(Card_id) FROM Borrower WHERE Card_id = '"+cardno+"' GROUP BY Card_id"
            cursor.execute(query)
            print(query)
            result_count = cursor.fetchone()
            print(result_count)
            if(result_count!= None):
                print("Passing the fetone")
                query = "SELECT COUNT(Loan_id) FROM Book_Loans WHERE Book_Loans.Card_id = '"+str(cardno)+"' AND Book_Loans.Date_in IS NULL GROUP BY Book_Loans.Card_id"
                cursor.execute(query)
                print(query)
                result = cursor.fetchone()
                print(result)
                if(result == None):
                    query = "SELECT Book.Availability FROM Book WHERE Book.Isbn = '"+isbn+"'"
                    print(query)
                    cursor.execute(query)
                    availability = cursor.fetchone()
                    print(availability)
                    if(availability == None):
                        msg = "Are you sure the ISBN is correct? Looks like not!"
                        return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})

                    if(availability[0] == 1):
                        query = 'INSERT INTO Book_Loans(Isbn, Card_id, Date_out, Due_date, Date_in) VALUES("'+ isbn +'","'+ str(cardno) +'",CURDATE(),DATE_ADD(Date_out,INTERVAL 14 DAY),NULL)'
                        cursor.execute(query)
                        print(query)
                        query = 'UPDATE Book SET Book.Availability = "0" WHERE Book.isbn = "'+isbn+'"'
                        cursor.execute(query)
                        msg = "Here ya go! You've got your book until "+ end_date
                        return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
                    else:
                        msg = "Sorry! Seems like the book is not available"
                        return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
                else:
                    print("Am i coming here")
                    query = "SELECT Book.Availability FROM Book WHERE Book.Isbn = '"+isbn+"'"
                    availability =cursor.execute(query)
                    if(availability == None):
                        msg = "Are you sure the ISBN is correct? Looks like not!"
                        return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
                    if(result[0] < 3):
                        query = 'INSERT INTO Book_Loans(Isbn, Card_id, Date_out, Due_date, Date_in) VALUES("'+ isbn +'","'+ str(cardno) +'",CURDATE(),DATE_ADD(Date_out,INTERVAL 14 DAY),NULL)'
                        cursor.execute(query)
                        query = 'UPDATE Book SET Book.Availability = "0" WHERE Book.isbn = "'+isbn+'"'
                        cursor.execute(query)
                        msg = "Here you go! You've got your book until "+ end_date
                        return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
                    else:
                        msg = "Sorry! You've reached the quota of maximum three books"
                        return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
                    return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})

            else:
                msg = "Uh Oh! Card-ID Invalid!"
                return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
        else:
            return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
    else:
        return render(request,'searchyourbook/index.html',{'books':books,'msg':msg,'fetch':fetch})
