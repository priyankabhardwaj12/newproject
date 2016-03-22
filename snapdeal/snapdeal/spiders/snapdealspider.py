from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import urllib
from scrapy.contrib.linkextractors import LinkExtractor
import urllib2
from BeautifulSoup import BeautifulSoup
from snapdeal.items import SnapdealItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
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

class snapdSpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "s"
	allowed_domains = ['www.snapdeal.com']
	start_urls =['http://www.snapdeal.com/product/avonzz-water-tank-overflow-alarm/637406203854#bcrumbLabelId:790']

	rules = (
		#Rule(SgmlLinkExtractor(allow=(".*/building-material?.*", ), unique=True), callback='parse_item', follow= True),
		Rule(SgmlLinkExtractor(allow=(".*http://www.snapdeal.com/products/.*", ), unique=True), callback='parse_item', follow= True),
		Rule(SgmlLinkExtractor(allow=(".*/product/.*", ), unique=True), callback='parse_item', follow= True),
		)
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.count = 0
		self.csvfile =  open('document.csv', 'a')
		self.spamwriter = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	
	def parse(self, response) :
		print ">>>>>", response.request.url 
		sel = Selector (response)
		items=[]
		data = []
		data1 = []
		item =  SnapdealItem()
		self.driver.get(response.url)
		item['url'] = response.request.url
		#import pdb;pdb.set_trace()
		item['title'] = sel.xpath('//h1[@itemprop="name"]/text()').extract()
		item['Product_id'] = str(item['url']).split('/')[-1].replace("#bcrumbLabelId:892","")
		brand = sel.xpath('//i[@itemprop="name"]/text()').extract()
		item['brand'] = brand
		price = str(list(map(unicode.strip,sel.xpath('//p[@class="product-offer-price"]/text()').extract())))
		price = price.replace("Rs.","").replace("[","").replace("]","").replace("u'","").replace(",","").replace("'","")
		item['price'] = price
		desc1 = str(list(map(unicode.strip,sel.xpath('//ul[@class="dtls-list clear"]//li//text()').extract())))
		desc1 = desc1.replace("[","").replace("]","").replace("u'","")
		item['desc1'] = desc1
		desc = str(list(map(unicode.strip,sel.xpath('//div[@itemprop="description"]//text()').extract())))
		desc = desc.replace("[","").replace("]","").replace("u'","")
		item['desc'] = desc
		try:
			
			saller =  str(list(map(unicode.strip,sel.xpath('//a[@class="pdp-e-seller-info-name reset-margin"]/text()').extract())))
			saller = saller.replace("u'","").replace("[","").replace("]","")
		except: pass
		item['Saller'] = saller
		category_path = sel.xpath('//div//span[@itemprop="title"]/text()').extract()
		level = len(category_path)
		item['level'] = level
		category_path = str(category_path).replace("u'","").replace("Home',","").replace("[","").replace("]","").replace('"','').replace("'","")
		item['category_path'] = category_path
		for o1 in self.driver.find_elements_by_xpath('//*[@id="attribute-select-0"]/ul//li'):
			variant1 = o1.text
			print"var1",variant1
			if o1:o1.click()
			time.sleep(5)					
			for x2 in self.driver.find_elements_by_xpath('//span//ul/li[@class="rippleGrey btn btn-toggle pdpAttr attrActive"]'):
				variant2 = x2.text
				print"var2",variant2
				if x2:x2.click()
				time.sleep(5)
				for x1 in  self.driver.find_elements_by_xpath('//*[@id="buyPriceBox"]/div[3]/div[2]/span[2]/span'):
					price = x1.text
					item['price'] = price.encode('ascii', 'ignore').replace(",","")
					#len(item['price'])
					Variant = variant1 , variant2
					item['Variant'] = str(Variant)
					self.spamwriter.writerow(item["price"])
					print "----", self.count, item["price"],item['Variant']
					self.count += 1
					data.append(item["price"])
					data1.append(item['Variant'])
					print len(data)
		item1 = BaseProducts()	
		item1.brand_name = item['brand'][0]
		item1.title = item['title'][0]
		item1.Product_id = item['Product_id']
		item1.Sku = item['title'][0]
		item1.category_name=  "Building Material"
		item1.description=item['desc']
		item1.additional_information = item['desc1']
		item1.source_url = item['url']
		try:
			item1.unit_measurements = item['um'][0]
		except:	item1.unit_measurements = ""
		item1.source_id = 2
		item1.save()
		item2 = Subscribe_Product()
		item3 = SPM()
		item2.bp = item1
		item2.source_id =2
		item2.Sku = item['title'][0]
		item2.save()
		item3.sp = item2
		item3.Sku = item['title'][0]
		try:
			item3.price = float(item['price'])
		except : item3.price = 0
		item3.source_id = 2
		item3.saller = item['Saller']
		item3.save()
		item4 = Category()
		item4.category_name = "Building Material"
		item4.category_path = item['category_path']
		item4.level = item['level']
		item4.source_id = 2
		item4.save()

		for y1 in range(len(data)):
			print"datadata", data[y1]
			print"datadata111",data1[y1]
			item2 = Subscribe_Product()
			item3 = SPM()
			item2.bp = item1
			item2.source_id =2
			item2.Sku = item['title'][0]
			item2.Variant = data1[y1]
			item2.save()
			item3.sp = item2
			item3.Sku = item['title'][0]
			try:
				item3.price = data[y1]
			except : item3.price = 0
			item3.source_id = 2
			item3.saller = item['Saller']
			item3.save()
			
		print item	
		return item

			
	