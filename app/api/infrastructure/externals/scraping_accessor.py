from datetime import datetime

import requests
from dateutil.relativedelta import relativedelta

from app.api.domain.models import NewsEntry, NewsProvider
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
                NewsEntry(
                    url=self.__convert_url(url.get("href"), provider_uid),
                    title=title_list[index].text.strip(),
                    published_at=self.__convert_datetime(
                        published_at_list[index].text.strip(),
                        provider_uid,
                    ),
                    provider_uid=provider_uid,
                )
            )
        return news_entries

    @staticmethod
    def __convert_url(url: str, provider_uid: str) -> str:
        if provider_uid == NewsProvider.MAINICHI_NEWS_UID:
            return f"https:{url}"
        if provider_uid == NewsProvider.HOKKAIDO_NEWS_UID:
            return f"https://www.hokkaido-np.co.jp{url}"
        return url

    @staticmethod
    def __convert_datetime(text: str, provider_uid: str) -> datetime:
        if provider_uid == NewsProvider.MAINICHI_NEWS_UID:
            return datetime.strptime(text, "%Y/%m/%d %H:%M")
        if provider_uid == NewsProvider.HOKKAIDO_NEWS_UID:
            today = datetime.today()
            text = f"{today.year}/{text}"
            if "更新" in text:
                date = datetime.strptime(text, "%Y/%m/%d %H:%M 更新")
            else:
                date = datetime.strptime(text, "%Y/%m/%d %H:%M")
            if date > today:
                date = date - relativedelta(years=1)
            return date
        return datetime.strptime(text, "%Y/%m/%d %H:%M")
