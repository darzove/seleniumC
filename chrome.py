from selenium import webdriver
from driver import SeleniumC
from default import config

class Chrome(SeleniumC):
    def __init__(self, config=config):
        super().__init__(config)
        self.driver = self.get_driver()

    def get_driver(self):
        options = webdriver.ChromeOptions()
        if self.config['HEADLESS']:
            options.headless = True

        for arg in self.config['ARGS']:
            options.add_argument(arg)

        #AFAIK headless still doesnt work with extensions, although I have heard some tomfoolery on the matter
        if not self.config['HEADLESS'] and self.config['ADBLOCK'] and self.config['ADBLOCK_CRX'] is not None:
            options.add_extension(self.config['ADBLOCK_CRX'])

        return webdriver.Chrome(chrome_options=options, executable_path=self.config['BINARY_PATH'])
