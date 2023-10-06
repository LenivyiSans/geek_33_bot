# from parsel import Selector
# import requests
#
#
# class NewsScraper:
#     PLUS_URL = 'https://kaktus.media'
#     URL = "https://kaktus.media/?lable=8&date=2023-10-02&order=time"
#     LINK_XPATH = '//div[@class="Tag--article"]/div/div/a/@href'
#     TITLE_XPATH = '//div[@class="Tag--article"]/div/div/a/@href'
#
#     def parse_data(self):
#         html = requests.get(url=self.URL).text
#         tree = Selector(text=html)
#         links = tree.xpath(self.LINK_XPATH).extract()
#         title = tree.xpath(self.TITLE_XPATH).extract()
#         # for link in links:
#         #     print(link)
#
#         return links[:5]
#     print(links)
#
#
# if __name__ == "__main__":
#     scraper = NewsScraper()
#     scraper.parse_data()