try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import re
urlInfo = "http://profs.info.uaic.ro/~orar/orar_profesori.html"
r = re.compile("<li><a\shref=\"[^\"\.]*\.html\">.*([A-Za-z\.\s,]+)<\/a>")

try:
    response = urlopen(urlInfo).read().decode("utf-8")
    for mo in r.finditer(response):
        print (mo.group(1).strip())
except Exception as e:
    print ("Error -> ",e)


urlManagement = "http://www.info.uaic.ro/bin/Structure/Management"
r = re.compile("Dean.*<a href=\"[^\"]+\">([A-Za-z\s]+)")

try:
    response = urlopen(urlManagement).read().decode("utf-8")
    obj = r.search(response)
    if obj:
        print("Dean", obj.group(1))
except Exception as e:
       print ("Error -> ",e)