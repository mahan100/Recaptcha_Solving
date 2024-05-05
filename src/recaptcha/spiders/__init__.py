# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from unicodedata import name
import scrapy


class recap(scrapy.Spider):
    name='recap'

    def start_requests(self):
        urls = [
            'https://www.google.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    def parse(self, response):
        print('*'*100)
        print(response.css('div.gb_Jd'))
