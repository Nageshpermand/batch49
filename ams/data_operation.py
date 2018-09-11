def get_con():
	con = psycopg2.connect(host="localhost",user="postgres",
	                    password="nag5306",port=5432,database="batch49")
    cur = con.cursor()
    return con,cur

def browse(cust_id=None):
	q="select * from customer"
	if cust_id:
		q=q+"where id=%s"%cust_id
	con,cur=get_con()
	cur.execute(q)
	data=cur.fetchall()
	con.close()
	return data

def insert():
	cust_id=raw_input("enter customer id: ")
	cust_name=raw_input("enter customer name: ")
	q="insert into values(%s, '%s')"%(cust_id, cust_name)
	con,cur=get_con()
	cur.execute(q)
	con.commit()
	con.close()
	print"insertion done!!"
def update():
	cust_id=raw_input("enter customer id:")
	if cust_id:
		print browse(cust_id)
		flag=raw_input("do you want to update: (y/n")
		if flag.lower()=="y" or flag.lower()=="yes":
            cust_name=raw_input("enter customer name: ")
            con,cur=get_con()
	        q="update customer set name='%s' where id=%s"%(cust_name,cust_id)
	        cur.execute(q)
	        con.commit()
	        con.close()
	    print browse(cust_id)
	    print "updation done!!"
	else:
		print"please enter customer id"

def delete():
	cust_id=raw_input("enter customer id:")
	if cust_id:
		print browse(cust_id)
		flag=raw_input("do you want to delete: (y/n")
		if flag.lower()=="y" or flag.lower()=="yes":
            con,cur=get_con()
	        q="delete from  customer where id=%s"%(cust_id)
	        cur.execute(q)
	        con.commit()
	        con.close()
	    print browse(cust_id) 
	    print "deletion done!!"
	else:
		print"please enter customer id"




"

