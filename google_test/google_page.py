import unittest
from selenium import webdriver
from test_google import GooglePage 

class Googletest(unittest. TestCase):

    @classmethod
    def setUpClass (cls):
        cls.driver=webdriver.Chrome(executable_path='../chromedriver')
        
    def test_search(self):
        google= GooglePage(self.driver)
        google.open()
        google.search('Platzi') 
        self.assertEqual('Platzi', google.keyword)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__=='__main__':
    unittest.main(verbosity=2)    