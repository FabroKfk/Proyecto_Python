from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class objeto_clics():
    def __init__(self, myDriver):
        self.driver = myDriver

#---------------------OBJETOS CLIC---------------------------------------#

    def clic_por_name(self, namebutton):
        clic_btn = self.driver.find_element_by_name(namebutton).click()
        self.driver.implicitly_wait(1)
    def clic_por_id(self, idbutton):
        clic_btn = self.driver.find_element_by_id(idbutton).click()
        self.driver.implicitly_wait(1)
    def clic_por_xpath(self, xpathbutton):
        clic_btn = self.driver.find_element_by_xpath(xpathbutton).click()
        self.driver.implicitly_wait(1)
    def clic_por_link_text(self, ltbutton):
        clic_btn = self.driver.find_element_by_link_text(ltbutton).click()
        self.driver.implicitly_wait(1)
    def clic_por_partial_link_text(self, pltbutton):
        clic_btn = self.driver.find_element_by_partial_link_text(pltbutton).click()
        self.driver.implicitly_wait(1)