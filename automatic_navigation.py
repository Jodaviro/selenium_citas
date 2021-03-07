import unittest
from selenium import webdriver

class NavigationTest (unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.implicitly_wait(30) 
        driver.maximize_window()   
        driver.get('https://google.com/')

    def test_browser_navigation(self):
        driver= self.driver
        search_field= driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        search_field.submit()
        driver.back()
        driver.forward()
        driver.refresh()
                
    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()
    
if __name__=='__main__':
    unittest.main(verbosity=2)