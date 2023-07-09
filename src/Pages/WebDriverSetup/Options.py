class ArgumentOptions:
    
    START_MAXIMIZED = "--start-maximized"
    IGNORE_SSL_ERRORS = '--ignore-ssl-errors'
    IGNORE_CERTIFICATE_ERRORS = '--ignore-certificate-errors'
    PROXY_SERVER = '--proxy-server={}'
    HEADLESS = '--headless'
    UNDETECTED_CONTROL = "--disable-blink-features=AutomationControlled"
    USER_AGENT = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    

class ExperimentalOptions:
    
    EXCLUDE_SWITCHES = 'excludeSwitches'
    USE_AUTOMATION_EXT = "useAutomationExtension"
    
    ENABLE_LOGGING = ['enable-logging']
    ENALE_AUTOMATION = ["enable-automation"]
    