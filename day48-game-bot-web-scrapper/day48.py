from selenium import webdriver

chrome_driver = "D:/Development/chromedriver"

"medium-widget event-widget last"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.python.org/")
time_columm = driver.find_elements_by_css_selector(".event-widget time")
news_columm = driver.find_elements_by_css_selector(".event-widget li a")
stack = {}

for n in range(len(time_columm)):
    stack[n] = {
        "time": time_columm[n].text,
        "name": news_columm[n].text
    }
print(stack)
driver.quit()