import os

from selenium import webdriver

from config import DATA_DIR, ROOT_DIR, EC_WAIT


def create_chrome_driver():
    options = webdriver.ChromeOptions()

    # 창 숨기는 옵션 추가
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--log-level=3')
    options.add_argument('--disable-logging')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--disable-setuid-sandbox')

    if os.name == 'nt':
        driver_path = ROOT_DIR + '/driver/chromedriver.exe'
        download_path = DATA_DIR + "\\driver_download"
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": download_path,  # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
    elif os.name == 'posix':
        driver_path = '/usr/local/bin/chromedriver'
        download_path = DATA_DIR + "/driver_download"
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": download_path,  # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
    else:
        driver_path = '/usr/lib/chromium-browser/chromedriver'
        download_path = DATA_DIR + "/driver_download"
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": download_path,  # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(driver_path, options=options)
    # driver.maximize_window()
    driver.implicitly_wait(EC_WAIT)

    return driver
