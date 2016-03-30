from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from amazon.items import AmazonItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
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
import urllib2
import csv
import json

class amzSpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "az"
	allowed_domains = ['amazon.in']
	start_urls =["http://www.amazon.com/ROBERTSON-3P20116-eBallast-ISU232T8120-Robertson/dp/B00H4HNQ44/ref=lp_5789850011_1_2?s=lamps-light&ie=UTF8&qid=1458026062&sr=1-2"]
	#"http://www.amazon.com/b?ie=UTF8&node=495266"]
	rules = (
		Rule(SgmlLinkExtractor(allow=(".*http://www.amazon.com/s/ref=lp_495266_nr_n_.*",".*&page=.*", ), unique=True), callback='parse_item', follow= True),
		Rule(SgmlLinkExtractor(allow=(".*http://www.amazon.com/.*", ), unique=True), callback='parse_item', follow= True),
		)

	def parse(self, response) :
		print ">>>>>", response.request.url 
		sel = Selector (response)
		items=[]
		item =  AmazonItem()
		item['url'] = response.request.url
		#import pdb;pdb.set_trace()
		#item['href'] = sel.xpath('//div[@class="a-row a-spacing-none"]/a[@class="a-link-normal a-text-normal"]/@href').extract()
		title = str(list(map(unicode.strip,sel.xpath('//span[@id="productTitle"]/text()').extract())))
		title = title.replace("u'","").replace("[","").replace("]","")
		item['title'] = title
		brand = str(list(map(unicode.strip,sel.xpath('//a[@id="brand"]/text()').extract())))
		brand = brand.replace("u'","").replace("[","").replace("]","")
		item['brand'] = brand
		import pdb;pdb.set_trace()
		price = str(list(map(unicode.strip,sel.xpath('//span[@class="olp-padding-right"]//span[@class="a-color-price"]//text()').extract())))
		price = price.replace("Rs.","").replace("[","").replace("]","").replace("u'","").replace(",","").replace("'","").replace("$","")
		item['price'] = float(price)*67.30
		desc = str(list(map(unicode.strip,sel.xpath('//div/ul[@class="a-vertical a-spacing-none"]/li//text()').extract())))
		desc = desc.replace("[","").replace("]","").replace("u'","")
		item['desc'] = desc
		category = str(list(map(unicode.strip,sel.xpath('//div[@data-feature-name="wayfinding-breadcrumbs"]/ul/li//a//text()').extract())))
		category = category.replace("u'","").replace("[","").replace("]","").replace('"','').replace("'","")
		item['category'] = category
		if item['title'] and item['category'] and item['price']:
			return item