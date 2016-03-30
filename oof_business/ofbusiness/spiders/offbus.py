# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib2
import csv
import urllib
import re
import re, sys, os
sys.path.append('/home/supplified/mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from products.models import Category
from products.models import BaseProducts
from products.models import SPM
from products.models import Subscribe_Product
data=[]
count=0
list_open = open("d.text")
read_list = list_open.read()
spamreader = read_list.split("\n")
for row in spamreader:
	d=row	#print 'Reading rows ..' ,row
	#print '.',
	content = urllib.urlopen(d).read()
	soup = BeautifulSoup(content)
	sp_price = 0
	price = 0
	for x in soup.findAll('div',{"class":"productTitle"}):
		title = x.text.encode('ascii', 'ignore')
		#print title
	for x1 in soup.findAll('a',{'class':"categoryName"}):
		category = x1.text.encode('ascii', 'ignore')
		#print category
	for x2 in soup.findAll('div',{'class':"productDescription"}):
		desc = x2.text.encode('ascii', 'ignore')
		#print desc
	for x3 in soup.findAll('ul',{'class':"pdpSpecDetails"}):
		desc1 = x3.text.encode('ascii', 'ignore')
		#print desc1	
	for x4 in soup.findAll('div',{'class':"sellerName"}):
		saller = x4.text.replace("Sold by:","")
		#print seller
	for x5 in soup.findAll('div',{'class':"estimateDeliveryPan"}):
		delev = x5.text
		#print delev		
	for x6 in soup.findAll('div',{'class':"productTotalPrice"}):
		y = x6.findAll('span')[0].string.replace(",","").rsplit(" ")
		price = y[1]
	code = d.split('/')[-1]
		
	item1 = BaseProducts()
	item1.title = title
	item1.Sku = title
	item1.Product_id = code
	item1.category_name= category
	item1.description = desc
	item1.additional_information = desc1
	item1.source_url = d
	item1.source_id = 6
	item1.save()
	item2 = Subscribe_Product()
	item3 = SPM()
	item2.bp = item1
	item2.source_id =6
	item2.Sku = title
	item2.save()
	item3.sp = item2
	item3.Sku = title
	try:
		item3.price = float(price)
	except : item3.price = 0
	item3.source_id = 6
	item3.saller = saller
	item3.save()
	item4 = Category()
	item4.category_name = category
	item4.category_path = category
	item4.level = 3
	item4.source_id = 6
	item4.save()