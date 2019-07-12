import scrapy
import os


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
        title = response.selector.xpath(
            "//div/div[@class='kInstance']/h1/text()").extract()

        publishDate = response.selector.xpath(
            "//div/div[@class='instance-byline']/span[@class='social-share-header']/text()").extract()

        body = response.selector.xpath(
            "//div/div[@class='kInstance-Summary']/text()").extract()

        source = response.url

        data = {'title': title[0], 'body': [
            x for x in body], 'publish date': publishDate[0], 'source': source}
        f = open("Bizzcommunity.txt", "a+")
        f.write(f"{data} \n")
        f.close()
