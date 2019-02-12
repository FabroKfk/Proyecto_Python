from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class objeto_formularios():
    def __init__(self, myDriver):
        self.driver = myDriver

#-----------------------------OBJETOS DE FORMULARIO--------------------------#
    #Se utiliza para rellenar formularios. Puede elegir entre formulario de 1 a 5 campos.

    def formulario_name(self, cantidad, txtcmp1, txtcmp2, txtcmp3, txtcmp4, txtcmp5 ,campo1, campo2, campo3, campo4, campo5):
        if cantidad == 1:
            cmp1 = self.driver.find_element_by_name(campo1).send_keys(txtcmp1)
        if cantidad == 2:
            cmp1 = self.driver.find_element_by_name(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_name(campo2).send_keys(txtcmp2)
        if cantidad == 3:
            cmp1 = self.driver.find_element_by_name(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_name(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_name(campo3).send_keys(txtcmp3)
        if cantidad == 4:
            cmp1 = self.driver.find_element_by_name(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_name(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_name(campo3).send_keys(txtcmp3)
            cmp4 = self.driver.find_element_by_name(campo4).send_keys(txtcmp4)
        if cantidad == 5:
            cmp1 = self.driver.find_element_by_name(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_name(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_name(campo3).send_keys(txtcmp3)
            cmp4 = self.driver.find_element_by_name(campo4).send_keys(txtcmp4)
            cmp5 = self.driver.find_element_by_name(campo5).send_keys(txtcmp5)
        self.driver.implicitly_wait(1)

    def formulario_id(self, cantidad, txtcmp1, txtcmp2, txtcmp3, txtcmp4, txtcmp5, campo1, campo2, campo3, campo4, campo5):
        if cantidad == 3:
            cmp1 = self.driver.find_element_by_id(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_id(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_id(campo3).send_keys(txtcmp3)
        if cantidad == 4:
            cmp1 = self.driver.find_element_by_id(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_id(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_id(campo3).send_keys(txtcmp3)
            cmp4 = self.driver.find_element_by_id(campo4).send_keys(txtcmp4)
        if cantidad == 5:
            cmp1 = self.driver.find_element_by_id(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_id(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_id(campo3).send_keys(txtcmp3)
            cmp4 = self.driver.find_element_by_id(campo4).send_keys(txtcmp4)
            cmp5 = self.driver.find_element_by_id(campo5).send_keys(txtcmp5)
        self.driver.implicitly_wait(1)

    def formulario_xpath(self, cantidad, txtcmp1, txtcmp2, txtcmp3, txtcmp4, txtcmp5, campo1, campo2, campo3, campo4, campo5):
        if cantidad == 3:
            cmp1 = self.driver.find_element_by_xpath(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_xpath(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_xpath(campo3).send_keys(txtcmp3)
        if cantidad == 4:
            cmp1 = self.driver.find_element_by_xpath(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_xpath(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_xpath(campo3).send_keys(txtcmp3)
            cmp4 = self.driver.find_element_by_xpath(campo4).send_keys(txtcmp4)
        if cantidad == 5:
            cmp1 = self.driver.find_element_by_xpath(campo1).send_keys(txtcmp1)
            cmp2 = self.driver.find_element_by_xpath(campo2).send_keys(txtcmp2)
            cmp3 = self.driver.find_element_by_xpath(campo3).send_keys(txtcmp3)
            cmp4 = self.driver.find_element_by_xpath(campo4).send_keys(txtcmp4)
            cmp5 = self.driver.find_element_by_xpath(campo5).send_keys(txtcmp5)
        self.driver.implicitly_wait(1)
