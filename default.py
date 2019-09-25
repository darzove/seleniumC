config = {
    'BINARY_PATH': './chromedriver',
    'ARGS': ['disable-infobars'],
    'HEADLESS': False,
    'VIRTUAL': False, #run virtual True if you are using a box without a real monitor connected
    #widths and heights are important for window resizing as well as virtual display settings
    'WIDTH': (480, 1920), #(min,max)
    'HEIGHT': (360, 1080), #(min,max)
    'JQ_PATH': None,
    'JQ_URL': 'https://code.jquery.com/jquery-3.4.1.min.js',
    'ADBLOCK': True,
    'ADBLOCK_XPI': None,
    'ADBLOCK_CRX': None
}