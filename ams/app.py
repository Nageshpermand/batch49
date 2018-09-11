"""
import db_operation
while True:
	   print
       1. insert
       2. update
       3.delete
       4.show
       q. quit
       
    
        opt=raw_input("Enter option: ")
        if opt.lower()=="q" or opt.lower()=="quit":
            print "thank you"
            break
        if opt=="1":
            db_operation.insert()
        elif opt=="2":
            db_operation.update()
        elif opt=="3":
            db_operation.delete()
        elif opt=="4":
            db_operation.browse()
        else:
            print "wrong option"
"""



import data_operation
while True:
    print """
    1. insert
    2. update
    3. delete
    4. show
    q. quit
    """
    opt = raw_input("Enter an option:")
    if opt.lower()=="q" or opt.lower()=="quit":
        print "thank you!!"
        break
    if opt=="1":
        data_operation.insert()
    elif opt=="2":
        data_operation.update()
    elif opt=="3":
        data_operation.delete()
    elif opt=="4":
        print data_operation.browse()
    else:
        print "wrong option"



    

