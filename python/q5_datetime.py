# Hint:  use Google to find python function

####a) 
from datetime import datetime

date_start = '01-02-2013'  
date_stop = '07-28-2015'

dstart = datetime.strptime(date_start, "%m-%d-%Y")
dstop = datetime.strptime(date_stop, "%m-%d-%Y")
days_between = dstop - dstart	

print(days_between.days)

####b)  
from datetime import datetime

date_start = '12312013'  
date_stop = '05282015'  

dstart = datetime.strptime(date_start, "%m%d%Y")
dstop = datetime.strptime(date_stop, "%m%d%Y")

days_between = dstop - dstart	

print(days_between.days)

####c)  
from datetime import datetime

date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

dstart = datetime.strptime(date_start, "%d-%b-%Y")
dstop = datetime.strptime(date_stop, "%d-%b-%Y")

days_between = dstop - dstart	

print(days_between.days)