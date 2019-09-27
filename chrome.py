from selenium import webdriver
from seleniumC.driver import SeleniumC
from seleniumC.default import config
import json

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

        if self.config['BINARY_PATH'] is not None:
            return webdriver.Chrome(chrome_options=options, executable_path=self.config['BINARY_PATH'])
        else:
            try:
                return webdriver.Chrome(chrome_options=options)
            except:
                Exception('Unable to find chromedriver, please specify the correct path to the binary in your config')

    def send_command(self, command, params=[]):
        target = f"/session/{self.driver.session_id}/chromium/send_command_and_get_result"
        url = self.driver.command_executor._url + target
        body = json.dumps({'cmd': command, 'params': params})
        res = self.driver.command_executor._request('POST', url, body)
        return res.get('value')

    def inject(self, script):
        self.send_command('Page.addScriptToEvaluateOnNewDocument', {"source": script})