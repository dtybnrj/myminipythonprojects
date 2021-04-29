# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:35:29 2019

@author: adity
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(r'C:\Users\adity\Downloads\Compressed\chromedriver')
wait=WebDriverWait(driver,600)
driver.get('http://web.whatsapp.com')
target='""'
string='message sent using pyhton'
x_args='//span[contains(@title,'+target+')]'
target=wait.until(EC.presence_of_element_located((By.XPATH,x_args)))
target.click()
input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(50):
    input_box.send_keys(string+Keys.ENTER)