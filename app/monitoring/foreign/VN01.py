from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import EC_WAIT
from common.crawling_driver import create_chrome_driver
from common.utils import chrome_close, date_change
from monitoring.embassy.site_url import url_dict
from monitoring.model import Content, ContentTable

category = 'BE00'


def monitoring():
    pass