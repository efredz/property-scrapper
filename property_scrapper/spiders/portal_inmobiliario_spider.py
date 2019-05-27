import scrapy


class PortalInmobiliario(scrapy.Spider):
    name = "portal-inmobiliario"
    start_urls = [
        'https://www.portalinmobiliario.com/venta/departamento/santiago-metropolitana?tp=2&op=1&ca=3&ts=1&dd=0&dh=6'
        '&bd=0&bh=6&or=f-des&mn=1&sf=1&sp=0',
    ]

    def parse(self, response):
        full_results = response.xpath('//div[@class="col-sm-9 product-item-data"]')
        for pi_property in full_results:
            print(get_location(pi_property).extract_first())
            print(get_price(pi_property).extract_first())
            print(get_square_meters(pi_property).extract_first())
            print(get_link(pi_property, response))


def get_location(selector):
    return selector.xpath("div/div/h4/a/text()")


def get_price(selector):
    return selector.xpath('.//span[@class="product-property-value product-price-value"]/text()')


def get_square_meters(selector):
    return selector.xpath('.//span[@class="product-property-value"]/text()')


def get_link(selector, response):
    relative_url = selector.xpath('.//h4/a/@href').extract_first()
    return response.urljoin(str(relative_url))

