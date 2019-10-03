# SeleniumC

### Overview
SeleniumC is a simple wrapper around selenium to remove a lot of boilerplate from all of the scraping projects.
It supports both chrome and firefox, although firefox has some limits on functionality. Primarily is the ability to preload scripts prior to the DOM. 
Because chrome supports this, it gives us significant flexibility in obscuring the driver itself to prevent detection - see `extension/base.js`

Written in python3.7

#### driver.py
The `SeleniumC` class takes care of the generic and shared items between both firefox and chrome. 
It will set up a virtualdisplay to run on vm's if not in headless mode.
`SeleniumC.get()` wraps the selenium get function but also automatically loads jQuery for convenience. If enabled, it also increments the resize counter which will change window sizing periodically to avoid fingerprinting/detection.
Beyond the basic functionality added here, the driver itself is still exposed for more complex operations.

#### chrome.py
Use this class for chrome instances. Chrome loads extensions only if not in headless (I believe this has changed since i wrote this package, but have not tested).

#### ff.py
Use this class for firefox instances.


#### Usage
This package may be installed by putting the folder in your python site-packages folder.
This may be found by running `python -m site`

```
from seleniumC.chrome import Chrome

c = Chrome()
c.preload("console.log('This will appear at the top of console');")
c.get('http://impactresearchinc.com')
c.close()
```
