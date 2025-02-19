import pytest
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Ensure SSL module is properly loaded
ssl._create_default_https_context = ssl._create_unverified_context

URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)  # Ensure ChromeDriver is installed
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search_functionality(browser):
    browser.get(URL)

    # Locate the search input box and enter 'New York'
    search_box = browser.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_box.send_keys("New York")

    # Wait for results to load
    browser.implicitly_wait(5)

    rows = browser.find_elements(By.XPATH, "//table[@id='example']/tbody/tr")
    assert rows, "No search results found, expected at least one result."
    assert len(rows) == 5, f"Expected 5 results, but got {len(rows)}"

    # Verify that all results contain 'New York'
    for row in rows:
        assert "New York" in row.text, f"Row does not contain 'New York': {row.text}"

    print("Test passed: Search functionality works correctly.")

