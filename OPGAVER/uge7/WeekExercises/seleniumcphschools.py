from selenium import webdriver

MAX_PAGE_NUM = 5

with open('results.csv', 'w') as f:
    f.write("schoolName, stars \n")

# Open up a chrome browser and navigate to web page.
driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_NUM - len(str(i))) + "0" + str


driver.get(
    "https://www.google.com/search?sz=0&biw=929&bih=888&q=copenhagen+schools&npsic=0&rflfq=1&rlha=0&rllag=55689668,12565818,3201&tbm=lcl&ved=2ahUKEwiWsPG6g4vpAhUMDewKHak2CgIQjGp6BAgLEEM&tbs=lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2&rldoc=1#rlfi=hd:;si:;mv:[[55.735535299999995,12.6451142],[55.643689699999996,12.4610018]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:2")

# Extract lists of "schoolnames" and "stars" based on xpath.
schoolName = driver.find_elements_by_xpath('//div[@class="dbg0pd"]')
# print(schoolName)
stars = driver.find_elements_by_xpath('//span[@class="BTtC6e"]')
# print(stars)

# printing schoolnames and stars:
num_page_items = len(schoolName)
for i in range(num_page_items):
    print(schoolName[i].text + " : " + stars[i].text)

# close browser
driver.close
