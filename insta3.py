import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import sys


class InstagramBot:

    def __init__(self, username, password):

        chrome_options = Options()
        #chrome_options.add_argument("--headless")

        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


    def login(self, num):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")

        #login
        driver.find_element_by_name("username").send_keys(self.username)
        #password
        driver.find_element_by_name("password").send_keys(self.password)
        #sign in
        driver.find_element_by_css_selector("._0mzm-.sqdOP.L3NKy").click()
        time.sleep(2)
        driver.get("https://www.instagram.com/explore/tags/cute/")
        driver.find_element_by_class_name("_9AhH0").click()
        time.sleep(1)

        '''
        full_heart = driver.find_elements_by_css_selector(".glyphsSpriteHeart__filled__24__red_5.u-__7")
        print(len(full_heart))
        '''

        for i in range(500):
            full_heart = driver.find_elements_by_css_selector(".glyphsSpriteHeart__filled__24__red_5.u-__7")

            if len(full_heart) > 0:
                full_heart = []
                driver.find_element_by_css_selector(".HBoOv.coreSpriteRightPaginationArrow").click()
                #continue
            else:
                #like
                driver.find_element_by_css_selector(".dCJp8.afkep.coreSpriteHeartOpen._0mzm-").click()
                #driver.find_element_by_css_selector(".glyphsSpriteHeart__outline__24__grey_9").click()
                #time.sleep(2)
                                                    #glyphsSpriteHeart__outline__24__grey_9 u-__7
                #driver.find_element_by_css_selector(".textarea.Ypffh").send_keys("This is cool")
                driver.find_element_by_css_selector(".HBoOv.coreSpriteRightPaginationArrow").click()
                #time.sleep(1)


            #time.sleep(1)


if __name__ == "__main__":

    x = int(input("How many times do you want it to iterate? "))

    username = "brandonj_iam"
    password = "johnson0416"

    ig = InstagramBot(username, password)
    ig.login(x)
