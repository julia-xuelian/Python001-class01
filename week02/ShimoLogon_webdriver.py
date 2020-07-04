from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
     
    browser.get('https://shimo.im/welcome')
    time.sleep(1)

    btm1 = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    btm1.click()
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('13500600789')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('111111')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    time.sleep(1)

    cookies = browser.get_cookies() # 获取cookies
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()
    