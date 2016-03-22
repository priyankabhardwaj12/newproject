from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
import urllib2
from BeautifulSoup import BeautifulSoup
from materialtree.items import MaterialtreeItem
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
import csv
import json
sys.path.append('/home/supplified/mysite')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
from products.models import Category
from products.models import BaseProducts
from products.models import SPM
from products.models import Subscribe_Product

class materialSpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "mst"
	allowed_domains = ['materialtree.com']
	start_urls =['http://www.materialtree.com/floor-wall-roof/vitrified-tiles/double-charge-vitrified-tiles',
	'http://www.materialtree.com/floor-wall-roof/vitrified-tiles/double-charge-vitrified-tiles?p=2',
	'http://www.materialtree.com/floor-wall-roof/vitrified-tiles/double-charge-vitrified-tiles?p=3',
	'http://www.materialtree.com/floor-wall-roof/vitrified-tiles/double-charge-vitrified-tiles?p=4',
	'http://www.materialtree.com/floor-wall-roof/vitrified-tiles/double-charge-vitrified-tiles?p=5',
	'http://www.materialtree.com/floor-wall-roof/vitrified-tiles/full-body-vitrified-tiles']

	def parse(self, response) :
		sel = Selector (response)
		data = []
		items=[]
		item = MaterialtreeItem ()
		#self.driver.get(response.url)
		#time.sleep(2.5)
		item['url'] = sel.xpath('//h2[@class="product-name"]/a/@href').extract()
		return item