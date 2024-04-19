# import module of mysql connector
import mysql.connector
import delete
import update
import monitor
#from update import update_emp(empid,email)
# create a connection with mysql database server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "employee",
)

print("1 . delete ")
print("2 . update ")
print("3 . create ")
print("4 . print all records ")
print("5 . high salarry ")
print("6 . low salarry ")
print("7 . specific employee")

choice= int(input("enter choice : "))
if choice==3:
    # create a query
    empid = int(input("Enter empid : "))
    name = input("Enter name : ")
    department =(input("Enter department : "))
    email = input("Enter email :")
    salary = int(input("Enter salary : "))
    date_of_joining=input("Enter date of joining : ")

    query = f"insert into emp values({empid}, '{name}', '{department}', '{email}', '{salary}','{date_of_joining}');"

    # create a cursor to execute the query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # after execution of query commit your changes
    connection.commit()

    # close the cursor
    cursor.close()

    #close the connection with mysql server 
    connection.close()

if choice==2:
    empid=int(input("enter empid : "))
    email=input("enter new email : ")
    update.update_emp(empid,email)

if choice==1:
    delete.delete_emp()
    print("sucessfully deleted data")

if choice==4:
    all=monitor.print_all()
    print(all)
    print("data print sussfully")

if choice==5:
    data=monitor.sallary()
    print(data)
    print("data print sussfully")

if choice==6:
    data=monitor.low()
    print(data)
    print("data print sussfully")
if choice==7:
    data=monitor.dep()
    print(data)
    print("data print sussfully")










