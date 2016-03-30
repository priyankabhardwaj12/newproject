from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from buildbazar.items import BuildbazarItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
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
# sys.path.append('/home/supplified/Desktop/parsing')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parsing.settings")
# from suplifi.models import BaseProducts
# from suplifi.models import SPM
# from suplifi.models import SubscribeProduct

class villorySpiders (CrawlSpider):
	handle_httpstatus_list = [302]
	name = "bi"
	allowed_domains = ["http://www.buildzar.com/"]
	start_urls = ['http://www.buildzar.com/gurgaon/cement-concrete-aggregates/cement',
'http://www.buildzar.com/gurgaon/cement-concrete-aggregates/cement?category=61&page=2',
'http://www.buildzar.com/gurgaon/cement-concrete-aggregates/ready-mix-concrete',
'http://www.buildzar.com/gurgaon/cement-concrete-aggregates/ready-mix-concrete?category=65&page=2',
'http://www.buildzar.com/gurgaon/cement-concrete-aggregates/fine-aggregates',
'http://www.buildzar.com/gurgaon/cement-concrete-aggregates/coarse-aggregates',
'http://www.buildzar.com/gurgaon/cement-concrete-aggregates/construction-chemicals-9',
'http://www.buildzar.com/gurgaon/steel-tmt/steel-tmt',
'http://www.buildzar.com/gurgaon/bricks-blocks/clay-bricks',
'http://www.buildzar.com/gurgaon/bricks-blocks/aac-blocks',
'http://www.buildzar.com/gurgaon/plumbing/pipes',
'http://www.buildzar.com/gurgaon/plumbing/pipes?category=55&page=2',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=2',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=3',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=4',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=5',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=6',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=7',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=8',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=9',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=10',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=11',
'http://www.buildzar.com/gurgaon/plumbing/pipes-fittings?category=54&page=12',
'http://www.buildzar.com/gurgaon/plumbing/water-tanks',
'http://www.buildzar.com/gurgaon/plumbing/water-tanks?category=57&page=2',
'http://www.buildzar.com/gurgaon/plumbing/solvents',
'http://www.buildzar.com/gurgaon/electricals/wires-and-cables?category=91',
'http://www.buildzar.com/gurgaon/electricals/wires-and-cables?category=92',
'http://www.buildzar.com/gurgaon/electricals/wires-and-cables?category=93',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=84',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=84&page=2',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=85',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=86',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=87',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=87&page=2',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=87&page=3',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=87&page=4',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=87&page=5',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=87&page=6',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=87&page=7',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=88',
'http://www.buildzar.com/gurgaon/electricals/mcbs-dbs?category=88&page=2',
]
	
	def __init__(self):
		self.count = 0
		CrawlSpider.__init__(self)
		self.verificationErrors = []
	def parse(self,response):
		self.count = self.count + 1
		sel = Selector (response)
		item = BuildbazarItem()
		#item['source_url'] = "http://www.buildzar.com/delhi"
		#import pdb;pdb.set_trace()
		item['url'] = sel.xpath('//li[@class="item"]/a/@href').extract()
		return item
		
		