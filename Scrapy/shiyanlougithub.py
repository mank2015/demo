#!/usr/bin/env python3

import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):
    
    neme='shiyanluogithub'

    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?page{}tab=repositories'
        urls = (url_tmpl.format(i) for i in range(1,4))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for course in response.css('li.col-12'):
            yield {
                'name':course.css('div.d-inline-block.h3 a::text').extract_first()        
            }
        pass
