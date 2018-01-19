from scrapy.spiders import Spider,Rule,CrawlSpider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from douban_spider.items import DoubanSpiderItem

class DoubanTopmovieSpider(CrawlSpider):
    name='douban_tmovie'
    download_delay=1
    start_urls= [
        'https://movie.douban.com/top250?start=0&filter=&type='
    ]

    rules = (
        Rule(LinkExtractor(allow=(r'https://movie\.douban\.com/top250\?start=\d+&filter=')), callback='parse_item',),
    )

    def parse_item(self,response):
        sel=Selector(response)
        item=DoubanSpiderItem()
        sites=sel.xpath('//div[@class="info"]')
        for site in sites:
            item['movie_name'] = site.xpath('div[@class="hd"]/a/span[1]/text()').extract()
            item['movie_star'] = site.xpath('div[@class="bd"]/div/span[2]/text()').extract()
            item['movie_quote'] = site.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            yield item

    # 不适用rules的方法
    # def parse(self,response):
    #     sel=Selector(response)
    #     item=DoubanSpiderItem()
    #     sites=sel.xpath('//div[@class="info"]')
    #     for site in sites:
    #         item['movie_name'] = site.xpath('div[@class="hd"]/a/span[1]/text()').extract()
    #         item['movie_star'] = site.xpath('div[@class="bd"]/div/span[2]/text()').extract()
    #         item['movie_quote'] = site.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
    #         yield item
    #
    #     urls=sel.xpath('//span[@class="next"]/a/@href').extract()
    #     for url in urls:
    #         url='https://movie.douban.com/top250'+url
    #         yield Request(url,callback=self.parse)




