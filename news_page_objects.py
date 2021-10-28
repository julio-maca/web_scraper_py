import bs4 
import requests

from common import config

class HomePage: 
    def __init__(self, news_site_uid, url):
        self._config = config()['news_sites'] [news_site_uid]
        self._queries = self._config['queries']
        self._html = None

        self.visit(url)

    def _visit(self, url):
        response = request.get(url)

        response.raise_for_status()

        self.html = bs4.BeautifulSoup(response.text, 'html.parcer')


    @property
    def article_links(self):

        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.hass_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)

    def _select(self, query_string):
        return self._html.select(query_string)
