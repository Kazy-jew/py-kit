from selenium import webdriver
from selenium.webdriver.common.by import By
from calendargen import Calendar
import time
import os
from selenium.common.exceptions import NoSuchElementException as NSe


def pixiv_daily():
    skip = 0
    root = os.path.expanduser('~')
    chrome_data = r'AppData\Local\Google\Chrome\User Data'
    data_dir = os.path.join(root, chrome_data)
    # change to your own proxy address
    http_proxy = "127.0.0.1:7890"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server={}'.format(http_proxy))
    # change to your own chrome profile path, you can find it under chrome://version/
    chrome_options.add_argument("--user-data-dir={}".format(data_dir))
    # chrome_options.add_argument('--profile-directory=C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
    # chrome_options.add_extension("C:\\Users\\Administrator\\Desktop\\dkndmhgdcmjdmkdonmbgjpijejdcilfh.crx")
    chrome_options.add_experimental_option("detach", True)
    dates = daily_gen()
    driver = webdriver.Chrome(options=chrome_options)
    for _ in dates:
        url = 'https://www.pixiv.net/ranking.php?mode=daily&date={}'.format(_)
        driver.get(url)
        dl_btn = driver.find_element(By.XPATH, '//*[@id="openCenterPanelBtn"]')
        dl_btn.click()
        crawl_debut = driver.find_element(By.XPATH, '/html/body/div[6]/div[4]/slot/form/div[1]/div/slot[1]/button[2]')
        crawl_debut.click()
        # default download interval for each day
        time.sleep(120)
        # check if download is complete every 20s after default interval
        while not complete(driver):
            time.sleep(20)
            # skip current date if not complete in 10min
            skip += 20
            # refresh the page every 200 seconds. sometimes useful if download stuck
            if skip % 200 == 0:
                driver.refresh()
            # skip current date if download time exceeds 10 minutes
            if skip > 600:
                print("date {} not finished".format(_))
                break


def daily_gen():
    I = Calendar()
    # I.year = 2021
    # year = I.year
    dates = I.input_dates()
    return dates

def complete(driver):
    try:
        case1 = driver.find_elements(By.XPATH, '//*[@id="logWrap"]')
        # case2 = driver.find_element_by_xpath('/html/body/div[1]/span[5]')
        print(case1[0].text)
        if "download complete" in case1[0].text.lower():
            return "Complete"
    except NSe:
        return False


if __name__ == '__main__':
    pixiv_daily()