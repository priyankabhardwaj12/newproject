import scrapy
from selenium import webdriver
from scrapy.spider import BaseSpider 
from buildbazar.items import BuildbazarItem
from time import sleep
import time
import csv

class VijaysalesSpider(BaseSpider):
    name = "vij"
    allowed_domains = ["snapdeal.com"]
    #start_urls = ['http://www.snapdeal.com/products/kitchen-bathroom-fittings-electrical-equipment/?q=Type_s%3AWires%7C&sort=plrty']
    start_urls = ['https://www.supplified.com/']
    def __init__(self):
    	self.driver = webdriver.Firefox()
    	self.count = 0       
    	# self.csvfile =  open('r1.csv', 'a')
    	# self.spamwriter = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    def parse(self, response):
    	data = []
    	self.driver.get(response.url)
        x1 = self.driver.find_element_by_xpath('//*[@id="menu"]/li/ul/li[2]/a')
        
        # for x1 in range(12000): self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(15)
        # for x2 in  self.driver.find_elements_by_xpath('//div[@class="product-tuple-image"]//a'):
        #     time.sleep(2)
        #     item = BuildbazarItem()
        #     item["url"] = x2.get_attribute('href')
        #     item["title"] = x2.text
        #     item["source_url"] = response.url
        #     self.spamwriter.writerow([item["url"], item["title"], item["source_url"]])
        #     print "----", self.count, item["title"]
        #     self.count += 1
        #     data.append(item)
        #     o1 = self.driver.find_element_by_xpath('//*[@id="see-more-products"]').click()
        #     #for x in range(0,100): o1
        return data
               