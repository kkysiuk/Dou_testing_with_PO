from selenium import webdriver
import Base_Page_Object  

class HeaderBar(Base_Page_Object.Page):
	xp_header = "//header[@class='b-head']"
	
	def __init__(self, selenium_browser):
		Base_Page_Object.Page.__init__(self, selenium_browser)
		#self.browser = browser

	def loginButton(self):
		xp_loginButton = "//a[@id='login-link']"
		self.loadingWait(xp_loginButton)
		self.browser.find_element_by_xpath(xp_loginButton).click()

	def mainPageButton(self):
		xp_mainPageButton = self.xp_header + "ul/li/a[@class='sel']"
		self.loadingWait(xp_mainPageButton)		
		self.browser.find_element_by_xpath(xp_mainPageButton).click()

	def forumsButton(self):
		xp_forumsButton = self.xp_header + "/ul/li/a[@href='http://dou.ua/forums/']"
		self.loadingWait(xp_forumsButton)		
		self.browser.find_element_by_xpath(xp_forumsButton).click()

	def lentaButton(self):
		xp_lentaButton = self.xp_header + "/ul/li/a[@href='http://dou.ua/lenta/']"
		self.loadingWait(xp_lentaButton)		
		self.browser.find_element_by_xpath(xp_lentaButton).click()

	def salariesButton(self):	
		xp_salariesButton = self.xp_header + "/ul/li/a[@href='http://jobs.dou.ua/salaries/']"
		self.loadingWait(xp_salariesButton)		
		self.browser.find_element_by_xpath(xp_salariesButton).click()

	def jobsButton(self):
		xp_jobsButton = self.xp_header + "/ul/li/a[@href='http://jobs.dou.ua/']"
		self.loadingWait(xp_jobsButton)		
		self.browser.find_element_by_xpath(xp_jobsButton).click()

	def calendarButton(self):
		xp_calendarButton = self.xp_header + "/ul/li/a[@href='http://dou.ua/calendar/']"
		self.loadingWait(xp_calendarButton)		
		self.browser.find_element_by_xpath(xp_calendarButton).click()

	def profileButton(self):
		xp_profileButton = self.xp_header + "//img[@class='g-avatar']"
		#xp_profileButton = xp_header + "/div[@class='right-part']/a[@class='min-profile']/img[@class='g-avatar']"
		self.loadingWait(xp_profileButton)
		el = self.browser.find_element_by_xpath(xp_profileButton)
		assert el is not None
		el.click()


if __name__ == "__main__":
	pytest.main()
