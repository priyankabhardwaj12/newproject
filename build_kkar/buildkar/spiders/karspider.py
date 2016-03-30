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
	name = "bk1"
	allowed_domains = ["buildkar.com"]
	start_urls =[ 'http://buildkar.com/']
	rules = (
		Rule(SgmlLinkExtractor(allow=(".*http://buildkar.com/shop/.*",),deny=(".*add-to-cart=.*",".*/building-materials/cement-rmc/.*")), follow= True),
		Rule(SgmlLinkExtractor(allow=(".*/page/.*",),),callback='parse_item', follow= True),
		#Rule(SgmlLinkExtractor(allow=(".*/sand/.*",),deny=(".*add-to-cart=.*",)),callback='parse_item', follow= True),

		)
	def parse_item(self, response) :
		try:
			#print ">>>>>", response.request.url
			sel = Selector (response)
			items = []
			item = BuildkarItem ()
			item['url'] = response.request.url
			#import pdb;pdb.set_trace()
			title = sel.xpath('//h1[@itemprop="name"]/text()').extract()
			#print len(title)
			item['title'] = title
			category = sel.xpath('//nav[@itemprop="breadcrumb"]/a/text()').extract()
			level = len(category)
			item['level'] = level
			category = str(category).replace("u'","").replace("[","").replace("]","").replace("Home","").replace("',","")
			item['category'] = category
			try:
				item['brand'] = sel.xpath('//p[@itemprop="brand"]/text()').extract()
			except: pass	
			price1 = str(list(map(unicode.strip,sel.xpath('//p[@class="price"]/del/span[@class="amount"]/text()').extract())))
			price1 = price1.replace("u'","").replace("[","").replace("]","").replace("Rs.\\xa0","").replace("'","").replace('"','')
			item['price1'] = price1
			price =str(list(map(unicode.strip,sel.xpath('//p[@class="price"]//ins/span[@class="amount"]/text()').extract())))
			price = price.replace("u'","").replace("[","").replace("]","").replace("Rs.\\xa0","").replace("'","").replace('"','')
			item['price'] = price
			desc = str(list(map(unicode.strip,sel.xpath('//div[@id="content_description"]//text()').extract())))
			desc = desc.replace("u'","").replace("[","").replace("]","").replace("'","")
			item['desc'] = desc
			variant = sel.xpath('//input[@name="quantity"]/@min').extract()
			item['Variant'] = variant
			item1 = BaseProducts()	
			item1.source_url = item['url']
			item1.Sku = item['title'][0]
			item1.title = item['title'][0]
			item1.category_name = item['category']
			item1.description = item['desc']
			item1.source_id = 5
			item1.save()
			item2 = Subscribe_Product()
			item3 = SPM()
			item2.bp = item1
			item2.source_id =5
			item2.Sku = item['title'][0]
			item2.Variant = item['Variant'][0]
			item2.save()
			item3.sp = item2
			item3.Sku = item['title'][0]
			try:
				item3.price = item['price']
			except : item3.price = 0
			try:
				item3.store_price = item['price1']
			except: item3.store_price = 0
			item3.source_id = 5
			#item3.saller = item['Saller']
			item3.save()
			item4 = Category()
			item4.category_name = item['category']
			item4.category_path = item['category'] 
			item4.level = "3"
			item4.source_id = 5
			item4.save()
			if item['title'] and item['category'] and item['price'] and item['Variant']:
				return item
		except:pass		
