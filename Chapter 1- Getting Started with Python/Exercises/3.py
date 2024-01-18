#import date and time 
import datetime
#get the current date and time
now = datetime.datetime.now()
#format
dt_string=now.strftime("%d/%m/%Y %H:%M:%S")
#then print
print(dt_string)