from selenium import webdriver #import mmodules
import time

driver = webdriver.Chrome("/usr/local/bin/chromedriver") #file to chromedriver
driver.get("https://www.howdidwedough.com") #vocher website
#driver.maximize_window()

driver.find_element_by_id("NextButton").click()

time.sleep(3)
########################
driver.find_element_by_name("CN1").send_keys("3203")
driver.find_element_by_name("Index_VisitDateDatePicker").click()   
time.sleep(3)#input                                    #contineously presses continue
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
#driver.find_element_by_name("S000073").send_keys(email as str) #enters your email 
#driver.find_element_by_name("S000074").send_keys(email as str) #to send the voucher
driver.find_element_by_id("NextButton").click()
