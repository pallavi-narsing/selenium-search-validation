import pytest
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Ensure SSL module is properly loaded
ssl._create_default_https_context = ssl._create_unverified_context

# URL of the Selenium Playground Table Search Demo
URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"


@pytest.fixture(scope="module")
def browser():
    """Setup and teardown for the browser instance."""
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)  # Ensure ChromeDriver is installed
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search_functionality(browser):
    """Test to validate the search functionality on the table search demo."""
    # Navigate to the URL
    browser.get(URL)

    # Locate the search input box and enter 'New York'
    search_box = browser.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("New York")

    # Wait for results to load
    browser.implicitly_wait(5)

    # Verify that 5 results are displayed
    rows = browser.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    assert rows, "No search results found, expected at least one result."
    assert len(rows) == 5, f"Expected 5 results, but got {len(rows)}"

    # Verify that all results contain 'New York'
    for row in rows:
        assert "New York" in row.text, f"Row does not contain 'New York': {row.text}"

    print("Test passed: Search functionality works correctly.")


# Additional Setup Instructions
# Environment Setup:
# - Follow good coding practices and ensure the script is compatible with the latest stable Selenium version.
# - Use Python 3.8+ for best compatibility.
# - Keep ChromeDriver updated to match your Chrome browser version.
#
# Browser Compatibility:

# - Test with at least one major browser (Chrome, Firefox).
# - For Firefox, install GeckoDriver: https://github.com/mozilla/geckodriver/releases
# - Modify the browser fixture to support multiple browsers if needed.
#
# Steps to Set Up:
# 1. Install dependencies:
#    pip install selenium pytest
# 2. Download and install ChromeDriver from:
#    https://sites.google.com/chromium.org/driver/
# 3. Ensure ChromeDriver is in your system PATH or specify its location explicitly when initializing the driver.
# 4. Run the test using:
#    pytest qa_selenium_test.py
