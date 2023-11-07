from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the web driver (you need to download and specify the driver executable path)
driver = webdriver.Chrome()#executable_path='C:/Users/kgrna/Downloads/chromedriver_win32')

# Navigate to the website
url = 'https://www.amazon.ca/s?k=shoes&crid=281KNZUNV7ISO&sprefix=shoes%2Caps%2C228&ref=nb_sb_noss_1'
driver.get(url)

# Create a list to store the scraped shoe data
shoe_data = []

# Define a function to extract the shoe data
def scrape_shoe_data():
    # product_name = driver.find_element(By.XPATH, '//*[@class="product-name"]').text
    # description = driver.find_element(By.XPATH, '//*[@class="product-description"]').text
    # price = driver.find_element(By.XPATH, '//*[@class="product-price"]').text
    product_details = driver.find_element(By.XPATH, '//*[@class="Product Details"]').text


    # Assuming color and size information are in dropdown menus
    color_element = driver.find_element(By.XPATH, '//*[@id="color-dropdown"]')
    color_options = color_element.find_elements(By.TAG_NAME, 'option')
    colors = [option.text for option in color_options if option.text.strip()]

    size_element = driver.find_element(By.XPATH, '//*[@id="size-dropdown"]')
    size_options = size_element.find_elements(By.TAG_NAME, 'option')
    sizes = [option.text for option in size_options if option.text.strip()]

    shoe_info = {
        'Product Details': product_details
        # 'Product Name': product_name,
        # 'Description': description,
        # 'Price': price,
        # 'Colors': colors,
        # 'Sizes': sizes
    }

    shoe_data.append(shoe_info)

# Loop through the pages and scrape data
while True:
    scrape_shoe_data()

    # Check if there is a "Next Page" button and click it
    next_page_button = driver.find_element(By.XPATH, '//*[@class="next-page-button"]')
    if next_page_button.is_enabled():
        next_page_button.click()
        time.sleep(2)  # Adjust the sleep duration as needed
    else:
        break

# Close the web driver when done
driver.quit()

# Print or process the scraped data
for shoe in shoe_data:
    print(shoe)
