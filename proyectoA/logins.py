from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class objeto_logins():
    def __init__(self, myDriver):
        self.driver = myDriver

    # --------------------OBJETOS LOGIN-----------------------------------------------#

        def login_por_id(self, iduser, idpass, username, password):
            usuario_box = self.driver.find_element_by_id(iduser).send_keys(username)
            contrasena_box = self.driver.find_element_by_id(idpass).send_keys(password)
            self.driver.implicitly_wait(1)

        def login_por_name(self, nameuser, namepass, username, password):
            usuario_box = self.driver.find_element_by_name(nameuser).send_keys(username)
            contrasena_box = self.driver.find_element_by_name(namepass).send_keys(password)
            self.driver.implicitly_wait(1)

        def login_por_xpath(self, xpathuser, xpathpass, username, password):
            usuario_box = self.driver.find_element_by_name(xpathuser).send_keys(username)
            contrasena_box = self.driver.find_element_by_name(xpathpass).send_keys(password)
            self.driver.implicitly_wait(1)

        def login_por_lt(self, ltuser, ltpass, username, password):
            usuario_box = self.driver.find_element_by_name(ltuser).send_keys(username)
            contrasena_box = self.driver.find_element_by_name(ltpass).send_keys(password)
            self.driver.implicitly_wait(1)

        def login_por_plt(self, pltuser, pltpass, username, password):
            usuario_box = self.driver.find_element_by_name(pltuser).send_keys(username)
            contrasena_box = self.driver.find_element_by_name(pltpass).send_keys(password)
            self.driver.implicitly_wait(1)
