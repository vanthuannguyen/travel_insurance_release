# -*- coding: utf-8 -*-
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from logging import getLogger

logger = getLogger(__name__)

driverLocation = 'C:\\Python27\\chromedriver.exe'
os.environ['webdriver.chrome.driver'] = driverLocation
home_page = 'https://www.gobear.com/ph?x_session_type=UAT'

class Travel_application():

    def goto_result_page(self, url):
        '''
        Arguments:
            1. url: link to travel insurance homepage
        '''
        logger.info('Test start here')
        #Init a chrome session
        driver = webdriver.Chrome(driverLocation)

        # Create an explicit wait handler with wait time is 10 seconds and frequency check is 1 second
        wait = WebDriverWait(driver, 10, poll_frequency=1)
        # Maximize current browser window
        driver.maximize_window()
        # Access to homepage
        driver.get(url)

        # Wait until homepage is loaded and button ĐĂNG NHẬP NGAY is clickable
        insurance_tab = wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@href='#Insurance' and @aria-controls='Insurance']")))
        # Click tab Insurance
        insurance_tab.click()

        # Wait until insurance form is loaded, then click Travel tab
        travel_tab = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='#Travel' and @aria-controls='Travel']")))
        travel_tab.click()

        # Wait until Show my results is clickable
        show_result_bt = wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@name='product-form-submit']")))
        show_result_bt.click()
        time.sleep(3)

        collepseFilter_btn = wait.until(ec.visibility_of_element_located((By.XPATH, "//h5[@id='collapseFilterBtn']")))
        collepseFilter_btn.click()
        try:
            expanded_element = wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@id='collapseFilter' and @aria-expanded='false']")))
        except Exception as e:
            print ('Test expanded Filter failed')
            print ('Exception: {}'.format(e))

        if expanded_element:
            print ('Test expanded Filter pass')
        else:
            print ('Test expanded Filter failed')

        # Expand Filter form
        collepseFilter_btn.click()
        time.sleep(1)

        # Test radio button
        promos_only = driver.find_element_by_xpath("//div[@data-filter-name='Promos Only']")
        promos_only.click()
        promos_only_radio = driver.find_element_by_xpath("//div[@data-filter-name='Promos Only']/input[@type='radio' and @class='gb-radio__original']")
        time.sleep(1)
        if promos_only_radio.is_selected():
            print ('Test Promotion pass')
        else:
            print ('Test Promotion failed')

        # Test checkbox
        insurers_pacific_cross = driver.find_element_by_xpath("//div[@data-filter-name='Pacific Cross']")
        insurers_pacific_cross.click()
        pacific_cross_checkbox = driver.find_element_by_xpath("//div[@data-filter-name='Pacific Cross']/input[@type='checkbox' and @class='gb-checkbox__original']")
        time.sleep(1)
        if pacific_cross_checkbox.is_selected():
            print ('Test Insurers pass')
        else:
            print ('Test Insurers failed')

travel = Travel_application()
travel.goto_result_page(home_page)