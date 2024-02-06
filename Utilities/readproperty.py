import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\application_settings.ini")


class Readconfig:
    @staticmethod
    def get_mobile_no() -> object:
        number = config.get('comon info', 'mobile_no')
        return number

    @staticmethod
    def get_otp():
        otp = config.get('comon info', 'otp_no')
        return otp

    @staticmethod
    def getapplication_title():
        app_title = config.get('comon info', 'title')
        return app_title

    @staticmethod
    def getapplication_URL():
        url = config.get('comon info', 'url')
        return url
