
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class objeto_vaciar():
    def __init__(self, myDriver):
        self.driver = myDriver

    # -------------------------LIMPIAR CAMPO-------------------------------#

    def limpiar_campo_name(self, namebox):
        busqueda_box = self.driver.find_element_by_name(namebox).clear()
        self.driver.implicitly_wait(1)


    def limpiar_campo_id(self, idbox):
        busqueda_box = self.driver.find_element_by_id(idbox).clear()
        self.driver.implicitly_wait(1)


    def limpiar_campo_xpath(self, xpathbox):
        busqueda_box = self.driver.find_element_by_xpath(xpathbox).clear()
        self.driver.implicitly_wait(1)


    def limpiar_campo_link_text(self, ltbox):
        busqueda_box = self.driver.find_element_by_link_text(ltbox).clear()
        self.driver.implicitly_wait(1)


    def limpiar_campo_partial_link_text(self, pltbox):
        busqueda_box = self.driver.find_element_by_partial_link_text(pltbox).clear()
        self.driver.implicitly_wait(1)
