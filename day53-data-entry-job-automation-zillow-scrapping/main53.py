from selenium import webdriver

chrome_driver = "D:/Development/chromedriver"
docs_link = "https://forms.gle/2Hppw4CCGJ11r6Zv8"

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.53752745581055%2C%22east%22%3A-122.32913054418945%2C%22south%22%3A37.656879965418064%2C%22north%22%3A37.89351359163887%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D")

listings = driver.find_element_by_xpath('//*[@id="grid-search-results"]/ul')
for n in listings:
    print(n.text)
    e = n.find_elements_by_name('a')
    print(f"e \n{e}")
