import unittest
from selenium import webdriver
from time import sleep

class TestingMercadolibre(unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver
        driver.implicitly_wait(30) 
        driver.maximize_window()   
        driver.get('https://www.mercadolibre.com/')
   
    def test_search_ps5(self):
        driver=self.driver
        country= driver.find_element_by_id('EC')
        country.click()
        sleep(2)
        search_field= driver.find_element_by_name('as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('ps5')
        search_field.submit()
        sleep(2)
        location= driver.find_element_by_partial_link_text('Pichincha ( Quito )')
        location.click()
        sleep(2)
        condition = driver.find_element_by_partial_link_text('Nuevo')
        condition.click()
        sleep(2)
        order_menu= driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        higher_price= driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[3]')
        higher_price.click()
        sleep(2)
        articles=[]
        prices= []
        for i in range(5):
            article_name= driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price=driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div/div/div/span[1]/span[2]').text 
            prices.append(article_price)
        
        print(articles,prices) 

    
    def tearDown(self):
        self.driver.close()
        
if __name__=='__main__':
    unittest.main(verbosity=2)        