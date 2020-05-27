'''
Zagreus - v0.1.0
Generate, Check and Manage social accounts.
Created by 0x51D <0x51D#5213>
wwww.github.com/0x51D/zagreus
'''

import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from checkers.instagramChecker import InstagramChecker

class Zagreus:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('window-size=700x570')
        self.browser = webdriver.Chrome(options=self.options)
        self.Keys = Keys

    def testSelenium(self):
        self.browser.get('https://zagreus.0x51d.fun')
        self.browser.implicitly_wait(10)

Zagreus = Zagreus()
CheckInstagram = InstagramChecker(Zagreus)
InstagramChecker.login(Zagreus, 'kieran', 'password')
# Zagreus.testSelenium()
time.sleep(5)