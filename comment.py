import csv
import time

import requests
from selenium import webdriver

# 引入driver
chromedriver = "driver/chromedriver"
browser = webdriver.Chrome(chromedriver)

comment_url = "https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=223205951&clazzid=52049524&cpi=161306048&enc" \
              "=89cde758bfa7ce4626a1d114da6bad1e&t=1653612717461&pageHeader=2 "

browser.get(comment_url)
time.sleep(2)

name_input = browser.find_element_by_css_selector("#phone")
pwd_input = browser.find_element_by_css_selector("#pwd")
name_input.send_keys('15779703454')
pwd_input.send_keys('izumiChan0816')

browser.find_element_by_css_selector("#loginBtn").click()
time.sleep(3)
# 打开网页


with open('resources/100.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        browser.switch_to.frame(0)
        browser.switch_to.frame(0)
        browser.find_element_by_css_selector('body').clear()
        browser.find_element_by_css_selector('body').send_keys(row)
        time.sleep(1)
        browser.switch_to.default_content()
        browser.switch_to.frame(0)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div[2]').click()
        browser.switch_to.default_content()
        time.sleep(5)
