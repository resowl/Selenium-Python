import inspect
import logging


class utils:

    def custom_logger(log_level=logging.DEBUG):
        """
        Logs messages from where the method is called
        Parameters:
            log_level(int): Threshold for the logger to level
        Returns:
            Logger instance
        """
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("automation.log", mode="a")
        file_handler.setLevel(log_level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s: %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger