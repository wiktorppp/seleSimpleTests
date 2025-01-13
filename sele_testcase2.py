from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (ensure the correct path for your driver)
driver = webdriver.Edge()
#driver1 = webdriver.Firefox()
#driver2 = webdriver.Chrome()

try:
    # Open the website
    driver.get("https://onet.pl/")

    # Verify the page title
    expected_title = "Onet"
    assert expected_title in driver.title, f"Expected title '{expected_title}' not found in '{driver.title}'"
    print("Page title verification passed.")

    # Wait for the page to load
    time.sleep(3)

    try:
        accept_cookies = driver.find_element(By.XPATH,"/html/body/div[10]/div/div[2]/div/div[6]/button[2]")
        accept_cookies.click()
        print("Cookies accepted!")

        time.sleep(3)
    except:
        print("Accepting failed:", e)
    
    try:
        selenium_training_link = driver.find_element(By.CLASS_NAME, "Logo_logoLink__qUFvz")
        selenium_training_link.click()
        print("Successfully clicked on 'Logo header'.")
        
        time.sleep(3)  # Let the new page load
    except Exception as e:
        print("Logo interaction failed:", e)

finally:
    # Close the browser
    driver.quit()
