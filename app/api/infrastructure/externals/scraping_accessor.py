from app.api.domain.models import NewsEntry
from app.api.domain.repositories import ScrapingRepository
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ScrapingAccessor(ScrapingRepository):
    CHROMEDRIVER = "/opt/chrome/chromedriver"

    def scribe_from_site(self, url: str) -> list[NewsEntry]:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.binary_location = "/usr/bin/google-chrome"

        driver = webdriver.Chrome(executable_path=self.CHROMEDRIVER, chrome_options=options)

        driver.get(url)
        driver.quit()
        return []
