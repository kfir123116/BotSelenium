import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:\\Users\\eitan\\Documents\\chromedriver.exe")

chromeOptions = Options()
chromeOptions.headless = False
driver = webdriver.Chrome(service=s, options=chromeOptions)
options = webdriver.ChromeOptions()
driver.maximize_window()

list_data = []


def delay():
    time.sleep(random.randint(1, 3))


def delay2():
    time.sleep(random.randint(0, 1))


def delay3():
    time.sleep(random.randint(1, 2))



def initialize_browser():
    driver.get("https://agendamentosonline.mne.gov.pt/AgendamentosOnline/app/scheduleAppointmentForm.jsf")
    print("Starting...")
    click = driver.find_element(by=By.ID, value="j_idt316")
    click.click()
    type1 = driver.find_element(by=By.ID, value="scheduleForm:tabViewId:ccnum")
    type1.send_keys("3")
    time.sleep(0.04)
    type1.send_keys("2")
    time.sleep(0.04)
    type1.send_keys("9")
    time.sleep(0.04)
    type1.send_keys("5")
    time.sleep(0.04)
    type1.send_keys("8")
    time.sleep(0.04)
    type1.send_keys("5")
    time.sleep(0.04)
    type1.send_keys("4")
    time.sleep(0.04)
    type1.send_keys("5")
    time.sleep(0.04)
    type1.send_keys("2")
    type2 = driver.find_element(by=By.ID, value="scheduleForm:tabViewId:dataNascimento_input")
    type2.send_keys("3")
    time.sleep(0.04)
    type2.send_keys("0")
    time.sleep(0.04)
    type2.send_keys("-")
    time.sleep(0.04)
    type2.send_keys("0")
    time.sleep(0.04)
    type2.send_keys("8")
    time.sleep(0.04)
    type2.send_keys("-")
    time.sleep(0.04)
    type2.send_keys("2")
    time.sleep(0.04)
    type2.send_keys("0")
    time.sleep(0.04)
    type2.send_keys("0")
    time.sleep(0.04)
    type2.send_keys("8")
    click1 = driver.find_element(by=By.ID, value="scheduleForm:tabViewId:searchIcon")
    click1.click()
    loop = True
    while loop:
        try:
            click2 = driver.find_element(by=By.ID, value="scheduleForm:postcons_label")
            click2.click()
            delay3()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click3 = driver.find_element(By.XPATH,
                                         "//li[@class='ui-selectonemenu-item ui-selectonemenu-list-item ui-corner-all']")
            click3.click()
            delay3()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click4 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:categato"]')
            click4.click()
            delay2()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click5 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:categato_panel"]/div/ul/li[3]')
            click5.click()
            delay3()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click4 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:comboBoxSN"]')
            click4.click()
            delay2()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click5 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:comboBoxSN_panel"]/div/ul/li[2]')
            click5.click()
            delay3()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click5 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:numAtosIguais"]')
            click5.click()
            delay3()
        except NoSuchElementException:
            pass
            continue
        break
    while loop:
        try:
            click5 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:numAtosIguais_panel"]/div/ul/li[3]')
            click5.click()
            time.sleep(4)
        except NoSuchElementException:
            pass
            continue
        break
    type3 = driver.find_element(by=By.ID, value="scheduleForm:name2")
    type3.send_keys("a")
    time.sleep(0.04)
    type3.send_keys("v")
    time.sleep(0.04)
    type3.send_keys("i")
    time.sleep(0.04)
    type3.send_keys("v")
    time.sleep(0.04)
    type3.send_keys(" ")
    time.sleep(0.04)
    type3.send_keys("e")
    time.sleep(0.04)
    type3.send_keys("l")
    time.sleep(0.04)
    type3.send_keys("y")
    time.sleep(0.04)
    type3.send_keys("a")
    time.sleep(0.04)
    type3.send_keys("h")
    time.sleep(0.04)
    type3.send_keys("u")
    type4 = driver.find_element(by=By.ID, value="scheduleForm:numDoc2")
    type4.send_keys("3")
    time.sleep(0.04)
    type4.send_keys("2")
    time.sleep(0.04)
    type4.send_keys("9")
    time.sleep(0.04)
    type4.send_keys("5")
    time.sleep(0.04)
    type4.send_keys("7")
    time.sleep(0.04)
    type4.send_keys("9")
    time.sleep(0.04)
    type4.send_keys("4")
    time.sleep(0.04)
    type4.send_keys("2")
    time.sleep(0.04)
    type4.send_keys("8")
    time.sleep(0.04)
    type5 = driver.find_element(by=By.ID, value="scheduleForm:birthdate2_input")
    type5.send_keys("2")
    time.sleep(0.04)
    type5.send_keys("9")
    time.sleep(0.04)
    type5.send_keys("-")
    time.sleep(0.04)
    type5.send_keys("0")
    time.sleep(0.04)
    type5.send_keys("3")
    time.sleep(0.04)
    type5.send_keys("-")
    time.sleep(0.04)
    type5.send_keys("2")
    time.sleep(0.04)
    type5.send_keys("0")
    time.sleep(0.04)
    type5.send_keys("1")
    time.sleep(0.04)
    type5.send_keys("5")
    type6 = driver.find_element(by=By.ID, value="scheduleForm:name3")
    type6.send_keys("s")
    time.sleep(0.04)
    type6.send_keys("h")
    time.sleep(0.04)
    type6.send_keys("i")
    time.sleep(0.04)
    type6.send_keys("r")
    time.sleep(0.04)
    type6.send_keys(" ")
    time.sleep(0.04)
    type6.send_keys("e")
    time.sleep(0.04)
    type6.send_keys("l")
    time.sleep(0.04)
    type6.send_keys("y")
    time.sleep(0.04)
    type6.send_keys("a")
    time.sleep(0.04)
    type6.send_keys("h")
    time.sleep(0.04)
    type6.send_keys("u")
    type7 = driver.find_element(by=By.ID, value="scheduleForm:numDoc3")
    type7.send_keys("3")
    time.sleep(0.04)
    type7.send_keys("2")
    time.sleep(0.04)
    type7.send_keys("9")
    time.sleep(0.04)
    type7.send_keys("5")
    time.sleep(0.04)
    type7.send_keys("8")
    time.sleep(0.04)
    type7.send_keys("5")
    time.sleep(0.04)
    type7.send_keys("2")
    time.sleep(0.04)
    type7.send_keys("8")
    time.sleep(0.04)
    type7.send_keys("2")
    type8 = driver.find_element(by=By.ID, value="scheduleForm:birthdate3_input")
    type8.send_keys("1")
    time.sleep(0.04)
    type8.send_keys("6")
    time.sleep(0.04)
    type8.send_keys("-")
    time.sleep(0.04)
    type8.send_keys("0")
    time.sleep(0.04)
    type8.send_keys("8")
    time.sleep(0.04)
    type8.send_keys("-")
    time.sleep(0.04)
    type8.send_keys("2")
    time.sleep(0.04)
    type8.send_keys("0")
    time.sleep(0.04)
    type8.send_keys("1")
    time.sleep(0.04)
    type8.send_keys("1")
    time.sleep(0.04)
    loop = True
    while loop:
        try:
            click6 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:bAddAto"]')
            click6.click()
            delay2()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click7 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:dataTableListaAtos:0:selCond"]')
            click7.click()
        except NoSuchElementException:
            pass
            continue
        break
    loop = True
    while loop:
        try:
            click8 = driver.find_element(By.XPATH, '//*[@id="scheduleForm:dataTableListaAtos:0:bCal"]')
            click8.click()
            delay()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="scheduleForm:j_idt174"]')
                                                                       )).click()
            click10 = driver.find_element(By.XPATH, '//*[@id="j_idt277"]')
            click10.click()
        except:
            continue


initialize_browser()

# driver.quit()
