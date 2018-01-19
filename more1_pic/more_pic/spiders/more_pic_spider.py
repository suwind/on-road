from scrapy.spiders import Rule,CrawlSpider,Spider
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

from more_pic.items import MorePicItem

class MorePicSpider(CrawlSpider):
# class MorePicSpider(Spider):
    name='more1_pic'
    download_delay=1
    start_urls=[
        'https://movie.douban.com/celebrity/1016930/photo/1253599819/'
    ]
    # rules=(
    #     Rule(LinkExtractor(allow=(r'https://movie.douban.com/celebrity/1016930/photo/\d+')),callback='parse_item'),
    # )
    rules = (
        Rule(LinkExtractor(allow=(r'https://movie\.douban\.com/celebrity/1016930/photo/\d+')), callback='parse_item',follow=False),
    )
    def parse_item(self,response):
        sel=Selector(response)
        item=MorePicItem()
        # item['page_url']=sel.xpath((''))
        item['image_url']=sel.xpath('//div[@class="photo-show"]/div[@class="photo-wp"]/a/img/@src').extract()
        yield item
        # sites=sel.xpath('//div[@class="photo-show"]')
        # for site in sites:
        #     item['image_url'] = site.xpath('div[@class="photo-wp"]/a/img/@src').extract()
        #     yield item
