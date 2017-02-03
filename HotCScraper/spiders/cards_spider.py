import scrapy


class CardsSpider(scrapy.Spider):
    name = "cards"
    start_urls = ['http://www.heartofthecards.com/code/cardlist.html?pagetype=ws']

    def parse(self, response):
        for set in response.xpath('//a[contains(@href, "/code/cardlist.html?pagetype=ws&")]'):
            set = "http://www.heartofthecards.com" + set.xpath('@href').extract_first()
            yield scrapy.Request(set, callback=self.parse_card_list)

    def parse_card_list(self, response):
        for card in response.xpath('//td[1]/a[contains(@href, "/code/cardlist.html?card=")]'):
            card = "http://www.heartofthecards.com" + card.xpath('@href').extract_first()
            yield scrapy.Request(card, callback=self.parse_card_list)
