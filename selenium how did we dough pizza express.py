from selenium import webdriver
import time

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.howdidwedough.com")
#driver.maximize_window()

driver.find_element_by_id("NextButton").click()

time.sleep(3)
########################
driver.find_element_by_name("CN1").send_keys("3203")
driver.find_element_by_name("Index_VisitDateDatePicker").click()
time.sleep(3)#input
driver.find_element_by_name("InputMinute").send_keys("03")
driver.find_element_by_name("InputHour").send_keys("03")
driver.find_element_by_name("AmountSpent1").send_keys("50")
driver.find_element_by_name("AmountSpent2").send_keys("30")
driver.find_element_by_name("NextButton").click()
########################
driver.find_element_by_class_name("radioBranded").click()
driver.find_element_by_id("NextButton").click()
######
time.sleep(3)
driver.find_element_by_class_name("radioBranded").click()
driver.find_element_by_id("NextButton").click()
#####
driver.find_element_by_class_name("radioBranded").click()
driver.find_element_by_id("NextButton").click()
####
for  i in range(5):
    driver.find_element_by_id("NextButton").click()
    time.sleep(3)
    driver.find_element_by_id("NextButton").click()

####
driver.find_element_by_id("NextButton").click()
time.sleep(3)
####
driver.find_element_by_class_name("radioBranded").click()
driver.find_element_by_id("NextButton").click()
####
for i in range(3):
    driver.find_element_by_id("NextButton").click()
    time.sleep(3)
    driver.find_element_by_id("NextButton").click()

####
driver.find_element_by_id("NextButton").click()

#####
print (1)
time.sleep(3)
driver.find_element_by_class_name("radioBranded").click()
driver.find_element_by_id("NextButton").click()
#####
print(2)
time.sleep(3)
driver.find_element_by_class_name("radioBranded").click()
driver.find_element_by_id("NextButton").click()
#######
#driver.find_element_by_id("NextButton").click()
print(3)
time.sleep(3)
driver.find_element_by_id("NextButton").click()
driver.find_element_by_name("S000073").send_keys(email as str)
driver.find_element_by_name("S000074").send_keys(email as str)
driver.find_element_by_id("NextButton").click()
