from datetime import timedelta
import datetime
n=int(input())
x=[]
y=[]
for i in range(0,n) :
		x.append(input())
		y.append(input())		
format = '%a %d %b %Y %H:%M:%S %z' # The format 
for i in range(0,n):
		t1=datetime.datetime.strptime(str(x[i]),format)
		t2=datetime.datetime.strptime(str(y[i]),format)
		t3=abs(t1-t2)
		print(int(t3.total_seconds()))
		#print(t1,t2,t3,sep='\n')
	    #total_seconds = tq.second + pt.minute*60 + pt.hour*3600
		#print(t3.timedelta.total_seconds())
		#print(t2.minute)
#format = "%b %d %Y %r" # The format 
#t1 = time.strftime(format, time.gmtime(datetime_str)) 
#Sun 10 May 2015 13:54:36 -0700
#print(int(x[11:15]),int(x[5:7]),sep=' ') 
#print(fromisoformat(x))
#year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
#t1=datetjme.datetime(int(x[11:15)]),int(x[5:6)]),int(x[)])nt(x[11:15)])nt(x[11:15)])nt(x[11:15)])