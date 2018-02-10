from datetime import datetime

start_time='1/1/2016 00:09:55'
time_stamp = datetime.strptime(start_time,'%m/%d/%Y %H:%M:%S')
print(time_stamp.strftime('%m'))
print(time_stamp.strftime('%H'))
print(time_stamp.strftime('%A'))
