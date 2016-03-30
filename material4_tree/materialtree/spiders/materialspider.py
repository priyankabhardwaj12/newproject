from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
import urllib2
from BeautifulSoup import BeautifulSoup
from materialtree.items import MaterialtreeItem
from selenium import selenium
from selenium import webdriver
from scrapy.http import FormRequest
from scrapy import log
from time import strftime
from datetime import timedelta
from datetime import datetime
import datetime
from time import sleep
from scrapy.selector import HtmlXPathSelector
import time
from scrapy.http import TextResponse
import re, sys, os
import urllib
import csv
import json
sys.path.append('/home/supplified/mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from products.models import Category
from products.models import BaseProducts
from products.models import SPM
from products.models import Subscribe_Product

class materialSpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "ms"
	allowed_domains = ['materialtree.com']
	start_urls =["http://www.materialtree.com/",]
	rules = (
		Rule(SgmlLinkExtractor(allow=(".*/building-materials.*",".*/.*", ), unique=True), callback='parse_item', follow= True),
		Rule(SgmlLinkExtractor(allow=(".*/plumbing.*", ".*/.*", ), unique=True), callback='parse_item', follow= True),
		
		)
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.count = 0
		self.csvfile =  open('jagdesh1.csv', 'a')
		self.spamwriter = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	def parse(self, response) :
		sel = Selector (response)
		data = []
		data1 = []
		items=[]
		item = MaterialtreeItem ()
		self.driver.get(response.url)
		time.sleep(2.5)
		item['url'] = response.request.url
		#import pdb;pdb.set_trace()
		item['title'] = sel.xpath('//div/h1/text()').extract()
		um1 = um2 = ""
		try:
			um1 = str(list(map(unicode.strip,sel.xpath('//span[@id="sellerPrice"]/text()').extract())))
			um1 = um1.split('/')[1]
			um1 = um1.replace("u'","").replace("Rs.","").replace("[","").replace("]","").replace("'","").replace('"','')
		except: pass	
		try:
			um2 = self.driver.find_element_by_xpath('//*[@id="ddContent"]/table/tbody//tr/td[6]')
			um2 = um2.text
			um2 = str(um2).replace("u'","")
			print "<<<<",um2
		except: pass 
		item['um'] = um2 or um1
		Sku1 = Sku2 = ""
		try:
			Sku1 = sel.xpath('//div[@class="sku"]/span[@class="value"]/text()').extract()
		except:pass
		try:
			Sku2 = sel.xpath('//div/h1/text()').extract()
		except: pass	
		item['Sku'] = Sku1 or Sku2
		try:
			item['Product_id'] = sel.xpath('//input[@name="productid"]/@value').extract()
		except: pass
		price11 = price22 = ""		

		try:
			price22 = self.driver.find_element_by_xpath('//*[@id="ddContent"]/table/tbody/tr[2]/td[7]/h5')
			price22 = price22.text
			price22 = str(price22).replace(".00","").replace(",","").replace("Rs","").replace("u'","")
			print ">>>",price22
		except: pass
		try:
			price11 = str(list(map(unicode.strip,sel.xpath('//span[@id="sellerPrice"]/text()').extract())))
			price11 = price11.split('/')[0]
			price11 = price11.replace("u'","").replace("Rs.","").replace("[","").replace("]","")
		except: pass
		item['price'] = price22 or price11
		try:
			seller = str(list(map(unicode.strip,sel.xpath('//span[@id="sold_by_name"]/a/text()').extract())))
			seller = seller.replace("u'","").replace("[","").replace("]","")
		except: pass
		item['Saller'] = seller
		#import pdb;pdb.set_trace()
		category = item['url'].split('/')[-1]
		category = str(category).split('-')[7:10]
		category = str(category).replace("'","").replace(",","").replace("[","").replace("]","")
		item['category'] = category
		desc = desc_new = ""
		try:
			desc = str(list(map(unicode.strip,sel.xpath('//div[@class="panel"]/div[@class="std"]/text()').extract())))
			desc = desc.replace("u'","").replace("[","").replace("]","")
		except:pass 
		try:
			desc_new = self.driver.find_element_by_xpath('//div[@id="category-description"]/p')
			desc_new = desc_new.text
			desc_new = str(desc_new).replace("u'","")
			print"......",desc_new
		except: pass 
		item['desc'] =  desc_new or desc
		try:
			desc1 = str(list(map(unicode.strip,sel.xpath('//table[@class="data-table"]/tbody//text()').extract())))
			desc1 = desc1.replace("u'","").replace("[","").replace("]","").replace("', ',","")
		except: pass	
		item['desc1'] = desc1
		brand1 = brand2 = ""
		try:
			brand1 = self.driver.find_element_by_xpath('//*[@id="ddContent"]/table/tbody//tr/td[3]')
			brand1 = brand1.text
			brand1 = str(brand1).replace("u'","")
		except: pass	
		try:
			brand2 = sel.xpath('//div[@class="brand-name attribute"]/text()').extract()
			brand2 = str(brand2).replace("u'","").replace("[","").replace("]","")
		except: pass
		item['brand'] = brand1 or brand2

		for x2 in  self.driver.find_elements_by_xpath("//*[@id='ddContent']/table/tbody//tr//h4"):
			price = x2.text
			item['price'] = price.encode('ascii', 'ignore').replace(",","").replace("Rs","")
			self.spamwriter.writerow(item['price'])
			print "----", self.count, item['price']
			self.count += 1
			data1.append(item['price'])
			
		row = self.driver.find_elements_by_xpath("//*[@id='ddContent']/table/tbody//tr")
		for x1 in row:
			variant = x1.text
			Variant = str(variant).split("/")[:2]
			item['Variant'] = Variant
			#print item['Variant']
			self.spamwriter.writerow(item['Variant'])
			print "----", self.count, item['Variant']
			self.count += 1
			data.append(item['Variant'])
			print">>>>>>>>", len(data)
			# if len(data)<7:
			# 	continue
			# else:break
			
		
		item1 = BaseProducts()	
		item1.brand_name = item['brand']
		item1.title = item['title'][0]
		try:
			item1.Product_id = item['Product_id'][0]
		except:
			item1.Product_id = ""
		item1.Sku = item['Sku'][0]
		#item1.category_name=  
		item1.category_name = item['category']
		item1.description=item['desc']
		item1.additional_information = item['desc1']
		item1.source_url = item['url']
		try:
			item1.unit_measurements = item['um']
		except:	item1.unit_measurements = ""
		item1.source_id = 3
		item1.save()
		item2 = Subscribe_Product()
		item3 = SPM()
		item2.bp = item1
		item2.source_id =3
		#item2.region_name = item['region_name']
		item2.Sku = item['Sku'][0]
		# item2.Variant = 
		item2.save()
		item3.sp = item2
		item3.Sku = item['Sku'][0]
		#item3.region_name = item['region_name']
		try:
			item3.store_price = float(item['price1'])
		except: item3.store_price = 0
		#item3.Delivery_time = item['Delivery_time']
		try:
			item3.price = float(item['price'])
		except : item3.price = 0
		item3.source_id = 3
		item3.saller = item['Saller']
		item3.save()
		item4 = Category()
		item4.source_id = 3
		item4.category_path = 'kitchen'+item['category']
		item4.category_name = item['category']
		item4.level = 3
		item4.save()
		for y1 in range(len(data)):
			print"datadata..........", data[y1]
			item2 = Subscribe_Product()
			item3 = SPM()
			item2.bp = item1
			item2.source_id =3
			item2.Sku = item['Sku'][0]
			item2.Variant = data[y1]
			item2.save()
			item3.sp = item2
			item3.Sku = item['Sku'][0]
			try:
				item3.price = data1[y1]
			except : item3.price = 0
			item3.source_id = 3
			item3.saller = item['Saller']
			item3.save()
			
		print item	
		return item
