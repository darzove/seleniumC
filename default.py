config = {
    'BINARY_PATH': './chromedriver',
    'ARGS': ['disable-infobars', 'user-agent=Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'],
    'HEADLESS': False,
    'VIRTUAL': False, #run virtual True if you are using a box without a real monitor connected
    #widths and heights are important for window resizing as well as virtual display settings
    'WIDTH': (480, 1920), #(min,max)
    'HEIGHT': (360, 1080), #(min,max)
    'JQ_PATH': None,
    'JQ_URL': 'https://code.jquery.com/jquery-3.4.1.min.js',
    'ADBLOCK': True,
    'ADBLOCK_XPI': None,
    'ADBLOCK_CRX': './3.6.3_0.crx'
}