from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import EC_WAIT
from common.crawling_driver import create_chrome_driver
from common.utils import chrome_close, date_change
from monitoring.embassy.site_url import url_dict
from monitoring.model import Content, ContentTable

category = 'CN00'


def monitoring():
    site = url_dict[category]

    driver = create_chrome_driver()
    driver.get(site)
    element = WebDriverWait(driver, EC_WAIT).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/div[2]'))
    )

    table = element.find_element(By.TAG_NAME, 'tbody')
    table_rows = table.find_elements(By.TAG_NAME, 'tr')

    content_table = ContentTable()
    for row in table_rows:
        title = row.find_element(By.TAG_NAME, 'a').text
        if title[:3] == 'NEW': title = title[3:]
        rgsr_dt = row.find_element(By.XPATH, './/td[5]').text
        rgsr_dt = date_change(rgsr_dt, '%Y-%m-%d')
        content_table.add(Content(category, title, rgsr_dt))

    chrome_close(driver)
    content_table.to_sql()


if __name__ == '__main__':
    monitoring()
