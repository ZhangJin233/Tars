# from loguru import logger
from app import tars
import logbook
from .decorator import SingleDecorator

@SingleDecorator
class Log(object):
    handle = None
    def __init__(self,name='tars',filename=tars.config['LOG_NAME']):
        self.handle = logbook.FileHandler(filename,encoding='utf_8')
        logbook.set_datetime_format('local')
        self.logger = logbook.Logger(name)
        self.handle.push_application()

    def info(self,*args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def error(self,*args, **kwargs):
        return self.logger.error(*args, **kwargs)

    def warning(self,*args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def debug(self,*args, **kwargs):
        return self.logger.debug(*args, **kwargs)