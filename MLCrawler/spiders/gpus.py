# -*- coding: utf-8 -*-
import scrapy


class GpusSpider(scrapy.Spider):
    name = 'gpus'
    allowed_domains = ['mercadolivre.com.br']
    start_urls = ['https://informatica.mercadolivre.com.br/componentes-pc/placas-video/']

    def parse(self, response):
        itens = response.xpath('//ol[@id="searchResults"]/li')
        for i in itens:
            links = i.xpath('././a/@href').extract_first()
            yield scrapy.Request(url = links, callback = self.cb)
        prox = response.xpath('//li[@class, "andes-pagination__arrow-title"]//a/@href').extract_first()
        if prox:
            self.log(f"Próxima Página: {prox}")
            yield scrapy.Request(url = prox, callback = self.parse)
    def cb(self, response):
        titulo = response.xpath('//h1[@class, "item-title__primary"]/text()').extract_first()
        condicao = response.xpath('//div[@class, "item-conditions"]/text()').extract_first()
        custo = response.xpath('//span[@class, "price-tag"]/span[1]/text()').extract_first() + response.xpath('//span[@class, "price-tag"]/span[2]/text()').extract_first() + response.xpath('//span[@class, "price-tag"]/span[3]/text()').extract_first()
        yield {'titulo': titulo, 'condicao': condicao, 'custo': custo}
