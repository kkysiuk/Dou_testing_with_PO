from selenium import webdriver
import pytest

import Header_Bar
import Login_Window
import Profile_Page
import Test_Data
 

@pytest.fixture
def browser(request):
	browser = webdriver.Firefox()
	request.addfinalizer(browser.close)
	return browser

def test_Login(browser):
	
	login = Login_Window.LoginWindow(browser)
	
	login.open()
	login.loginByMail(Test_Data.mail, Test_Data.password)
	
	testprofile = Profile_Page.ProfilePage(browser)
	testprofile.profileLogOut()	
	print "Log In on Main Page is seccessfull" 
	menu = Header_Bar.HeaderBar(browser)

def test_Forum(browser):
	
	forum = Header_Bar.HeaderBar(browser)
	
	forum.open()
	forum.forumsButton()

	login = Login_Window.LoginWindow(browser)
	login.loginByMail(Test_Data.mail, Test_Data.password)

	testprofile = Profile_Page.ProfilePage(browser)
	testprofile.profileLogOut()
	print "Log In on Forum Page is seccessfull" 



if __name__ == "__main__":
	pytest.main()
