import sqlite3 as sql
con=sql.connect('becdb')
con.execute('''
    create table employee(employee_id int,first_name varchar2(25),last_name varchar2(25),email varchar2(25),
	 phone_number int,hiredate varchar2(25),job_id int,salary int,commission_pct int,manager_id int,department_id varchar2(25));''')
		 
con.execute('''
    insert into employee values(103,'madhu','k','madhupriya@gmail.com',9999999999,'30-04-2002',32,24000,3500,302,'ece01');  ''' )
		
con.execute('''
    insert into employee values(104,'poojitha','k','poojitha@gmail.com',988888888,'03-06-2002',31,24000,3500,302,'cse01');  ''' )
	
con.execute('''
    insert into employee values(111,'sweety','g','sweety123@gmail.com',7777777777,'23-04-2002',32,25000,2500,301,'ece01');  ''' )
	
con.execute('''
    insert into employee values(112,'munny','m','munny23@gmail.com',9090090900,'21-04-2003',32,10000,300,302,'cse01');  ''' )
	
rd=con.execute('''
       select * from employee; ''')
	   
for i in rd:
	print(i)

m=con.execute(''' select avg(salary),count(employee_id),department_id from employee group by department_id having count(employee_id)>10; ''')
for k in m:
	print(k)