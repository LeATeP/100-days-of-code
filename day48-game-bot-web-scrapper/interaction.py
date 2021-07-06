from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
from time import sleep


def check_and_buy():
    money = driver.find_element_by_xpath('// *[ @ id = "money"]').text
    money = int(money.replace(",", ""))

    store = driver.find_element_by_xpath('//*[@id="store"]')
    item = store.find_elements_by_css_selector('b')
    for n in item:
        index = item.index(n)

        item2, item1 = int(item[index + 1].text.split()[2].replace(",", "")), int(n.text.split()[2].replace(",", ""))
        print(item1)
        if item1 > money:
            break
        elif index != 7 and item2 > money >= item1:
            item[index].click()
            break
        elif index == 7 and money >= item[7]:
            item[7].click()
            break


def cookie_click():
    cookie = driver.find_element_by_xpath('//*[@id="cookie"]')
    cookie.click()


chrome_driver = "D:/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie_click()

in_game = True
while in_game:
    sleep(0.01)
    cookie_click()
    seconds = int(dt.today().strftime('%S'))
    if seconds % 5 == 0:
        print(seconds)
        check_and_buy()
