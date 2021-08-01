from selenium import webdriver
from time import sleep

chrome_driver_path = 'C:/Chrome Driver/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://www.amazon.ca/Instant-Pot-DUONOVA60-Pressure-Cooker/dp/B07RCNHTLS/ref=sr_1_2?dchild=1&keywords=instant+pot&qid=1627837299&s=kitchen&sr=1-2')
price = driver.find_element_by_id("priceblock_ourprice")

print(price.text)

sleep(2)
driver.quit() 
