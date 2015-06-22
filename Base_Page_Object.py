from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
	def __init__(self, selenium_browser, url ="http://dou.ua/"):
		self.url = url
		self.browser = selenium_browser

	def open(self):
		self.browser.get(self.url)

	def loadingWait(self, xp_el):
		WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, xp_el)))

if __name__ == '__main__':
	pytest.main()
