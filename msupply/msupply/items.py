from scrapy.item import Item,Field
import scrapy


class MsupplyItem(Item):
	source = Field()
	title = Field()
	Sku = Field()
	price = Field()
	url = Field()
	saller = Field()
	Variant = Field()
	variant = Field()
	subvariant = Field()
	source_url = Field()
	desc = Field()
	category = Field()
	brand = Field()
	
	pass
