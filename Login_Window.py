from selenium import webdriver
import Base_Page_Object  
import Header_Bar


class LoginWindow(Base_Page_Object.Page):

	def __init__(self, selenium_browser):
		Base_Page_Object.Page.__init__(self, selenium_browser)
		#self.browser = browser

	def loginByMail(self, email, password):
		home = Header_Bar.HeaderBar(self.browser)
		home.loginButton()

		self.browser.find_element_by_xpath("//a[@id='_loginByMail']").click()
		self.browser.find_element_by_xpath("//input[@name='username']").send_keys(email)
		self.browser.find_element_by_xpath("//input[@name='password']").send_keys(password)
		self.browser.find_element_by_xpath("//button[@class='big-button btnSubmit']").click()


if __name__ == "__main__":
	pytest.main()
