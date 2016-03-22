from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from collegedunia.items import CollegeduniaItem
from selenium import selenium
from selenium import webdriver
from scrapy.http import FormRequest
from scrapy import log
from time import strftime
#from datetime import timedelta
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

class collSpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "co"
	allowed_domains = ['collegedunia.com/']
	start_urls = ["http://collegedunia.com/college/5680-sir-jj-college-of-architecture-sjjca-mumbai"]

	def parse(self, response) :
		print ">>>>>", response.request.url 
		sel = Selector (response)
		items=[]
		item =  CollegeduniaItem ()
		item['url'] = response.request.url
		#import pdb;pdb.set_trace()
		#item['href'] = sel.xpath('//div[@class="a-row a-spacing-none"]/a[@class="a-link-normal a-text-normal"]/@href').extract()
		college_name = str(list(map(unicode.strip,sel.xpath('//span[@itemprop="name"]/text()').extract())))
		college_name = college_name.replace("u'","").replace("[","").replace("]","")
		item['college_name'] = college_name
		import pdb;pdb.set_trace()
		city = str(list(map(unicode.strip,sel.xpath('//div[@class="name-data-container"]/span/text()').extract()))).split(',')[0]
		city = city.replace("u'","").replace("[","").replace("]","")
		item['city'] = city
		Courses = str(list(map(unicode.strip,sel.xpath('//div[@class="college_quick_stats"]/table//tr/th/a[@data-gtmcategory="College V3"]/text()').extract())))
		Courses = Courses.replace("u'","").replace("[","").replace("]","").replace("'","")
		Fees = str(list(map(unicode.strip,sel.xpath('//td/svg[@class="svg-rupee"]/following-sibling::text()').extract())))
		Fees = Fees.replace("u'","").replace("[","").replace("]","").replace("'","")
		return item
