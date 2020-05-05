from selenium import webdriver

driver = webdriver.Chrome()

with open('results.csv', 'w') as f:
    f.write("schoolName, stars \n")

    url = "https://www.google.com/search?sz=0&biw=929&bih=888&q=copenhagen+schools&npsic=0&rflfq=1&rlha=0&rllag=55689668,12565818,3201&tbm=lcl&ved=2ahUKEwi8wfOEkovpAhUCDuwKHTJqDy4QjGp6BAgLEEM&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:;mv:[[55.7348505,12.6134975],[55.655788199999996,12.4627915]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2"
    driver.get(url)

schoolName = driver.find_elements_by_xpath('//div[@class="dbg0pd"]')
stars = driver.find_elements_by_xpath('//span[@class="BTtC6e"]')

num_page_items = len(schoolName)
with open('results.csv', 'a') as f:
    for i in range(num_page_items):
        f.write(schoolName[i].text + "," + stars[i].text + "\n")
