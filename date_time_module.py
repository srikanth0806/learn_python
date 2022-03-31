Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime
>>> 
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> 
>>> 
>>> from datetime import time
>>> 
>>> dir(time)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dst', 'fold', 'fromisoformat', 'hour', 'isoformat', 'max', 'microsecond', 'min', 'minute', 'replace', 'resolution', 'second', 'strftime', 'tzinfo', 'tzname', 'utcoffset']
>>> 
>>> datetime.time.hour
<attribute 'hour' of 'datetime.time' objects>
>>> time.hour
<attribute 'hour' of 'datetime.time' objects>
>>> time.max
datetime.time(23, 59, 59, 999999)
>>> datetime.time.max
datetime.time(23, 59, 59, 999999)
>>> time.min
datetime.time(0, 0)
>>> time.minute
<attribute 'minute' of 'datetime.time' objects>
>>> time.minute()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    time.minute()
TypeError: 'getset_descriptor' object is not callable
>>> x = time.now()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x = time.now()
AttributeError: type object 'datetime.time' has no attribute 'now'
>>> time.dst()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    time.dst()
TypeError: unbound method time.dst() needs an argument
>>> from datetime import date
>>> dir(date)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'ctime', 'day', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'timetuple', 'today', 'toordinal', 'weekday', 'year']
>>> 
>>> 
>>> date.ctime()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    date.ctime()
TypeError: unbound method date.ctime() needs an argument
>>> date.today()
datetime.date(2021, 8, 29)
>>> x = date.today()
>>> x
datetime.date(2021, 8, 29)
>>> 
>>> 
>>> date.ctime(x)
'Sun Aug 29 00:00:00 2021'
>>> x.today
<built-in method today of type object at 0x00007FFC0B1D5990>
>>> x.day
29
>>> x.month
8
>>> x.year
2021
>>> x.week
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    x.week
AttributeError: 'datetime.date' object has no attribute 'week'
>>> x.weekday
<built-in method weekday of datetime.date object at 0x000001E69E374C50>
>>> x.weekday()
6
>>> date.max
datetime.date(9999, 12, 31)
>>> date.min
datetime.date(1, 1, 1)
>>> x.strftime("%d-%m")
'29-08'
>>> x.strftime("%d-%m-%y")
'29-08-21'
>>> x.strftime("%d-%m-%Y")
'29-08-2021'
>>> x.strftime("%d-%M-%Y")
'29-00-2021'
>>> x.strftime("%d-%m-%Y")
'29-08-2021'
>>> x.strftime("%d-%m-%Y: %a")
'29-08-2021: Sun'
>>> 
>>> 
>>> 
>>> from datetime import datetime
>>> 
>>> dir(datetime)
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']
>>> 
>>> 
>>> 
>>> x = datetime.now()
>>> x
datetime.datetime(2021, 8, 29, 9, 53, 18, 336312)
>>> 
>>> 
>>> x.day
29
>>> x.month
8
>>> x.weekday
<built-in method weekday of datetime.datetime object at 0x000001E69E42D9F0>
>>> x.weekday()
6
>>> x.hour
9
>>> x.minute
53
>>> x.second
18
>>> x.microsecond
336312
>>> 