import time
from selenium import webdriver

# from selenium.webdriver.opera.options import Options
URL1 = 'course url'
URL2 = 'course url'
driver = webdriver.Opera()
driver.get(URL1)

fname='grades.csv'
f = open(fname, 'a', encoding='utf-8')

userbox = driver.find_element_by_xpath('//*[@id="userNameInput"]')
userbox.send_keys('god@university.ca')

passbox = driver.find_element_by_xpath('//*[@id="passwordInput"]')
passbox.send_keys('abcd123')

loginLink = driver.find_element_by_xpath('//*[@id="submitButton"]')
loginLink.click()

# driver.implicitly_wait(1)
time.sleep(5)
driver.get(URL2)
perc = driver.find_element_by_xpath('//*[@id="z_a"]/tbody/tr[3]/td[4]/div/div')
perce = perc.text
print (perce)

if len(perce) > 99:
    print ('you received max grade')

perct = driver.find_element_by_xpath('//*[@id="d_content_inner"]')
percet = perct.text
print (percet)

f.write(percet)