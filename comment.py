import csv
import time
from selenium import webdriver


def action():
    # 引入driver，这里替换成你所使用的driver版本
    chromedriver = "driver/chromedriver"
    browser = webdriver.Chrome(chromedriver)

    # 评论课程的链接
    comment_url = "https://mooc2-ans.chaoxing.com/mycourse/stu?courseid=223205951&clazzid=52049524&cpi=161306048&enc" \
                  "=89cde758bfa7ce4626a1d114da6bad1e&t=1653612717461&pageHeader=2 "

    browser.get(comment_url)
    time.sleep(2)

    name_input = browser.find_element_by_css_selector("#phone")
    pwd_input = browser.find_element_by_css_selector("#pwd")
    # 替换成你的用户名
    name_input.send_keys('123456789')
    # 替换成你的密码
    pwd_input.send_keys('123456asdfga')

    browser.find_element_by_css_selector("#loginBtn").click()
    time.sleep(3)
    # 打开网页

    with open('resources/100.csv', encoding="utf-8") as csvfile:
        # 读取评论文件，一行一句话
        reader = csv.reader(csvfile)
        for row in reader:
            # 网页结构是多个iframe的嵌套，这里先进入第一层iframe
            browser.switch_to.frame(0)
            # 进入了第一层以后，再进入第一层里的第一层（也就是主网页的第二层）
            browser.switch_to.frame(0)
            # 查找评论区
            browser.find_element_by_css_selector('body').clear()
            browser.find_element_by_css_selector('body').send_keys(row)
            time.sleep(1)
            # 回到主网页
            browser.switch_to.default_content()
            # 因为提交按钮在主网页的第一层，所以需要重新进入一次
            browser.switch_to.frame(0)
            # 使用xpath定位提交按钮
            browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[4]/div[2]').click()
            # 进入下一次评论前需要回到主网页，否则会保留状态导致无法寻址
            browser.switch_to.default_content()
            time.sleep(5)


if __name__ == '__main__':
    action()
