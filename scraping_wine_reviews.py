import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
from time import sleep
import urllib

import requests



wine_varieties = ['Pinot Noir', 'Chardonnay', 'Cabernet Sauvignon', 'Shiraz/Syrah', 'Sauvignon Blanc', 'Riesling', 
'Merlot', 'Sangiovese', 'Zinfandel', 'Rose', 'Tempranillo', 'Pinot Grigio/Gris','Cabernet Franc', 'Gruner Veltliner',
'Viognier', 'Barbera', 'Bordeaux-style', 'Zinfandel' ]



def scrape_wine_links(base_url, min_page_number, max_page_number, proxies, header):
    wine_pages_to_mine = []
    for page_number in range(min_page_number, max_page_number):
        url_to_mine = base_url + str(page_number)
        r = requests.Session()
        r.proxies = proxies
        r.headers = header
        try:
            response = r.get(url_to_mine)
            soup = BeautifulSoup(response.content, 'html.parser')

            all_wine_links = soup.find_all("a", class_="review-listing")
            all_wine_links = [a.get('href') for a in all_wine_links]
            wine_pages_to_mine.extend(all_wine_links)
        except:
            continue

    series_wine_pages = pd.Series(wine_pages_to_mine)
    series_wine_pages.to_csv('data/wine_pages_to_mine.csv')
    return wine_pages_to_mine


class WineInfoScraper:

    def __init__(self, wine_page_to_mine, proxies, header):
        self.page = wine_page_to_mine
        self.proxies = proxies
        self.user_agent = header


    def get_soup_wine_page(self):

        r = requests.Session()
        r.proxies = self.proxies
        r.headers = self.user_agent
        wine_review_response = r.get(self.page)

        wine_review_soup = BeautifulSoup(wine_review_response.content, 'html.parser')
        return wine_review_soup


    def get_wine_name(self, soup):
        wine_name_raw = soup.find(class_='title')
        wine_name_clean = wine_name_raw.text
        
        return wine_name_clean


    def get_vintage(self, wine_name_clean):
        name_strings = wine_name_clean.split(' ')
        number_strings = [i for i in name_strings if (i.isnumeric())]
        for n in number_strings:
            if 1900 < int(n) < datetime.datetime.now().year:
                vintage = n
                return vintage
            else:
                continue


    def get_wine_rating(self, soup):
        wine_rating_raw = soup.find(class_='rating')
        wine_rating_text = wine_rating_raw.text
        wine_rating_list = wine_rating_text.split('\n')
        wine_rating_clean = wine_rating_list[1]
        return wine_rating_clean


    def get_wine_description(self, soup):
        wine_description_raw = soup.find(class_='description')
        wine_description_clean = wine_description_raw.text
        return wine_description_clean


    def chunks(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]


    def get_wine_info(self, soup, primary_secondary):
        wine_info_raw = soup.find(class_=primary_secondary)
        wine_info_text = wine_info_raw.text
        wine_info_list = wine_info_text.split('\n')
        wine_info_list_no_blanks = [w for w in wine_info_list if len(w) > 1]

        # Break the list of wine information up into chunks of two
        wine_info_list_chunked = list(self.chunks(wine_info_list_no_blanks, 2))

        # Each chunk will consist of a label and a value. Put these into a dictionary format for easier navigating
        wine_info_dict = {}
        for w in wine_info_list_chunked:
            # When extracting the price make sure to eliminate the 'noise' in the text string
            if w[0] == 'Price':
                clean_price_list = str(w[1]).split(',')
                wine_info_dict['Price'] = clean_price_list[0]
                continue

            # when extracting hte appellation then ma
            if w[0] == 'Appellation':
                appellation_split = w[1].split(',')
                wine_info_dict['Country'] = appellation_split[-1]
                if len(appellation_split) > 1:
                    wine_info_dict['Province'] = appellation_split[-2]
                if len(appellation_split) > 2:
                    wine_info_dict['Region'] = appellation_split[-3]
                if len(appellation_split) > 3:
                    wine_info_dict['Subregion'] = appellation_split[-4]

            if len(w) >= 2:
                wine_info_dict[w[0]] = w[1]

            else:
                continue

        return wine_info_dict




    def scrape_all_info(self):
        wine_info_dict = {}
        wine_review_soup = self.get_soup_wine_page()
   

        wine_info_dict['Name'] = self.get_wine_name(wine_review_soup)
        wine_info_dict['Vintage'] = self.get_vintage(wine_info_dict['Name'])
        wine_info_dict['Rating'] = self.get_wine_rating(wine_review_soup)
        wine_info_dict['Description'] = self.get_wine_description(wine_review_soup)

        wine_info_dict.update(self.get_wine_info(wine_review_soup, primary_secondary='primary-info'))
        wine_info_dict.update(self.get_wine_info(wine_review_soup, primary_secondary='secondary-info'))

   

        return wine_info_dict


def mine_all_wine_info(max_page_number=700, wine_variety="Zinfandel"):
    all_wine_links = scrape_wine_links(base_url=f'https://www.winemag.com/?s=&drink_type=wine&varietal={wine_variety}&page=',
                                       min_page_number=1,
                                       max_page_number=max_page_number,
                                       proxies={'http': 'http://user:pass@13.59.204.225:8080'},
                                       header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

    all_wine_info = []
    for link in all_wine_links:
        try:
            scraper = WineInfoScraper(wine_page_to_mine=link, proxies={'http': 'http://user:pass@13.59.204.225:8080'}, header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
            wine_info = scraper.scrape_all_info()
            all_wine_info.append(wine_info)
            
        except Exception as e:
            print(e)
            continue
        # sleep(5)

    full_wine_info_dataframe = pd.DataFrame(all_wine_info)
    full_wine_info_dataframe = full_wine_info_dataframe[['Alcohol', 'Appellation', 'Bottle Size', 'Category', 'Country',
                                                         'Date Published', 'Description', 'Designation',
                                                         'Name', 'Price', 'Province', 'Rating', 'Region',
                                                        'Subregion', 'User Avg Rating',
                                                         'Variety', 'Vintage', 'Winery']]
    wine_variety= wine_variety.replace("/", "_")
    full_wine_info_dataframe.to_csv(f'data/all_scraped_wine_info_{wine_variety}.csv')

def get_all_varieties(wine_varieties=None):
    for wv in wine_varieties:
        print(f"attempting_wv: {wv}")
        mine_all_wine_info(max_page_number=100, wine_variety=wv)


if __name__ == '__main__':
    get_all_varieties(wine_varieties=['Pinot Noir', 'Chardonnay', 'Cabernet Sauvignon', 'Shiraz/Syrah', 'Sauvignon Blanc', 'Riesling', 
                                    'Merlot', 'Sangiovese', 'Zinfandel', 'Rose', 'Tempranillo', 'Pinot Grigio/Gris','Cabernet Franc', 
                                    'Gruner',  'Veltliner', 'Viognier', 'Barbera', 'Bordeaux-style', 'Zinfandel'])
