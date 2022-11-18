from selenium import webdriver
import logging as log

driver = webdriver.Chrome()
driver.get("https://ithelp.ithome.com.tw/articles/10230426")
driver.quit()