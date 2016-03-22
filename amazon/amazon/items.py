import scrapy
from scrapy.item import Item,Field


class AmazonItem(Item):
	href = Field()
	title = Field()
	desc = Field()
	price = Field()
	url = Field()
	brand = Field()
	category = Field()
	img_list = Field()
	pass
