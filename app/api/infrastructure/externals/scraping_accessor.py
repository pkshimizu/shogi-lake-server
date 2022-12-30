from datetime import datetime

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
        date_format: str,
        provider_uid: str,
    ) -> list[NewsEntry]:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        dom = html.fromstring(str(soup))
        url_list = dom.xpath(url_xpath)
        title_list = dom.xpath(title_xpath)
        published_at_list = dom.xpath(date_xpath)
        news_entries = []
        for index, url in enumerate(url_list):
            news_entries.append(
                NewsEntry(
                    url=url.get("href"),
                    title=title_list[index].text,
                    published_at=datetime.strptime(
                        published_at_list[index].text, date_format
                    ),
                    provider_uid=provider_uid,
                )
            )
        return news_entries
