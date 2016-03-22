import scrapy
from scrapy.item import Item,Field


class CollegeduniaItem(Item):
	url = Field()
	title = Field()
	college_name = Field()
	city = Field()
	Courses = Field()
	Avg_Fees_per_Year = Field()
	Rating = Field()
	Seats = Field()
	pass
