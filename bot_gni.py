from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os, time

from selenium.webdriver.common.action_chains import ActionChains

contas = [
   'sua conta',
] #lista dos nomes dos usuarios
senha = 'sua senha' #Senha dos usuarios (importante que seja a mesma para todos)
cont = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.ganharnoinsta.com/painel/?pagina=logout')

time.sleep(3)

#Start Login GNI
email_element = driver.find_element_by_xpath("//input[@name='email']")
email_element.clear()
email_element.send_keys('seu email')

time.sleep(1)

pass_element = driver.find_element_by_xpath("//input[@name='senha']")
pass_element.clear()
pass_element.send_keys('sua senha da plataforma')

time.sleep(1)

pass_element.send_keys(Keys.RETURN)
#End Login

for username in contas:
    time.sleep(4)
    
    #acessar pagina de adicionar conta
    driver.get('https://www.ganharnoinsta.com/painel/?pagina=adicionar_conta')

    time.sleep(3)
    
    button = driver.find_element_by_xpath("//input[@value='instagram']")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(button).click(button).perform()
    
    time.sleep(2)
    #confirmar
    driver.find_element_by_xpath("//button[@class='btn btn-block btn-success']").click()

    time.sleep(3)
    #nome do usuario
    user_element = driver.find_element_by_xpath("//input[@name='nome_usuario']")
    user_element.clear()
    user_element.send_keys(username)

    time.sleep(2)
    #genero
    driver.find_element_by_xpath("//select[@name='sexo']/option[text()='Feminino']").click()
    
    time.sleep(2)
    #estado
    driver.find_element_by_xpath("//select[@name='estado']/option[text()='Rio de Janeiro']").click()

    time.sleep(2)
    #confirmar 
    driver.find_element_by_xpath("//button[@class='btn btn-block btn-success']").click()
    
    time.sleep(2)
    #copiar codigo
    driver.find_element_by_xpath("//button[@class='btn btn-warning']").click()

    time.sleep(2)
    #abrir instagram
    driverInsta = webdriver.Chrome(ChromeDriverManager().install())
    driverInsta.get('https://www.instagram.com/')

    time.sleep(4)

    #Start Login
    user_element = driverInsta.find_element_by_xpath("//input[@name='username']")
    user_element.clear()
    user_element.send_keys(username)
    
    time.sleep(1)

    pass_element = driverInsta.find_element_by_xpath("//input[@name='password']")
    pass_element.clear()
    pass_element.send_keys(senha)

    time.sleep(1)
    
    pass_element.send_keys(Keys.RETURN)
    #End Login

    time.sleep(4)
    driverInsta.get('https://www.instagram.com/accounts/edit/')

    time.sleep(2)
    #adicionar codigo
    bio_element = driverInsta.find_element_by_xpath("//textarea[@class='p7vTm']")
    bio_value = driverInsta.find_element_by_xpath("//textarea[@class='p7vTm']").get_attribute('value')
    
    bio_element.send_keys(Keys.ENTER)

    bio_element.send_keys(Keys.CONTROL, "v")

    time.sleep(1)
    driverInsta.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()

    time.sleep(2)

    #validar conta s
    driver.find_element_by_xpath("//button[@class='btn btn-block btn-success']").click()
    
    time.sleep(7)

    bio_element.send_keys(Keys.CONTROL, "a")
    bio_element.send_keys(bio_value)

    time.sleep(1)
    driverInsta.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()

    time.sleep(3)
    #fecha instagram
    driverInsta.quit()
    
    time.sleep(4)
    print(f'{cont} - O perfil {username} foi adicionado.')

driver.quit() #Fecha o navegador