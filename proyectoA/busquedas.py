from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class objeto_busquedas():
    def __init__(self, myDriver):
        self.driver = myDriver

    #---------------------OBJETOS DE BUSQUEDA--------------------------------#

    def busqueda_por_name(self, namebox, texto):
        busqueda_box = self.driver.find_element_by_name(namebox).send_keys(texto, Keys.ENTER)
        self.driver.implicitly_wait(1)
    def busqueda_por_id(self, idbox, texto):
        busqueda_box = self.driver.find_element_by_id(idbox).send_keys(texto, Keys.ENTER)
        self.driver.implicitly_wait(1)
    def busqueda_por_xpath(self, xpathbox, texto):
        busqueda_box = self.driver.find_element_by_xpath(xpathbox).send_keys(texto, Keys.ENTER)
        self.driver.implicitly_wait(1)
    def busqueda_por_link_text(self, ltbox, texto):
        busqueda_box = self.driver.find_element_by_link_text(ltbox).send_keys(texto, Keys.ENTER)
        self.driver.implicitly_wait(1)
    def busqueda_por_partial_link_text(self, pltbox, texto):
        busqueda_box = self.driver.find_element_by_partial_link_text(pltbox).send_keys(texto, Keys.ENTER)
        self.driver.implicitly_wait(1)






