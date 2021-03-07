import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class CitaAsilo(unittest.TestCase):
    
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path='./chromedriver')
        driver= self.driver
        driver.implicitly_wait(30) 
        driver.maximize_window()   
        driver.get('https://sede.administracionespublicas.gob.es/icpco/acOpcDirect')
   
    def test_search_cita(self):
        driver= self.driver
        cockie_kill= driver.find_element_by_id('cookie_action_close_header')
        cockie_kill.click()
        first_button= driver.find_element_by_id('btnSubmit')
        first_button.click()
        #sleep(1)
        location_select=driver.find_element_by_id('form')
        location_select.click()
        driver=self.driver
        malaga= driver.find_element_by_xpath('//*[@id="form"]/option[35]')
        malaga.click()
        #sleep(1)
        submit_one= driver.find_element_by_id('btnAceptar')
        submit_one.click()
        #sleep(1)
        tramites_group=driver.find_element_by_id('tramiteGrupo[0]')
        #tramites_group.click()
        tramite_asilo= driver.find_element_by_xpath('//*[@id="tramiteGrupo[0]"]/option[7]')
        tramite_asilo.click()
        sleep(1)
        
        action= ActionChains(driver)
        submit_two= driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div[2]/form[1]/div[4]/input[1]')
        action.move_to_element(submit_two)
        action.click(submit_two)
        action.perform()
        sleep(1)
        enter_button= driver.find_element_by_id('btnEntrar')
        enter_button.click()
        
        passport_selection= driver.find_element_by_id('rdbTipoDocPas')
        passport_selection.click()
        passport_input= driver.find_element_by_id('txtIdCitado')
        passport_input.click()
        passport_input.send_keys('093098487')
        sleep(1)
        
        action= ActionChains(driver)
        name_input= driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div[2]/form/div/div/div[1]/div[3]/div/div/div/div/input[1]')
        action.move_to_element(name_input).click(name_input).perform()
        name_input.send_keys('JOSE VILLALOBOS')
        
        action= ActionChains(driver)
        birthday_input= driver.find_element_by_id('txtAnnoCitado')
        action.move_to_element(birthday_input)
        action.click(birthday_input).perform()
        birthday_input.send_keys('1988')
        
        action= ActionChains(driver)
        nationality= driver.find_element_by_id('txtPaisNac')
        action.move_to_element(nationality)
        action.click(nationality).perform()
        venezuelan= driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div/div/div[1]/div[5]/div/div/div/div/span/select/option[199]')
        venezuelan.click()
        
        action= ActionChains(driver)
        submit_three= driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/div/section/div[2]/form/div/div/div[2]/input[1]')
        action.move_to_element(submit_three)
        action.click(submit_three).perform()
        sleep(1)
        
        cita= driver.find_element_by_xpath('/html/body/div[1]/div/main/div/div/section/div[2]/form/div/div/div[3]/input[1]')
        cita.click()
        sleep(999)   
    def tearDown(self):
        self.driver.close()
        
if __name__=='__main__':
    unittest.main(verbosity=2)   
