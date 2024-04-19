import delete
import update
import mysql.connector

print("1 . delete ")
print("2 . update ")
#print("3 .  ")

choice= int(input("enter choice : "))

if choice==1:
    empid=int(input("enter empid"))
    delete_emp(empid)
    print("sucessfully deleted data")

if choice==2:
    empid=int(input("enter empid"))
    empid=input("enter new email")
    update_emp(empid,email)
    print("sucessfully updated data")

print("EXIT !")
