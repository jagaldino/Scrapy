from scrapy import Spider

class AdoroCinemaSpider(Spider):
    name = 'adorocinema'
    start_urls = ['https://www.adorocinema.com/filmes/melhores/']

    def parse(self, response):
        movies = response.xpath("//div[contains(@class, 'card-list')]")
        for movie in movies:
            yield {
                "title": movie.css("a.meta-title-link::text").get(),
                "duration": movie.css("div.meta-body-item.meta-body-info::text").get().replace("\n", ""),
                "original_title": movie.css("span.dark-grey::text").get(),
            }
