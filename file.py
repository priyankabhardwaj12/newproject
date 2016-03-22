import csv
import urllib
from BeautifulSoup import BeautifulStoneSoup
import os
import subprocess
import re
i=0
with open('Products_Report.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		x= row[0].split(',')[0]
		print x
		if len(x)==13:
			direct_output=subprocess.check_output ('''curl 'http://eandata.com/lookup.php?extra=x&code=%s&mode=prod&show=&force=&ajax=1' -X POST -H 'Cookie: __utma=115798290.2112697394.1402473688.1402473688.1402480532.2; __utmb=115798290.2.10.1402480532; __utmc=115798290; __utmz=115798290.1402473688.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=ijfo2t8t3uq916r2vl8v6co6o1' -H 'Origin: http://eandata.com' -H 'Accept-Encoding: gzip,deflate,sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Cache-Control: max-age=0' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'Referer: http://eandata.com/lookup/%s/' -H 'Content-Length: 0' --compressed'''%(x,x),shell=True)
			Soup = BeautifulStoneSoup(direct_output)
			#Soup.findAll(attrs={"id" : "price_new"})
			#print Soup.prettify()
			for a in Soup.findAll('div',{'class':'two-col-grid-row'}):
				      x =a.find('div',{'class':'cell-z'}).text
				      if x != 'No':
					 if x != 'Search Google':
						if x[2] != '-':
						   if x[0] != 'B' and x[1] != '0' and x[2] != '0':
							       print x.replace('&nbsp;&nbsp;','')
