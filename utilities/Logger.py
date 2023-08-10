import inspect
import logging


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\OrangeHRM Project\\Logs\\OrangeHrm.log")
        format = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

# class LogGenerator:
#     @staticmethod
#     def loggen():
#         name = inspect.stack()[1][3]
#         logger = logging.getLogger(name)
#         logfile = logging.FileHandler("C:\\Users\\Dreamer\\Documents\\pythonProject1\\pythonProject\\OrangeHRM Project\\Logs\\OrangeHrm.log")
#         format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
#         logfile.setFormatter(format)
#         logger.addHandler(logfile)
#         logger.setLevel(logging.INFO)
#         return logger

