import scrapy
from ..items import GoodreadsItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.goodreads.com/genres']

    def parse(self, response, **kwargs):
        links = response.xpath(
            '//div[@class="bigBoxContent containerWithHeaderContent"]/div[@class="left"]/a/@href').getall()

        for link in links:
            link = 'https://www.goodreads.com' + link
            yield response.follow(link, callback=self.book_page)

    def book_page(self, response):
        books = response.xpath('//div[@class="leftAlignedImage bookBox"]/div[@class="coverWrapper"]/a/@href').getall()

        for book in books:
            yield response.follow(book, callback=self.parse_book)

    def parse_book(self, response):
        title = response.xpath('//div[@class="BookPageTitleSection__title"]/h1/text()').get()
        author = response.xpath('//a[@class="ContributorLink"]/span/text()').get()
        description = response.xpath('//div[@class="DetailsLayoutRightParagraph__widthConstrained"]/span').get()
        rating = response.xpath(
            '//div[@class="RatingStatistics__column"]/div[@class="RatingStatistics__rating"]').get()
        total_rating = response.xpath(
            '//div[@class="RatingStatistics__column"]/div[@class="RatingStatistics__meta"]/span').get()
        genre = response.xpath(
            '//div[@class="BookPageMetadataSection__genres"]/ul[@class="CollapsableList"]/span').extract_first()

        yield {'author': author,
               'description': description,
               'genre': genre,
               'rating': rating,
               'title': title,
               'total_rating': total_rating}
