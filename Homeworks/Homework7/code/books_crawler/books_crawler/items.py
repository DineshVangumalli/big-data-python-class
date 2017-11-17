# %load code/tutorial/tutorial/items.py

# Define here the models for your scraped items

import scrapy

## Adding container to hold scraped data using scrapy.Item as the parent class
class BooksCrawlerItem(scrapy.Item):
    Inurl = scrapy.Field()
    Outurl = scrapy.Field()
    #url = scrapy.Field()
    pass