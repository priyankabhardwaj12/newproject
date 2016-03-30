# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item,Field
import scrapy

class BuildbazarItem(Item):
	source = Field()
	level = Field()
	um = Field()
	title = Field()
	Product_id = Field()
	desc1 = Field()
	img = Field()
	region_name = Field()
	Delivery_time = Field()
	price = Field()
	price1 = Field()
	Sku = Field()
	url = Field()
	brand = Field()
	source_url = Field()
	desc = Field()
	Variant = Field()
	Saller = Field()
	category = Field()
	img_list = Field()
	pass
