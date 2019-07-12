import scrapy

class Bizz(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.bizcommunity.com/']

    def parse(self, response):
        urls = response.xpath("//div/a/@href").extract()
        for article in urls:
            if '/Article' in article:
                url = "https://www.bizcommunity.com"+article
                print(url)
                yield scrapy.Request(url, callback=self.next)

    def next(self, response):
        yield(response.url)