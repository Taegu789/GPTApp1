from selenium import webdriver

# Create a webdriver instance
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("http://www.naver.com")

# Wait for the page to load
driver.implicitly_wait(10)

# Extract the page source
page_source = driver.page_source

# Find an element with the ID "submit-button" and click it
driver.find_element_by_id("#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(8) > a").click()

# Print the page source
print(page_source)

# Close the webdriver
driver.close()