import sys
import time
from selenium.common.exceptions import NoSuchElementException
from utils.pretty_print import prettyPrint
from utils.helpers import *

class InstagramChecker:

    def __init__(self, Zagreus):
        prettyPrint('info', 'Instagram Checker Loaded.')
        self.Zagreus = Zagreus
    
    def login(self, username, password):

        # Set the authenticated flag.
        Authenticated = False
        
        # Attempt to load the instagram login page and check for the logged out wordmark.
        try: 
            self.browser.get('https://www.instagram.com/accounts/login/')
            self.browser.implicitly_wait(2)
            self.browser.find_element_by_class_name('coreSprteLoggedOutWordmark')
        except NoSuchElementException as e:
            prettyPrint('error', 'Something Wen\'t Wrong: ' + e.msg)
            prettyPrint('stack', 'StackTrace: ' + str(e.stacktrace))
            closeBrowserAndExit(self)

        # Attempt to find the input fields.
        try: 
            usernameInput = self.browser.find_elements_by_css_selector('form input')[0]
            passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
        except IndexError as e:
            print(e.msg)
            self.browser.close()
            sys.exit()

        # Attempt to enter the provided username, password and then press enter.
        try:
            usernameInput.send_keys(username)
            passwordInput.send_keys(password)
            passwordInput.send_keys(self.Keys.ENTER)
        except: 
            print('Something went wrong while entering the users details...')
            self.browser.close()
            sys.exit()

        # Simpole check to see if the user has logged in succesffully.
        try:
            self.browser.implicitly_wait(3)
            self.browser.find_element_by_class_name('_47KiJ')
            Authenticated = True
        except:
            self.browser.close()
            Authenticated = False
            print('Not logged in...')
            sys.exit()

        if Authenticated == True:
            print('Logged in sucessfully.')

        self.browser.close()
        sys.exit()
