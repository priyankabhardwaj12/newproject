from scrapy.selector import Selector
from selenium import selenium
from selenium import webdriver
from msupply.items import MsupplyItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
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
sys.path.append('/home/supplified/Desktop/parsing')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parsing.settings")
from product.models import SPM
class msupplySpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "m1"
	allowed_domains = ["www.msupply.com/"]
	start_urls =['http://www.buildzar.com/delhi/aerocon-cpvc-plumbing-pipes-3m/p/4632']
	rules = (
		Rule(SgmlLinkExtractor(allow=("", ), unique=True), callback='parse_item', follow= True),
		)
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.count = 0
		self.csvfile =  open('document.csv', 'a')
		self.spamwriter = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	def parse(self, response) :
		data = []
		self.driver.get(response.url)
		o1 = self.driver.find_element_by_xpath('//*[@id="0"]/span')
		x = o1.click()
		y = self.driver.find_element_by_xpath('//*[@id="product-options-wrapper"]/div/div/ul[2]/li/label/span')
		y1 = y.click()
		time.sleep(5)
		#for x in range(0,40): o1.click()
		#import pdb;pdb.set_trace()
		for x1 in  self.driver.find_elements_by_xpath('//*[@id="selling-price-displayed"]'):
			item = MsupplyItem ()
			#item["url"] = x1.get_attribute('href')
			price = x1.text
			item['price'] = price.encode('ascii', 'ignore').decode('ascii')
			print">>>>>>>>>>>>",item['price']
			item['variant'] = o1.text
			print "______________",item['variant']
			item['subvariant'] = y.text
			print "...........",item['subvariant']
			item["source"] = response.url
			self.spamwriter.writerow([item["price"], item["source"],item['variant'],item['subvariant']])
			print "----", self.count, item["price"]
			self.count += 1
			data.append(item)
		item1 = SPM()
		item1.store_price = item['price']
		return item

	