# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class TencentsItem(scrapy.Item):

    Name = Field()
    Type = Field()
    Number = Field()
    Location = Field()
    publishTime = Field()
    Link = Field()
