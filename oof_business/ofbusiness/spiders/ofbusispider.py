import scrapy
from selenium import webdriver
from scrapy.spider import BaseSpider 
from ofbusiness.items import OfbusinessItem
import urllib2
from time import strftime
from datetime import timedelta
from datetime import datetime
import datetime
from time import sleep
import time
from bs4 import BeautifulSoup
import csv

class ofSpider(BaseSpider):
    name = "of"
    allowed_domains = ["ofbusiness.in/"]
    start_urls = ['https://www.ofbusiness.in/category/manufacturing/steel',
    'https://www.ofbusiness.in/category/manufacturing/welding',
    'https://www.ofbusiness.in/category/manufacturing/industrial-paints',
    'https://www.ofbusiness.in/category/manufacturing/abrasives',
    'https://www.ofbusiness.in/category/manufacturing/fasteners',
    'https://www.ofbusiness.in/category/manufacturing/lubrication',
    'https://www.ofbusiness.in/category/manufacturing/power-transmission',
    'https://www.ofbusiness.in/category/manufacturing/power-tools',
    'https://www.ofbusiness.in/category/manufacturing/hand-tools',
    'https://www.ofbusiness.in/category/manufacturing/measure-test',
    'https://www.ofbusiness.in/category/manufacturing/safety-fire-protection',
    'https://www.ofbusiness.in/category/manufacturing/cutting-machining-tools',]
    def __init__(self):
    	self.driver = webdriver.Firefox()
    	self.count = 0       
    	self.csvfile =  open('d.csv', 'a')
    	self.spamwriter = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    def parse(self, response):
    	data = []

    	self.driver.get(response.url)
    	for x1 in range(2000): self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for x1 in  self.driver.find_elements_by_xpath('//a[@class="itemImgWrap"]'):
            item = OfbusinessItem()
            item["url"] = x1.get_attribute('href')
            item["title"] = x1.text
            item["source"] = response.url
            self.spamwriter.writerow([item["url"], item["title"], item["source"]])
            print "----", self.count, item["title"] 
            self.count += 1 
            data.append(item)
        return data
       