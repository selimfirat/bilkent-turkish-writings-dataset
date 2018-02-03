from scrapy import Item, Field


class WritingEntry(Item):
    file_urls = Field()
    files = Field()