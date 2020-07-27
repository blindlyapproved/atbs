from selenium import webdriver

browser = webdriver.Firefox()

browser.get("https://automatetheboringstuff.com/")

elem = browser.find_element_by_css_selector(".main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)")
elem.click()

elems = browser.find_elements_by_css_selector("p")

len(elems)

browser.quit()