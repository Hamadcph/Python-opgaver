from selenium import webdriver

driver = webdriver.Chrome()

with open('iphones.csv', 'w') as f:
    f.write("title, price")

    url = "https://www.pricerunner.com/cl/1/Mobile-Phones?q=iphone%2011"
    driver.get(url)

title = driver.find_elements_by_xpath('//h3[@class="_1jlH40g035 fuQfQrNu3i"]')
price = driver.find_elements_by_xpath(
    '//span[@class="_5PAGMLoZx1 _3kmphLYvsN _3QA1aV3-Qo _25u3hNZfKi"]')

num_page_items = len(title)
with open('iphones.csv', 'a') as f:
    for i in range(num_page_items):
        f.write("\n" + title[i].text + "," + price[i].text + "\n")
