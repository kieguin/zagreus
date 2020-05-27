import sys
import time
from selenium.common.exceptions import NoSuchElementException
from utils.pretty_print import prettyPrint
from utils.helpers import *

class InstagramChecker:

    def __init__(self, Zagreus):
        prettyPrint('info', 'Instagram Checker Loaded.')
        self.Zagreus = Zagreus
        self.config = Zagreus.config

    def login(self, username, password):

        # Set the authenticated flag.
        Authenticated = False
        
        # Attempt to load the instagram login page and check for the logged out wordmark.
        try: 
            self.browser.get('https://www.instagram.com/accounts/login/')
            self.browser.implicitly_wait(self.wait_time)
            self.browser.find_element_by_class_name('coreSpriteLoggedOutWordmark')
        except NoSuchElementException as e:
            prettyPrint('error', 'Something Wen\'t Wrong: ' + e.msg)
            prettyPrint('warning', 'StackTrace: ' + str(e.stacktrace))
            closeBrowserAndExit(self)

        # Attempt to find the input fields.
        try: 
            usernameInput = self.browser.find_elements_by_css_selector('form input')[0]
            passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
        except IndexError as e:
            prettyPrint('error', 'Something wen\'t wrong finding the login fields.')
            closeBrowserAndExit(self)

        # Attempt to enter the provided username, password and then press enter.
        try:
            usernameInput.send_keys(username)
            passwordInput.send_keys(password)
            passwordInput.send_keys(self.Keys.ENTER)
        except: 
            prettyPrint('error', 'Something wen\'t wrong entering the details provided.')
            closeBrowserAndExit(self)

        # Simple check to see if the user has logged in succesffully.
        try:
            time.sleep(2)
            self.browser.find_element_by_id('slfErrorAlert')
            Authenticated = False
            prettyPrint('warning', f"WARNING: {username}:{password} not working!")
        except NoSuchElementException:
            Authenticated = True
            prettyPrint('success', f"SUCCESS: {username}:{password} working!")
            closeBrowserAndExit(self)

        closeBrowserAndExit(self)
