from selenium import webdriver

# from selenium.webdriver.opera.options import Options
URL1 = 'url1'
URL2 = 'url2'
driver = webdriver.Opera()
driver.get(URL1)

userbox = driver.find_element_by_xpath('//*[@id="userNameInput"]')
userbox.send_keys('god@universitymail.ca')

passbox = driver.find_element_by_xpath('//*[@id="passwordInput"]')
passbox.send_keys('abc123')

loginLink = driver.find_element_by_xpath('//*[@id="submitButton"]')
loginLink.click()

# driver.implicitly_wait(1)

driver.get(URL2)
loginLink = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div/div/a[2]')
loginLink.click()

res = 1

while res < 15:
    owl = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div/div/a[2]')
    owl.click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div/div/a[2]').click()
    res = res + 1