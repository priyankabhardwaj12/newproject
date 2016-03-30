import scrapy
from scrapy.item import Item,Field


class CollegeduniaItem(Item):
	url = Field()
	Institute_Name = Field()
	Courses_Offered = Field()
	Adress= Field()
	Contact_No = Field()
	Year = Field()
	Interance_eaxam = Field()
	Rating = Field()
	Approval = Field()
	pass
