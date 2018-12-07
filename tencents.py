# -*- coding: utf-8 -*-
import scrapy
from Tencents.items import TencentsItem

class TencentsSpider(scrapy.Spider):
    name = 'tencents'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=0']

    def parse(self, response):
        offer_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for offer in offer_list:
            item = TencentsItem()
            item['Name'] = offer.xpath('./td[1]/a/text()')[0].extract()
            #某些职位类别可能为空，这里加个判定
            if len(offer.xpath('./td[2]/text()')):
                item['Type'] = offer.xpath('./td[2]/text()')[0].extract()
            else:
                item['Type'] = ''

            item['Number'] = offer.xpath('./td[3]/text()')[0].extract()

            item['Location'] = offer.xpath('./td[4]/text()')[0].extract()

            item['publishTime'] = offer.xpath('./td[5]/text()')[0].extract()

            item['Link'] = offer.xpath('./td[1]/a/@href')[0].extract()

            yield item
        #提取下一页链接，发送请求，回调parse函数，直至提取不到链接
        if len(response.xpath('//a[@class="noactive" and @id="next"] ')) == 0:
            url = response.xpath('////a[@id="next"]/@href')[0].extract()
            yield scrapy.Request('https://hr.tencent.com/' + url ,callback=self.parse)