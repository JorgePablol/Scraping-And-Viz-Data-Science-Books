import scrapy 

#book_links_from_search = //h2/a[@class="a-link-normal a-text-normal"]/@href

#next_page = //li[@class="a-last"]/a/@href
#titles = //span[@id="productTitle"]/text()
#stars = //span[@class="a-icon-alt"]/text()
#cost = //span[@class="a-size-medium a-color-price offer-price a-text-normal"]/text()
#reviewrs = //span[@id="acrCustomerReviewText"]/text()'


#2nd Iteration: We will add multiple cost nodes due to many null datapoints

#cost2 = //span[@class="a-color-secondary"]/span[@class="a-size-base a-color-secondary"]/text()

#kindle = //tr[@class="kindle-price"]/td[@class="a-color-price a-size-medium a-align-bottom"]/span[@class="a-size-medium a-color-price"]/text()

#kindle2 = //span[@class="a-color-base"]/span[@class="a-size-base a-color-price a-color-price"]/text()

#kindle3 = //td[@class="a-color-price a-size-medium a-align-bottom"]/span[@class="a-size-medium a-color-price"]/text()

#cost3 = //span[@class="a-size-medium a-color-price"]/text()

#https://www.amazon.com/s?k=data+science&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss



class SpiderBooks(scrapy.Spider):
    name = 'Juno'

    start_urls = [
        'https://www.amazon.com.mx/s?k=data+science&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2'
    ]

    custom_settings = {
        'USER_AGENT': 'Mozilla5.0',
        'FEED_URI': 'ds_books_MX_january.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
	'DOWNLOAD_DELAY': 0.5,
	'CONCURRENT_REQUESTS': 24
    }

    def parse(self, response):

        links_books = response.xpath(
            '//h2/a[@class="a-link-normal a-text-normal"]/@href').getall()

        for link in links_books:
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url':response.urljoin(link)})




        next_page_button_link = response.xpath('//li[@class="a-last"]/a/@href').get()

        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)



    def parse_link(self, response, **kwargs):
        
        link = kwargs['url']
        title = response.xpath('//span[@id="productTitle"]/text()').get()
        stars = response.xpath('//span[@class="a-icon-alt"]/text()').get()
        cost = response.xpath('//span[@class="a-size-medium a-color-price offer-price a-text-normal"]/text()').get()
        reviewers = response.xpath('//span[@id="acrCustomerReviewText"]/text()').get()

        #2nd Iteration : 

        cost_2 = response.xpath('//span[@class="a-color-secondary"]/span[@class="a-size-base a-color-secondary"]/text()').get()

        cost_3 = response.xpath('//span[@class="a-size-medium a-color-price"]/text()').get()
        kindle = response.xpath('//tr[@class="kindle-price"]/td[@class="a-color-price a-size-medium a-align-bottom"]/span[@class="a-size-medium a-color-price"]/text()').get()
        kindle_2 = response.xpath('//span[@class="a-color-base"]/span[@class="a-size-base a-color-price a-color-price"]/text()').get()
        kindle_3 = response.xpath('//td[@class="a-color-price a-size-medium a-align-bottom"]/span[@class="a-size-medium a-color-price"]/text()').get()





        yield {
            'url': link,
            'title': title,
            'stars': stars,
            'reviewers': reviewers,
            'cost': cost,
            'cost_2': cost_2,
            'cost_3': cost_3,
            'kindle': kindle,
            'kindle_2': kindle_2,
            'kindle_3': kindle_3
            }
