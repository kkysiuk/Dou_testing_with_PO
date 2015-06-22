from selenium import webdriver
import Base_Page_Object  
import Header_Bar


class ProfilePage(Base_Page_Object.Page):

	def __init__(self, selenium_browser):
		Base_Page_Object.Page.__init__(self, selenium_browser)
		#self.browser = browser

	def profileLogOut(self):
		profile = Header_Bar.HeaderBar(self.browser)
		profile.profileButton()
		xp_logoutButton = "//a[@href='http://dou.ua/logout/']"
		self.loadingWait(xp_logoutButton)
		self.browser.find_element_by_xpath(xp_logoutButton).click()

		
if __name__ == "__main__":
	pytest.main()
