import os
import scrapy
from scrapy.crawler import CrawlerProcess
from Daily_Sun import Daily
from Bizzcommunity import Bizz


def process():
    process = CrawlerProcess()
    process.crawl(Bizz)
    process.crawl(Daily)
    process.start()


if __name__ == "__main__":
    process()
