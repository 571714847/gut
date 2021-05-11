#coding = utf-8
from selenium import webdriver
from time import sleep, ctime
import os

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/NacOS/Google Chrome"
chrome_driver_binary = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver.get("http: //www. baidu.com")
sleep(3)
driver.find_element_by_id("kw" ).send_keys("Test search")
driver.find_element_by_id("su").click()
sleep(3)
driver.quit()