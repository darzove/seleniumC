"""
This is a simple wrapper around selenium to avoid boilerplate for scraping projects
It also has some built in convenience functions, allowing for injecting scripts prior to DOM loading,
automatically injecting needed dependencies (namely jQuery), detection avoidance features, adBlock,
virtual display for headless mode (if running on a box), etc
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlopen
from random import randint

class SeleniumC():
    def __init__(self, config):
        self.config = config
        self.driver = None
        self.jq = self.load_jQuery()
        self.display = self.virtual_display()

    def get(self, url, jq=True):
        self.driver.get(url)
        if jq:
            self.driver.execute_script(self.jq)

    #This method ensures we find a given identifier on the page, retrying n times
    def try_n_times(self, n, identifier, by=By.ID, timeout=10):
        for i in range(n):
            elem = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by, identifier))
            if elem is not None:
                return True
            else:
                continue
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
            from pyvirtualdisplay import Display
            size = (randint(self.config['WIDTH']), randint(self.config['HEIGHT']))
            return Display(visible=0, size=size).start()
        else:
            return None

    def close(self):
        self.driver.close()
        if self.display is not None:
            self.display.stop()



