
from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="241513",database="studentdetails")

def insert (id,name,age,city):
    res = con.cursor()
    sql = "INSERT INTO student_record (id, name, age, city) VALUES (%s, %s, %s, %s)"
    data = (id,name,age,city)
    res.execute(sql,data)
    con.commit()
    print("data updated")


def update (name ,age, city, id):
   res = con.cursor()
   sql = "UPDATE student_record SET name = %s, age = %s, city = %s WHERE id = %s"
   data = (name,age,city,id)
   res.execute(sql,data)
   con.commit()
   print("data updated")



def select ():
    res=con.cursor()
    sql="select id, name , age , city from student_record"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=['id','name','age','city']))



def delete (id):
    res = con.cursor()
    sql="delete from student_record where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("data deleted")


while True:
    print("1.Insert date")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        id=int(input("Enter student id"))
        name=input("Enter your name:")
        age=input("Enter your age:")
        city=input("Enter your city:")
        insert (id,name,age,city)


    elif choice==2:
        id = input("Enter student id")
        name = input("Enter your name:")
        age = input("Enter your age:")
        city = input("Enter your city:")
        update ( name, age, city, id )

    elif choice==3:
        select()

    elif choice==4:
        id = int(input("Enter student id to delete:"))
        delete(id)

    elif choice==5:
        exit()

    else:
        print("Invalid choice")