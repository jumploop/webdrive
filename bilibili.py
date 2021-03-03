#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait # 用于实例化一个Driver的显式等待
from selenium.webdriver.common.by import By # 内置定位器策略集
from selenium.webdriver.support import expected_conditions as EC # 内置预期条件函数，具体API请参考此小节后API链接

driver=webdriver.Chrome(executable_path='driver/chromedriver.exe')
driver.get('https://www.bilibili.com/v/game/esports/?spm_id_from=333.334.primary_menu.35#/9222')

try:
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'vd-list'))) #使用expected_conditions自带验证函数
    for doctorName in driver.find_elements_by_css_selector('.vd-list li'):
        print(doctorName.find_element_by_css_selector('.r > a').text)
finally:
    driver.close() # close the driver