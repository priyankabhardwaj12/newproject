# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.common import action_chains, keys
# from selenium.webdriver.support import expected_conditions as EC 
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# import unittest, time, re
# import HTMLTestRunner

# class BasicActions(unittest.TestCase):

# 	def setUp(self):
# 		global driver
# 		driver = webdriver.Firefox()
# 		driver.implicitly_wait(30)
# 		base_url = "http://priyanka:Pr14a9ka123@dev.supplified.com/online-buy/Plants-&-More-Indoor-Hanging-Basket-Plants/993"
# 		driver.maximize_window()
# 		verificationErrors = []

# 	def test1(self):
# 		# driver = self.driver
# 		handle_httpstatus_list = [302]
# 		driver.get(base_url)
# 		links = driver.find_element_by_xpath('/html/body/div[7]/section/div[2]/div[2]/div/div[5]/div[1]/a[2]').click()
# 	def test2_price_change(self):
# 		x =0
# 		while x <4:
# 			for li in driver.find_elements_by_class_name("qtyplus"):
# 				li.click()
# 				for x1 in driver.find_elements_by_xpath('//label[@id="store_offer_price"]'):
# 					price = x1.text
# 					print"<<>>",price
# 			x += 1
# 	def test3_clickbuttons(self):
# 		AdtocartButtonxpath = ('//*[@id="addcartbtn2"]')
# 		SELECTLOCATIONxpath = ('/html/body/div[4]/div/div[2]/div/div[1]')
# 		GoTocartxpath       = ('/html/body/div[7]/div[6]/div/button[2]')
# 		ProceedToGuestxpath = ('//*[@id="frmsignup"]/div[1]/p[1]/label[3]')

# 		AdtocartButtonField = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(AdtocartButtonxpath))
# 		SELECTLOCATIONField = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(SELECTLOCATIONxpath))
# 		GoTocartField       = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(GoTocartxpath))
# 		ProceedToGuestField = WebDriverWait(driver,5).until(lambda driver: driver.find_element_by_xpath(ProceedToGuestxpath))

# 		AdtocartButtonField.click()
# 		SELECTLOCATIONField.click()
# 		GoTocartField.click()
# 		ProceedToGuestField.click()

# 	def test4_login(self):
# 		inputElementMobID   = ("txtphone")
# 		inputElementNameID  = ("txtname")
# 		inputElementEmailID = ("txtemail")
# 		buttonsID           = ("btnsignup")
# 		okbuttonxpath       = ('//*[@id="successpopup"]/div/button')

# 		MobFieldElement    = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(inputElementMobID))
# 		NameFieldElement   = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(inputElementNameID))
# 		EmailFieldElement  = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(inputElementEmailID))
# 		ButtonFieldElement = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(buttonsID))
# 		OkButtonField      = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(okbuttonxpath))

# 		MobFieldElement.clear()
# 		MobFieldElement.send_keys('9899656544')
# 		NameFieldElement.clear()
# 		NameFieldElement.send_keys('priya')
# 		EmailFieldElement.clear()
# 		EmailFieldElement.send_keys('priyanka.bhardwaj@supplified.com')
# 		ButtonFieldElement.click()
# 		OkButtonField.click()

# 	def test5_inputs(self):
# 		inputElementPinID      = ("vPincode")
# 		inputElementAddID      = ("tAddress")
# 		inputElementStatexpath = ('//*[@id="vState"]')
# 		continuebuttonxpath    = ('//*[@id="ship_form"]/button[1]')
# 		place_orderxpath       = ('//*[@id="pay_form"]/button')

# 		PinFieldElement       = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(inputElementPinID))
# 		AddressFieldElement   = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(inputElementAddID))
# 		StateFieldElement     = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_xpath(inputElementStatexpath))
# 		continuebuttonField   = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(continuebuttonxpath))
# 		PlaceOrderField       = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id(place_orderxpath))

# 		PinFieldElement.clear()
# 		PinFieldElement.send_keys("110019")
# 		AddressFieldElement.clear()
# 		AddressFieldElement.send_keys("supplified.com,ploat no 246,ph-3 okla")
# 		StateFieldElement.clear()
# 		StateFieldElement.send_keys('DELHI')
# 		continuebuttonField.click()
# 		PlaceOrderField.click()

# 	def test6_screenshort(self):
# 		driver.save_screenshot('screenshot1.png')
		
# 	def tearDown(self):
# 		driver.quit()


# if __name__ == "__main__":
# 	HTMLTestRunner.main()