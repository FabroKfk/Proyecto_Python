from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class objeto_selecciones():
    def __init__(self, myDriver):
        self.driver = myDriver

#---------------------OBJETOS SELECCIONAR POR VALUE--------------------------------#

    def seleccionar_id(self, idlista, valor):
        seleccionar_list = Select(self.driver.find_element_by_id(idlista)).select_by_value(valor)
        self.driver.implicitly_wait(1)
    def seleccionar_name(self,namelista, valor):
        seleccionar_list = Select(self.driver.find_element_by_name(namelista)).select_by_value(valor)
        self.driver.implicitly_wait(1)
    def seleccionar_xpath(self,xpathlista, valor):
        seleccionar_list = Select(self.driver.find_element_by_xpath(xpathlista)).select_by_value(valor)
        self.driver.implicitly_wait(1)
    def seleccionar_link_text(self,ltlista, valor):
        seleccionar_list = Select(self.driver.find_element_by_link_text(ltlista)).select_by_value(valor)
        self.driver.implicitly_wait(1)
    def seleccionar_partial_link_text(self,pltlista, valor):
        seleccionar_list = Select(self.driver.find_element_by_partial_link_text(pltlista)).select_by_value(valor)
        self.driver.implicitly_wait(1)