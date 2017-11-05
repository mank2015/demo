#!/usr/bin/env python3

import scrapy
import re

class ShiyanlouGithubSpider(scrapy.Spider):
    
    name='shiyanlougithub'

    def start_requests(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url_tmpl.format(i) for i in range(1,4))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        for course in response.css('li.public'):
            yield {
                    'name': course.xpath('.//h3/a/text()').re_first("\n\s*(.*)"),
                    'update': course.xpath('.//relative-time/@datetime').extract_first()
            }
