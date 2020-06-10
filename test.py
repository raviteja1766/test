def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("db.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans

def create_table1():
    query = """
    CREATE TABLE student(
        sid INT PRIMARY KEY, 
        name VARCHAR(16),
        login VARCHAR(32) UNIQUE, 
        age INT,
        gpa FLOAT 
    );"""
    write_data(query)
    
def create_table2():
    query = """
    CREATE TABLE course(
        cid VARCHAR(32) PRIMARY KEY, 
        name VARCHAR(32) NOT NULL
    );"""
    write_data(query)
    
def create_table3():
    query = """
    CREATE TABLE enrolled(
        sid INT REFERENCES student (sid),
        cid VARCHAR(32) REFERENCES course (cid), 
        grade CHAR(1)
    );"""
    write_data(query)

def insert_data1():
    c1,c2,c3,c4,c5 = input().split()
    query = f"INSERT INTO student VALUES({int(c1)},\"{c2}\",\"{c3}\",{int(c4)},{float(c5)});"
    write_data(query)

def insert_data3():
    c1,c2,c3 = input().split()
    query = f"INSERT INTO enrolled VALUES({int(c1)},\"{c2}\",\"{c3}\");"
    write_data(query)

def insert_data2():
    c1,c2 = input().split()
    query = f"INSERT INTO course VALUES(\"{c1}\",\"{c2}\");"
    write_data(query)


def get_info():
    query=input()
    info = read_data(query)
    print(info)


def create_another_table():
    query = input()
    write_data(query)

def insert_another_values():
    query = input()
    info=read_data(query)
    table=input()
    print("------c---------")
    print("a-----b")
    for i in info:
        write_data(f"insert into \"{table}\" values(\"{i}\")")
