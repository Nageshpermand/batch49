"""
import sales
print a
"""

"""
import sales
print sales.a
"""

""" print in terminel like cd batch49/ & 
cd modules &   ls-l than it shows sales.py and app.py and  sales.pyc 
this sales.pyc is the buffer(compiler buffer)
that data stored in pyc if u delet sales.py and execute with .pyc it shows result 
"""

"""
b=20
import sales
print b
print sales.a
sales.fun()
"""

"""
if we edit data in sales.py it will  edit in only .pyc 
10:12  sales.py
10:12 sales.pyc         after edit some data

10:12 sales.py
10:14 sales.pyc
        observe the timing of sales.pyc latest timing in updated timing pyc file

if we delete  sales.pyc in folder then execute app.py it shows results
"""


""" import sales """

"""
import sales
import sales
import sales
import sales
                    prints only one time
"""


"""
 if we replacing sales.py in anathor home folder   then exectute app.py we get output because there is sale.pyc 
"""
"""
if we replce  sales.py and sales.pyc in anathor home folder  then exectute  app.py we dont get output 
 """

""" 
 so we can use import sys
                   import sys.path  
                                   and then type import sales and execute app.py then we get output
out put shows in list first  shows current directory batch49/modules next python folders next linux next 
some system main paths  
"""


""" in the above list the batch/49/modules are 0 th position in list """



"""
#import sales 
#import sys
#import sys.path

"""
"""
import sales
sys.path.append("/home/batch49/modules")
import sales.path
import sales
"""


""" this after creating pur sub folder """


"""
import  pur 
"""
"""
there is no module named pur
"""
"""
noe create anathor folder sale file1.py
"""

#import pur.file2
#from pur import file2

"""
import pur
print pur.file1.a
"""

"""
import pur
print pur.file1.a
print pur.file1.b
pur.file1.fun()
"""

"""
from pur import file1
import pur
print pur.file1.a
print pur.file1.b
pur.file1.fun()
"""

from pur import file1
print file1.a


















