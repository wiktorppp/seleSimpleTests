from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (ensure the correct path for your driver)
driver = webdriver.Chrome()  # Or use webdriver.Firefox(), webdriver.Edge(), etc.

try:
    # Open the website
    driver.get("https://toolsqa.com/")

    # Maximize the browser window
    #driver.maximize_window()

    # Verify the page title
    expected_title = "Tools QA"
    assert expected_title in driver.title, f"Expected title '{expected_title}' not found in '{driver.title}'"
    print("Page title verification passed.")

    # Wait for the page to load
    time.sleep(3)  # Consider using WebDriverWait for better handling

    # Interact with a menu item (e.g., click on the 'Selenium Training' link if present)
    try:
        selenium_training_link = driver.find_element(By.LINK_TEXT, "SELENIUM TRAINING")
        selenium_training_link.click()
        print("Successfully clicked on 'SELENIUM TRAINING'.")

        # Verify navigation to the correct page
        time.sleep(3)  # Let the new page load
        assert "selenium-training" in driver.current_url, "Navigation to 'Selenium Training' failed."
        print("Navigation verification passed.")
    except Exception as e:
        print("Menu item interaction failed:", e)

finally:
    # Close the browser
    driver.quit()
