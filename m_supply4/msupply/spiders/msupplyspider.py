from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from msupply.items import MsupplyItem
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
sys.path.append('/home/supplified/Desktop/parsing')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parsing.settings")
from product.models import BaseProducts
print ">>>>> base product", BaseProducts.objects.all()
class msupplySpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "m"
	allowed_domains = ["www.msupply.com/"]
	start_urls =['http://www.msupply.com/building-material/cement/acc-concrete-plus-ppc.html']
	def __init__(self):
		self.count = 0
		CrawlSpider.__init__(self)
		self.verificationErrors = []
	def parse(self,response):
		self.count = self.count + 1
		sel = Selector (response)
		item = MsupplyItem()
		#import pdb;pdb.set_trace()
		item['url'] = response.request.url
		item['title'] = sel.xpath('//h1/text()').extract()
		sku = str(list(map(unicode.strip,sel.xpath('//*[@id="product_addtocart_form"]/div[2]/div[1]/div/div/div[2]/div/span/text()').extract())))
		sku = sku.replace("u'Product ID :","").replace("[","").replace("]","").replace("'","")
		item['Sku'] =sku
		brand = str(list(map(unicode.strip,sel.xpath('//div[@class="tab-pane"][@id="tab_b"]//text()').extract())))
		brand = str(brand).replace("u'","").replace("'","").replace('" ",','').replace("' ',","").replace(", ,","")
		brand = str(brand).split(' ')[5]
		item['brand'] = brand
		category = str(list(map(unicode.strip,sel.xpath('//div[@class="current-product"]//text()').extract())))
		category = category.replace("[u'","").replace("]","")
		item['category'] = category
		#brand = sel.xpath('//div[@class="tab-pane"]/hr/div/table/tr//td//text()').extract()
		Variant = str(list(map(unicode.strip,sel.xpath('//div[@class="tab-pane"][@id="tab_b"]//text()').extract())))
		Variant = str(Variant).replace("u'","").replace("'","").replace('" ",','').replace("' ',","").replace(", ,","")
		Variant = str(Variant).split(' ')[8]
		item['Variant'] = Variant
		desc = str(list(map(unicode.strip,sel.xpath('//div[@class="tab-pane"][@id="tab_b"]//text()').extract())))
		desc = desc.replace("[","").replace("]","").replace("u\'\',","").replace("u\'","").replace("\'","")
		item['desc'] = desc
		price = str(list(map(unicode.strip,sel.xpath('//span[@class="price"][@id="old-price-4788"]/text()').extract())))
		price = price.replace("\u20b9","").replace("[","").replace("]","").replace("u'","").replace("'","")
		item['price'] = price
		#import pdb;pdb.set_trace()
		item1 = BaseProducts()
		item1.brand_name = item['brand']
		item1.title = item['title'][0]
		item1.Sku = item['Sku']
		item1.category_name=item['category']
		item1.description=item['desc']
		#item1.color_name = item['color']
		# item1.price = item['price']
		item1.source_id = 1
		item1.save()
		print item
		return item	