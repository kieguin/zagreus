'''
Zagreus - v0.1.0
Generate, Check and Manage social accounts.
Created by 0x51D <0x51D#5213>
wwww.github.com/0x51D/zagreus
'''

import time
import sys
import os
import io
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser

# Import our required utils.
from utils.pretty_print import prettyPrint

# Import all our checking modules.
from checkers.instagramChecker import InstagramChecker

# Setup our config injection.
config = ConfigParser()
config.read('client/config.ini')

class Zagreus:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('window-size=700x570')
        self.browser = webdriver.Chrome(options=self.options)
        self.Keys = Keys
        self.config = config
        self.wait_time = config.get('core', 'wait_time')

Zagreus = Zagreus()
CheckInstagram = InstagramChecker(Zagreus)
InstagramChecker.login(Zagreus, '0x51d', 'password')