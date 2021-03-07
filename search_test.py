import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld (unittest.TestCase):
    
    
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()   
        #driver.implicitly_wait(15)    
    
    def test_search_text_field (self):
        search_field = self.driver.find_element_by_id('search')
        
    def test_search_text_field_by_name(self):
        self.driver.find_element_by_name ('q')
        
    def test_search_text_field_class_name(self):
        self.driver.find_element_by_class_name('input-text')
        
    def test_search_botton_enabled(self):
        button= self.driver.find_element_by_class_name('button')
        
    def test_count_of_promo_banner_images(self):
        banner_list=self.driver.find_element_by_class_name ('promos')
        banners= banner_list.find_elements_by_tag_name ('img')
        self.assertEqual(3, len(banners))
        
    def test_vip_promo(self):
        vip_promo= self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/ul/li[1]/a/img')
    
    def test_shopping_car (self):
        shoppping_car_icon= self.driver.find_elements_by_css_selector('div.header-minicart span.icon')
    
    def tearDown(self):
        self.driver.quit()
    
if __name__=='__main__':
    unittest.main(verbosity=2)#, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))