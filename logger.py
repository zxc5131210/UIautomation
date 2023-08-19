"""Logger Class."""
import logging


LOGGING_LEVEL = logging.DEBUG
DATE_FORMAT = '%Y%m%d %H:%M:%S'
FORMAT ='%(asctime)s %(levelname)-2s %(message)s'

class Logger:
    """Logger Class."""
    def __init__(self) -> None:
        self.logger = logging
        self.logger.basicConfig(
            level=LOGGING_LEVEL,
            format=FORMAT,
            datefmt=DATE_FORMAT
        )

    def debug(self, msg: str) -> None:
        """Logging debug message."""
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        """Logging info message."""
        self.logger.info(msg)

    def warring(self, msg: str) -> None:
        """Logging warring message."""
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """Logging error message."""
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """Logging critical message."""
        self.logger.critical(msg)

if __name__ == '__main__':
    logger = Logger()
    logger.info('aaa')
    