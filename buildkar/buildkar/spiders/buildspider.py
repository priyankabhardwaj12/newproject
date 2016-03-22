from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from buildkar.items import BuildkarItem
import re,sys, os
import sys, traceback
from scrapy.contrib.linkextractors import LinkExtractor
import urllib2
from bs4 import BeautifulSoup

sys.path.append('/home/supplified/mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from products.models import BaseProducts
from products.models import SPM
from products.models import Category
from products.models import Subscribe_Product

class buildkSpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "bk"
	start_urls =['http://buildkar.com/building-materials/blocks/',
'http://buildkar.com/building-materials/boards-planks/',
'http://buildkar.com/building-materials/boards-planks/page/2/',
'http://buildkar.com/building-materials/bricks/']
	rules = (
		Rule(SgmlLinkExtractor(allow=(".*/building-materials/cement-rmc/.*", ),deny=(".*add-to-cart=.*",), unique=True), callback='parse_item', follow= True),
		Rule(SgmlLinkExtractor(allow=(".*/page/.*", ), unique=True), callback='parse_item', follow= True),
		)
	def parse(self, response) :
		#print ">>>>>", response.request.url
		sel = Selector (response)
		items = []
		item = BuildkarItem ()
		# item['url'] = response.request.url
		# #import pdb;pdb.set_trace()
		# title = (map(unicode.strip,sel.xpath('//h3[@class="heading-title product-title"]//a/text()').extract()))
		# #print len(title)
		# item['title'] = title
		# category = (map(unicode.strip,sel.xpath('//div[@class="product-meta-wrapper"]/div[@class="wd_product_categories"]/a/text()').extract()))
		# item['category'] = category
		# price1 = (map(unicode.strip,sel.xpath('//span[@class="price"]/del/span[@class="amount"]/text()').extract()))
		# item['price1'] = price1
		# price = (map(unicode.strip,sel.xpath('//ins/span[@class="amount"]/text()').extract()))
		# item['price'] = price
		item['href'] = sel.xpath('//h3[@class="heading-title product-title"]/a/@href').extract()
		# print len (item['href'])
		# description = []
		# for i in range (len(item['href'])) :
		# 	url = item['href'][i]
		# 	html_doc = urllib2.urlopen (url)
		# 	soup = BeautifulSoup (html_doc.read ())
		# 	raw_data = soup.find('div',{'id':"content_description"})
		# 	p =raw_data.text
		# 	print">>>>>",p
		# 	description.append (p)
		# for x1 in range(len(title)):
		# 	print title[x1]
		# 	item1 = BaseProducts()	
		# 	item1.source_url = item['url'][x1]
		# 	item1.Sku = title[x1]
		# 	item1.title = title[x1]
		# 	item1.category_name=category[x1]
		# 	item1.description = description[x1]
		# 	item1.source_id = 5
		# 	item1.save()
		# 	item2 = Subscribe_Product()
		# 	item3 = SPM()
		# 	item2.bp = item1
		# 	item2.source_id =5
		# 	item2.Sku = title[x1]
		# 	item2.save()
		# 	item3.sp = item2
		# 	item3.Sku = title[x1]
		# 	try:
		# 		item3.price = price[x1].replace("[","").replace(",","").replace("u","").replace("]","").replace("'","").replace("\xa0","").replace("Rs.","")
		# 	except : item3.price = 0
		# 	try:
		# 		item3.store_price = price1[x1].replace("[","").replace(",","").replace("u","").replace("]","").replace("'","").replace("\xa0","").replace("Rs.","")
		# 	except: item3.store_price = 0
		# 	item3.source_id = 5
		# 	#item3.saller = item['Saller']
		# 	item3.save()
		# 	item4 = Category()
		# 	item4.category_name = category[x1]
		# 	item4.category_path = category[x1]
		# 	item4.level = "3"
		# 	item4.source_id = 5
		# 	item4.save()
		# 	if item['title'] :
		# 		# print item	
		return item	



