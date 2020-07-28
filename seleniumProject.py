from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver= webdriver.Firefox()
driver.get('https://www.wikipedia.org/')

element= driver.find_element_by_id('js-link-box-en')

print(element.text)
print(element.get_attribute('href'))
element.click()
#show other driver.find methods


driver.find_element_by_id('searchInput').click()
driver.find_element_by_id('searchInput').send_keys('discworld')
driver.find_element_by_id('searchInput').send_keys(Keys.ENTER)


