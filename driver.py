"""
This is a simple wrapper around selenium to avoid boilerplate for scraping projects
It also has some built in convenience functions, allowing for injecting scripts prior to DOM loading,
automatically injecting needed dependencies (namely jQuery), detection avoidance features, adBlock,
virtual display for headless mode (if running on a box), etc
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.request import urlopen
from random import randint
from time import sleep

class SeleniumC():
    def __init__(self, config):
        self.config = config
        self.driver = None
        self.jq = self.load_jQuery()
        self.display = self.virtual_display()
        self.on_page_load = None
        self.page_counter = 0

    def get(self, url, jq=True):
        if self.config['VERBOSE']:
            print(f"GETTING {url}")

        if self.config['DELETE_COOKIES']:
            self.driver.delete_all_cookies()

        try:
            self.driver.get(url)
        except TimeoutException:
            if self.config['VERBOSE']:
                print(f'Timeout attempting to get {url}')
            return False

        if jq:
            self.driver.execute_script(self.jq)

        if self.on_page_load is not None:
            self.driver.execute_script(self.on_page_load)

        self.page_counter += 1
        if self.page_counter > self.config['RESIZE_LIMIT']:
            self.resize()

        sleep(randint(*self.config['SLEEP_RANGE']))
        return True

    #This method ensures we find a given identifier on the page, retrying n times
    def wait_for(self, identifier, n=2, by=By.ID, timeout=10):
        for i in range(n):
            try:
                elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, identifier)))
                if elem is not None:
                    return True
                else:
                    continue
            except:
                continue
        if self.config['VERBOSE']:
            print(f'Failed to find element {identifier}')
        return False

    #loads jQuery as a resource if/when it is needed.
    def load_jQuery(self):
        if self.config['JQ_PATH'] is not None:
            with open(self.config['JQ_PATH'], 'r') as jq:
                return jq.read()
        else:
            return urlopen(self.config['JQ_URL']).read().decode()

    #If we aren't running headless and don't have a monitor, we can still scrape!
    def virtual_display(self):
        if self.config['VIRTUAL'] and not self.config['HEADLESS']:
            if self.config['VERBOSE']:
                print('STARTING VIRTUAL DISPLAY')
            from pyvirtualdisplay import Display
            size = (randint(*self.config['WIDTH']), randint(*self.config['HEIGHT']))
            return Display(visible=0, size=size).start()
        else:
            return None

    def resize(self, width=None, height=None):
        self.page_counter = 0
        if width is None:
            width = randint(*self.config['WIDTH'])
        if height is None:
            height = randint(*self.config['HEIGHT'])
        if self.config['VERBOSE']:
            print(f'Set window size to {width}x{height}')
        self.driver.set_window_size(width, height)

    def close(self):
        if self.config['VERBOSE']:
            print('Closing. Goodbye!')
        self.driver.close()
        if self.display is not None:
            self.display.stop()




