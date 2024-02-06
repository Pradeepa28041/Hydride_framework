import logging


class Loggin:

    @staticmethod
    def loggin():
        logging.basicConfig(filename=".\\Logs\\automation.log", format="%(pastime)s [%(levelness)s] - %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
