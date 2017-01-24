import re

if re.match("\d+", "123 USD"):
    print ("Match")

if re.match("[a-zA-Z ]+\d+","Price is 123 USD"):
    print ("Match")

result = re.search("\d+","Price is 123 USD") 
if result:
    print (result.group(0))

result = re.search(".*(\d+)", "File size if 12345 bytes") 
if result:
    print (result.group(1))

result = re.search(".*?(\d+)", "File size if 12345 bytes") 
if result:
    print (result.group(1))

result = re.findall("(\d){1}","Color from pixel 20,30 is 123") 
if result:
    print (result)

import re
print (re.split("\d\d+","Color from pixel 20,30 is 123"))
print (re.split("(\d)\d+","Color from pixel 20,30 is 123"))
print (re.split("(\d)(\d+)","Color from pixel 20,30 is 123"))
s = "Today I'm having a python course"
print (re.split("([^a-z']+)", s))
print (re.split("([^a-z'])+", s))

s = "File config.txt was created on 2016-10-20 and has 12345 bytes"
result = re.search("File\s+(?P<name>[a-z\.]+)\s.*(?P<creation_date>\d{4}-\d{2}-\d{2}).*?(?P<size>\d+)", s)
print(result.groupdict())

s = "12345abc54321"
result = re.search("(?s)([A-Z]+)",s) 
if result:
    print(result.group(1))