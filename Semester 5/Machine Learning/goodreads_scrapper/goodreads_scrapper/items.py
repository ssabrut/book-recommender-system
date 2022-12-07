# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodreadsItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    total_rating = scrapy.Field()
    genre = scrapy.Field()