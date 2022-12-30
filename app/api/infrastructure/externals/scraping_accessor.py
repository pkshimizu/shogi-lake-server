from app.api.domain.models import NewsEntry
from app.api.domain.repositories import ScrapingRepository
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service as fs


class ScrapingAccessor(ScrapingRepository):
    CHROMEDRIVER = "/opt/chrome/chromedriver"

    def scribe_from_site(self, url: str) -> list[NewsEntry]:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        chrome_service = fs.Service(executable_path=self.CHROMEDRIVER)
        driver = webdriver.Chrome(service=chrome_service, options=options)

        driver.get(url)
        return []
