import argparse 
import logging

from yaml.parser import Parser
logging.basicConfig(level=logging.INFO)

from common import config 

logger = logging.getLogger(__name__)

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info(f'Begining scrape for {host}')


if __name__ == "__main __":
    parser = argparse.ArgumentParser()

    news_sites_choises = list(config()['news_sites'].keys())
    parser.add_argument('neews_site',
                        help='The news site that you want to scrape',
                        type=str,
                        choises=news_sites_choises)

    args = parser.parse_args()
    _news_scraper(args.news_site)