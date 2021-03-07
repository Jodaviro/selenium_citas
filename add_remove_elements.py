import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements (unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path='./chromedriver')
        driver=self.driver 
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver= self.driver
        elements_added= int (input('How many elements will you add?'))
        elements_removed= int (input('How many elements will you remove?'))
        total_elements= elements_added - elements_removed
        add_button=driver.find_element_by_xpath('//*[@id="content"]/div/button')
        sleep(3)
        for i in range (elements_added):
            add_button.click()
            
        for i in range (elements_removed):
            try:
                delete_button= driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
                delete_button.click()
            except:
                print('You are trying to delete more elements than the existense')
                break
            
        if total_elements > 0:
            print(f'There are {total_elements}')
        else:
            print ('There are 0 elements on screen')
        
        sleep (3)
            
        
    
if __name__=='__main__':
    unittest.main(verbosity=2)