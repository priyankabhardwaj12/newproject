# from selenium import selenium
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from time import sleep
# import unittest, time, re
# import unittest, time, re

# class NewTest(unittest.TestCase):
#     def setUp(self):
#         self.verificationErrors = []
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "http://dev.supplified.com/online-buy/Plants-&-More-Indoor-Hanging-Basket-Plants/993"

#     def test_new(self):
#         driver = self.driver
#         wait = WebDriverWait(driver, 10)
#         driver.get(self.base_url)
#         links = driver.find_element_by_xpath('/html/body/div[7]/section/div[2]/div[2]/div/div[5]/div[1]/a[2]').click()
#         x =0
#         while x <4:
#             for li in driver.find_elements_by_class_name("qtyplus"):
#                 li.click()
#                 for x1 in self.driver.find_elements_by_xpath('//label[@id="store_offer_price"]'):
#                     price = x1.text
#                     print"<<>>",price
#             x += 1
#         adtocart = driver.find_element_by_xpath('//*[@id="addcartbtn2"]').click()
#         l = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[1]').click()
#         gotocart = driver.find_element_by_xpath('/html/body/div[7]/div[5]/div/button[2]').click()
#         time.sleep(2)
#         con = driver.find_element_by_xpath('//*[@id="step1"]/div/div[1]/div[2]/div[3]/a[1]/button').click()
#         procetoguest = driver.find_element_by_xpath('//*[@id="frmsignup"]/div[1]/p[1]/label[3]').click()
#         inputElementMob = driver.find_element_by_id("txtphone")
#         val1 = inputElementMob.send_keys('9990373674')
#         inputElementName = driver.find_element_by_id("txtname")
#         val2 = inputElementName.send_keys('pri')
#         inputElementEmail = driver.find_element_by_id("txtemail")
#         val3 = inputElementEmail.send_keys('priyank1.bhardwaj@supplified.com')
#         ###Do some JQuery stuff here##
#         wait.until(driver.execute_script('jQuery.active == 0'))
#         continuebtn = driver.find_element_by_xpath('//*[@id="btnsignup"]').click()

#     # def tearDown(self):
#     #     self.selenium.stop()
# if __name__ == "__main__":
#     unittest.main()     
