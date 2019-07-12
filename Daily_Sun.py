import scrapy
from scrapy.selector import HtmlXPathSelector
import os


class Daily(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.dailysun.co.za/']

    def parse(self, response):
        urls = response.xpath(
            '//div[contains(@class, "content")]//@href').extract()

        for article in urls:
            f = open("Log.txt", "a+")
            f.write(f"{article} \n")
            f.close()
            yield scrapy.Request(url=article, callback=self.next)

    def next(self, response):

        title = response.selector.xpath(
            "//meta[@property='twitter:title']/@content").extract()

        publishDate = response.selector.xpath(
            "//meta[@property='article:published_time']/@content").extract()

        body = response.selector.xpath(
            "//div[@class='content']/p/text()").extract()

        source = response.url
        data = {'title': title[0], 'body': [
            x for x in body], 'publish date': publishDate[0], 'source': source}
        f = open("Daily Sun.txt", "a+")
        f.write(f"{data} \n")
        f.close()
