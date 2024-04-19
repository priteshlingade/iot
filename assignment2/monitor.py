def print_all():

    import dbconn
   # empid=int(input("enter empid"))
    
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = "select * from emp;"
    #val = (empid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query)

    result=cursor.fetchall()

    # commit the changes
    #conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()
    return result

def dep():
    import dbconn
    department=input("enter department : ")
    
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = f"select * from emp where department= %s;"
    val = (department, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query, val)

    # commit the changes
    #conn.commit()
    data=cursor.fetchall()
    # close cursor as well as connection
    cursor.close()
    conn.close()
    return data

def sallary():
    import dbconn
    #salary=int(input("enter empid"))
    
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = "select * from emp order by salary DESC LIMIT 1"
    #val = (empid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query)

    result=cursor.fetchall()

    # commit the changes
    #conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()
    return result

def low():
    import dbconn
    #salary=int(input("enter empid"))
    
    # get connection
    conn = dbconn.get_connection()

    # form a query
    query = "select * from emp order by salary ASC LIMIT 1"
    #val = (empid, )

    # create a cursor
    cursor = conn.cursor()

    # execute the query
    cursor.execute(query)

    result=cursor.fetchall()

    # commit the changes
    #conn.commit()

    # close cursor as well as connection
    cursor.close()
    conn.close()
    return result