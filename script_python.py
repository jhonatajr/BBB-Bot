from selenium import webdriver
import time
        
counter = 0

while True:
  #browser = webdriver.Chrome()
  browser = webdriver.Chrome(executable_path='C:/Users/jhona/AppData/Local/Temp/Rar$EXa7912.16132/chromedriver.exe')
  browser.maximize_window()
  browser.get("https://login.globo.com/login/1")
 
  login = browser.find_elements_by_tag_name("input")
  login[0].clear()
  login[0].send_keys("vekev94168@fft-mail.com");
  login[1].send_keys("298f1cb4");
  find_entrar = browser.find_elements_by_tag_name("button")
  find_entrar[1].click()
  
  browser.get(
      'https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml')
  time.sleep(1)

  #find_manu = browser.find_elements_by_class_name("_26xt8IFJvrVPx2mFcbAHt")

  
  find_manu = browser.find_elements_by_class_name("_3zoZLSrLE8cbp9qgGV3Yjl")
  find_manu[1].click()

  time.sleep(1)

  bandeira = 0 
  while bandeira == 0: 
    try:
        find_captcha =  browser.find_element_by_class_name("gc__3_EfD")
        find_captcha.click()
    except:
        browser.close()
        counter = counter + 1
        print(counter)
        bandeira = 1
        time.sleep(1)
  time.sleep(5)