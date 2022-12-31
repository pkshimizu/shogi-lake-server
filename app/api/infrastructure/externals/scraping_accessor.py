import requests

from app.api.domain.models import NewsEntry
from app.api.domain.repositories import ScrapingRepository
from bs4 import BeautifulSoup
from lxml import html


class ScrapingAccessor(ScrapingRepository):
    CHROMEDRIVER = "/opt/chrome/chromedriver"

    def scribe_from_site(
        self,
        url: str,
        url_xpath: str,
        title_xpath: str,
        date_xpath: str,
        news_entry_type: type[NewsEntry],
        provider_uid: str,
    ) -> list[NewsEntry]:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        dom = html.fromstring(str(soup))
        url_list = dom.xpath(url_xpath)
        title_list = dom.xpath(title_xpath)
        published_at_list = dom.xpath(date_xpath)
        if not (len(url_list) == len(title_list) == len(published_at_list)):
            print(len(url_list))
            print(len(title_list))
            print(len(published_at_list))
        news_entries = []
        for index, url in enumerate(url_list):
            news_entries.append(
                news_entry_type(
                    url=url.get("href"),
                    title=title_list[index].text.strip(),
                    published_at=published_at_list[index].text.strip(),
                    provider_uid=provider_uid,
                )
            )
        return news_entries
