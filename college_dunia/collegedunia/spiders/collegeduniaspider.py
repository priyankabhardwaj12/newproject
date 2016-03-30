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
	start_urls = ['http://collegedunia.com/university/26007-indian-institute-of-technology-iit-kharagpur',
'http://collegedunia.com/university/25455-indian-institute-of-technology-iit-new-delhi',
'http://collegedunia.com/university/25881-indian-institute-of-technology-iit-chennai',
'http://collegedunia.com/university/25948-indian-institute-of-technology-iit-kanpur',
'http://collegedunia.com/university/25603-indian-institute-of-science-iisc-bangalore',
'http://collegedunia.com/university/25992-indian-institute-of-technology-iit-roorkee',
'http://collegedunia.com/university/25703-indian-institute-of-technology-iit-mumbai',
'http://collegedunia.com/university/25947-indian-institute-of-technology-bhu-iit-varanasi',
'http://collegedunia.com/university/25800-birla-institute-of-technology-and-science-bits-pilani',
'http://collegedunia.com/university/25396-indian-institute-of-technology-iit-guwahati',
'http://collegedunia.com/university/25889-national-institute-of-technology-nit-thiruchirapalli',
]

	def parse(self, response) :
		print ">>>>>", response.request.url 
		sel = Selector (response)
		items=[]
		item =  CollegeduniaItem ()
		item['url'] = sel.xpath('//a[@data-gtmaction="Website "]/@href').extract()
		#import pdb;pdb.set_trace()
		#url = sel.xpath('//div[@class="college_details"]/a/@href').extract()
		#item['href'] = sel.xpath('//div[@class="a-row a-spacing-none"]/a[@class="a-link-normal a-text-normal"]/@href').extract()
		college_name = str(list(map(unicode.strip,sel.xpath('//span[@itemprop="name"]/text()').extract())))
		college_name = college_name.replace("u'","").replace("[","").replace("]","")
		item['Institute_Name'] = college_name
		#import pdb;pdb.set_trace()
		Courses_Offered = str(list(map(unicode.strip,sel.xpath('//div[@class="college_quick_stats"]/table//tr/th/a[@data-gtmcategory="College V3"]/text()').extract())))
		Courses_Offered = Courses_Offered.replace("u'","").replace("[","").replace("]","").replace("'","")
		item['Courses_Offered'] = Courses_Offered
		Adress  = str(list(map(unicode.strip,sel.xpath('//span[@itemprop="address "]/text()').extract())))
		Adress = Adress.replace("u'","").replace("\n","").replace("[","").replace("]","").replace("'","")
		item['Adress'] = Adress
		Contact_No = str(list(map(unicode.strip,sel.xpath('//p[@itemprop="telephone "]/text()').extract())))
		Contact_No = Contact_No.replace("u'","").replace("[","").replace("]","").replace("'","")
		item['Contact_No'] = Contact_No
		Year =  str(list(map(unicode.strip,sel.xpath('//p[@title="Established "]/text()').extract())))
		Year = Year.replace("u'","").replace("[","").replace("]","").replace("'","").replace("Established -","")
		item['Year'] = Year
		Rating = str(list(map(unicode.strip,sel.xpath('//div[@class="college-stream-rating"]/ul/li//span[@class="textrating"]/text()').extract())))
		Rating = Rating.replace("u'","").replace("[","").replace("]","").replace("'","").split(',')[0]
		item['Rating'] = Rating

		# city = str(list(map(unicode.strip,sel.xpath('//div[@class="name-data-container"]/span/text()').extract()))).split(',')[0]
		# city = city.replace("u'","").replace("[","").replace("]","")
		# item['city'] = city

		# Fees = str(list(map(unicode.strip,sel.xpath('//td/svg[@class="svg-rupee"]/following-sibling::text()').extract())))
		# Fees = Fees.replace("u'","").replace("[","").replace("]","").replace("'","")
		# item['Avg_Fees_per_Year'] = Fees
		# #import pdb;pdb.set_trace()
		# desc = str(list(map(unicode.strip,sel.xpath('//div[@class="collegediscription div-with-content click-description"]//text()').extract())))
		# desc = desc.replace("u'","").replace("[","").replace("]","").replace("'","")
		# item['desc'] = desc
		
		return item
