import scrapy
from scrapy import Request
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor

from writing_entry import WritingEntry


class BilkentTurkishWritingsSpider(scrapy.Spider):

    name = "bilkent_turkish_writings"
    custom_settings = {
        "ITEM_PIPELINES": {
            'scrapy.pipelines.files.FilesPipeline': 100
        },
        "DOWNLOAD_DELAY": 0.25,
        "FILES_STORE": '../data/'
    }

    start_urls = ["https://stars.bilkent.edu.tr/turkce/"]
    allowed_domains = ['stars.bilkent.edu.tr']

    def __init__(self, *args, **kwargs):
        super(BilkentTurkishWritingsSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        print('Parsing '+response.url)

        file_urls = []

        for link in LxmlLinkExtractor(allow=self.allowed_domains).extract_links(response):
            if "ogrenciNo" in link.url:
                file_urls.append(link.url)
            else:
                yield Request(link.url, self.parse)

        yield WritingEntry(file_urls=file_urls)

    def save_pdf(self, response):
        """ Save pdf files """
        path = response.url.split('/')[-1]
        self.logger.info('Saving PDF %s', path);
        with open(path, 'wb') as file:
            file.write(response.body);
