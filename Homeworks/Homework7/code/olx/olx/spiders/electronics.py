
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ElectronicsSpider(CrawlSpider):
    name = "electronics"
    allowed_domains = ["www.olx.com.in"]
    start_urls = ['https://www.olx.in/computers-laptops/']
    
    rules = (Rule(LinkExtractor(), callback='parse_item', follow=True),)
          
    def parse_item(self, response):
        yield {'url': response.url }
            