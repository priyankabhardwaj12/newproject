# import scrapy
# from selenium import webdriver
# from scrapy.spider import BaseSpider 
# from snapdeal.items import SnapdealItem
# import csv

# class VijaysalesSpider(BaseSpider):
#     name = "vij"
#     allowed_domains = ["www.snapdeal.com"]
#     start_urls = ['https://www.ofbusiness.in/category/manufacturing/steel']
#     def __init__(self):
#     	self.driver = webdriver.Firefox()
#     	self.count = 0       
#     	self.csvfile =  open('d.csv', 'a')
#     	self.spamwriter = csv.writer(self.csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     def parse(self, response):
#     	data = []
#         items=[]
#     	self.driver.get(response.url)
#     	for x1 in range(2000): self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     	for x1 in  self.driver.find_elements_by_xpath('//div[@class="listRow"]/a'):
#     		item = SnapdealItem()
#     		item["url"] = x1.get_attribute('href')
#     		item["title"] = x1.text
#     		self.spamwriter.writerow([item["url"], item["title"]])
#     		print "----", self.count, item["title"] 
#     		self.count += 1 
#     		data.append(item)
#     		# o1 = self.driver.find_element_by_xpath('//*[@id="see-more-products"]')
#     		# for x in range(0,40): o1.click()
#     	return data		