from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest, time, re
import HTMLTestRunner
class Sele1(unittest.TestCase):
class Settings:
	driver = webdriver.Firefox()	
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "http://priyanka:Pr14a9ka123@dev.supplified.com/buy-online/metro-load-carrying-helmet-sh-1206-(yellow)/sh-1206-yellow-chin-strap-load-carrying-helmet-hdpe---high-density-polyethylene/6746"
		#self.base_url = "http://priyanka:Pr14a9ka123@dev.supplified.com/online-buy/safety-&-security/147",
		self.verificationErrors = []
	def test_sele1(self):
		driver = self.driver
		driver.maximize_window()
		handle_httpstatus_list = [302]
		driver.get(self.base_url)
		#product = driver.find_element_by_xpath('/html/body/div[5]/section/div[2]/div[2]/div[3]/div[5]/div[15]/a[2]').click()
		location = driver.find_element_by_xpath('//*[@id="currentLocs"]/a/span').click()
		# time.sleep(2)
		lo = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]')
		lo.click()
		try:
			adtocart = driver.find_element_by_xpath('//*[@id="addcartbtn1"]').click()
		except: pass
		try:
			check_product = driver.find_element_by_xpath('/html/body/div[5]/section/div[2]/div[2]/div[2]/div/ul/span').text
			print ">>>",check_product
		except: pass
		title = driver.find_element_by_xpath('//h1[@class="ptSansBold"]').text
		print "product name---",title
		price = driver.find_element_by_xpath('//span[@itemprop="price"]')
		print"product price---",price.text
		desc = driver.find_element_by_xpath('//*[@id="specification"]/table').text
		print"specification desc-----",desc
		for keyfeatures in driver.find_element_by_xpath('//div[@id="keyFeature"]/ul'):
			print "keyfeatures---",keyfeatures.text
		for descriptions in driver.find_element_by_xpath('//div[@id="productDescription"]'):
			print"descriptions-----", descriptions.text
		for category in  driver.find_elements_by_xpath('//div[@class="col-md-10 pull-left prodbreadcrumb"]/div//a'):
			print"category---",category.text
		#driver.refresh()
		# 	lo.click()
		# 	# check_product = driver.find_element_by_xpath('//ul[@class="pull-left col-md-10"]//span[@style="font-family:PTSans-Bold;font-size:20px;color:red;"]')
		# 	# if check_product:
		# 	# 	check_product.text

if __name__ == "__main__":
	HTMLTestRunner.main()			
		
	