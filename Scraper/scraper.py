from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from datetime import datetime

range_low = '35078000'
range_high = '35080000'
start_date = '01/07/2020'
end_date = '29/07/2020'
path = 'https://www.hacienda.go.cr/tica/web/hcitrncm1.aspx'

##########################################
### Opening Brower and Desired Website ###
##########################################

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(path)

#############################################
### Grabbing Captcha and Obtaining Answer ###
#############################################

img_src = driver.find_element_by_xpath('//div[@id="captchaImage"]/img')
img_src = img_src.get_attribute('src')
captcha_number = int(img_src.split('/')[-1].split('.')[0])
captchas = pd.read_csv('../Captchas/captchas.csv', index_col=0)
captcha_value = captchas.iloc[captcha_number - 1]

#########################
### Filling Form Data ###
#########################

driver.find_element_by_xpath(
    '//select[@id="vVADUANA"]/option[@value="X"]'
    ).click()

time.sleep(1)
date_i = driver.find_element_by_xpath('//div[@id="vVFCHIN_dp_container"]/input')
date_i.clear()
date_i.send_keys(start_date)

time.sleep(3)
date_f = driver.find_element_by_xpath('//div[@id="vVFCHFN_dp_container"]/input')
date_f.clear()
date_f.send_keys(end_date)

time.sleep(3)
range_start = driver.find_element_by_xpath('//td/input[@id="vVNCMINI"]')
range_start.clear()
range_start.send_keys(range_low)

time.sleep(1)
range_end = driver.find_element_by_xpath('//td/input[@id="vVNCMFIN"]')
range_end.clear()
range_end.send_keys(range_high)

time.sleep(1)
captcha_field = driver.find_element_by_xpath('//input[@id="_cfield"]')
captcha_field.clear()
captcha_field.send_keys(captcha_value)

time.sleep(1)
driver.find_element_by_xpath('//input[@name="BUTTON1"]').click()
