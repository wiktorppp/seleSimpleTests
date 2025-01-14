from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def main_test_def(driver):
    try:
        # Open the website
        driver.get("https://tester-wp.azurewebsites.net/")

        # Verify the page title
        expected_title = "Home Page - MyMvcApp"
        assert expected_title in driver.title, f"Expected title '{expected_title}' not found in '{driver.title}'"
        print("Page title verification passed.")

        # Wait for the page to load
        time.sleep(3)

        try:
            home_page_link = driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul/li[1]/a")
            home_page_link.click()
            print("Successfully clicked on 'Home'!")

            time.sleep(3)
        except:
            print("'Home' interaction failed:", e)

        try:
            privacy_link = driver.find_element(By.LINK_TEXT, "Privacy")
            privacy_link.click()
            print("Successfully clicked on 'Privacy'!")
                
            time.sleep(3)  # Let the new page load
        except Exception as e:
            print("Privacy interaction failed:", e)

    finally:
        # Close the browser
        driver.quit()

# Initialize the WebDriver (ensure the correct path for your driver)
main_test_def(webdriver.Edge())
main_test_def(webdriver.Firefox())
main_test_def(webdriver.Chrome())
