from datetime import datetime
import sys

def timeConversion(s):
    return datetime.strptime(s, '%I:%M:%S%p').strftime('%H:%M:%S')#strptime() reads the string as a datetime and strftima() convert it back to string 

s = input().strip()
result = timeConversion(s)
print(result)
