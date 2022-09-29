
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData  ## impoting classes from our projet folders
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):      ## inheritance
    # Here we have derived the BaseClass(parentclass) into TestHomePage(Child class) that means all properties
    # from BaseClass will comes into TestHomePage class.
    '''
        TestHomePage => Child class
        BaseClass => Parent class
        inheritance # we are inheriting BaseClass into TestHomePage
        So all the properties of base class will be available to child
        All properties or methods will be inherited in child
    '''

    def test_formSubmission(self, getData): #created variable getData
        log = self.getLogger() #creating logger object to maintain or write logs.
        # getLogger method present in baseclass
        # self.driver we will get from setup fixture which is been used by parent BaseClass
        homepage = HomePage(self.driver)     ## Creating object of homePage and passing driver in parameterized contructor
                   #HomePage class present in pageObjects-->HomePage.py
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=[{"firstname": "Sagar", "lastname":"Sarade", "gender": "Male"},
                            {"firstname": "Yusuf", "lastname":"Tamboli", "gender": "Male"},
                            {"firstname": "Akshay", "lastname":"Nikam", "gender": "Male"}])

    ###@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):     #request is default object of fixture which automatically initilized when fixture is being executed
        return request.param


