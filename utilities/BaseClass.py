import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from tests.conftest import setup


@pytest.mark.usefixtures(setup)       ## fixture gets execute before and after function or class
# Fixture is special method which is attached with classes or methods to get execute before and after
# method or class
class BaseClass:

    def getLogger(self): #defined one method which has name getLogger
        loggerName = inspect.stack()[1][3] #Return a list of records for the stack
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log') #A handler class which writes formatted logging records to disk files
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self,locator,text):  # drop down selection
        sel = Select(locator)
        sel.select_by_visible_text(text)
