from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

name = ["고예준","송민규","김기범","문세혁","양성준","이동근"]
birth =["030302","030920","030312","030929","030424","030609"]

for i in range(0,len(name),1):

    driver = webdriver.Chrome()
    driver.get('https://eduro.jje.go.kr/stv_cvd_co00_002.do')

    driver.find_element_by_id("pName").send_keys(name[i])
    time.sleep(1)
    driver.find_element_by_id("frnoRidno").send_keys(birth[i])
    time.sleep(1)
    driver.find_element_by_id("schulNm").send_keys("제주과학고등학교")
    driver.find_element_by_xpath('//*[@id="btnSrchSchul"]').click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    time.sleep(1)
    driver.find_element_by_id("rspns011").click()
    driver.find_element_by_id("rspns02").click()
    driver.find_element_by_id("rspns070").click()
    driver.find_element_by_id("rspns080").click()
    driver.find_element_by_id("rspns090").click()
    driver.find_element_by_id("btnConfirm").click()
    time.sleep(5)
    driver.close()
