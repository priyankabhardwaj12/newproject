import scrapy
from selenium import webdriver
from scrapy.spider import BaseSpider 
import csv
from sonata.items import SonataItem
import re
class sonataSpiders (BaseSpider) :
	handle_httpstatus_list = [302]
	name = "s"
	allowed_domains = ["titan.co.in/shop-online/watches/sonata"]
	start_urls = ['http://titan.co.in/shop-online/watches/sonata']
	def __init__(self):
		self.driver = webdriver.Firefox()
		self.count = 0
		self.csvfile =  open('document.csv', 'a')
		self.spamwriter = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	def parse(self, response) :
		data = []
		self.driver.get(response.url)
		o1 = self.driver.find_element_by_xpath('//div[@class="show_more_bar"]')
		for x in range(0,40): o1.click()
		#import pdb;pdb.set_trace()
		for x1 in  self.driver.find_elements_by_xpath('//div[@class="product_image"]//a'):
			item = SonataItem()
			item["url"] = x1.get_attribute('href')
			item["title"] = x1.text
			item["source"] = response.url
			self.spamwriter.writerow([item["url"], item["title"], item["source"]])
			print "----", self.count, item["title"]
			self.count += 1
			data.append(item)
		return data
		