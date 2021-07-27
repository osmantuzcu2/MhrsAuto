from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import telegram_send
driver_path= "C:\\Users\\web\\Downloads\\chromedriver_win32\chromedriver.exe"
browser = webdriver.Chrome(driver_path)
browser.get("https://www.mhrs.gov.tr/vatandas/")
time.sleep(1)
tckimlik = browser.find_element_by_id("LoginForm_username")
print("*****************************")
print(tckimlik.value_of_css_property("padding"))
tckimlik.send_keys("1111111111")
time.sleep(1)
passw = browser.find_element_by_id("LoginForm_password")
passw.send_keys("1111111111")
login = browser.find_element_by_class_name("login-form-button")
login.click()
time.sleep(4)
rand = browser.find_element_by_class_name("hasta-randevu-card")
rand.click()
time.sleep(1)
genel = browser.find_element_by_class_name("genel-arama-button")
genel.click()


time.sleep(1)
il = browser.find_element_by_class_name("ant-select-selection")
il.click()

time.sleep(1)
ist = browser.find_element_by_class_name("ant-select-tree li:nth-child(2)")
ist.click()

""" time.sleep(1)
ilce = browser.find_element_by_class_name("ant-form div:nth-child(3)")
ilce.click()

time.sleep(1)
basak = browser.find_element_by_class_name("ant-select-dropdown-menu li:nth-child(7)")
basak.click() """  

time.sleep(1)
klinik = browser.find_element_by_class_name("ant-form div:nth-child(4)")
klinik.click()


time.sleep(1)
onk = browser.find_element_by_xpath('//*[@title="Tıbbi Onkoloji"]')
onk.click()


time.sleep(2)
btne = browser.find_elements_by_tag_name("button")
#btne = browser.find_element_by_class_name('ant-btn-primary')
btne[8].click()

time.sleep(1)
try:
    alert = browser.find_element_by_class_name("ant-modal")
    if alert.is_displayed():
        telegram_send.send(messages=["Randevu Yok "])
    else:
        telegram_send.send(messages=["Randevu Var "])
except:
    telegram_send.send(messages=["Randevu Var 1"])
    telegram_send.send(messages=["Randevu Var 2"])
    telegram_send.send(messages=["Randevu Var 3"])
