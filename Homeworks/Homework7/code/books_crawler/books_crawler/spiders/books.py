
import scrapy
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from books_crawler.items import BooksCrawlerItem

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com',]
    
    rules = [Rule(LinkExtractor(canonicalize=True, unique=True), callback='parse_page')]

    for i in range(2, 50):
        start_urls.append("http://books.toscrape.com/catalogue/page-"+str(i)+".html")
        
    def parse_page(self, response):
        items = []
        links = LinkExtractor(canonicalize=True, unique=True).extract_links(response)
        for link in links:
            for dm in self.allowed_domains:
                if dm in link.url:
                    item = BooksCrawlerItem()
                    item['Inurl'] = response.url
                    item['Outurl'] = link.url
                    items.append(item)
                    yield item
        #items