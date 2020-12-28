from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib import request

SCROLL_PAUSE_TIME = 1

driver = webdriver.Chrome() # call browser driver.
driver.get("https://www.google.co.kr/imghp?hl=en&tab=ri&ogbl") # google image search tab

# finding elements used on web. element name q is user input on search bar.
elem = driver.find_element_by_name("q") 

# send_keys : keyboard input = user inut
elem.send_keys("짤방") 
elem.send_keys(Keys.RETURN) # enter key

# find list of searched images and get first index image
imgList = driver.find_elements_by_class_name('rg_i.Q4LuWd')

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    # TO notify the end of searching
    if new_height == last_height:
        try:
            # click to find more searched items
            driver.find_element_by_class_name('mye4qd').click()
        except:
            break # if there's no more items to be searched, end scroll down.
    last_height = new_height

# downlading searched images
# count = 1
# for img in imgList:
#     img.click()
#     time.sleep(2)
#     imgSrc = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[3]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attrivute('src)
#     request.urlretrieve(imgSrc, f'sample{count}.jpg')
#     count += 1


imgList[0].click()
time.sleep(2) # wait for click first image
# get 
imgSrc = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute('src')
driver.get(imgSrc)

time.sleep(10)
driver.quit()
