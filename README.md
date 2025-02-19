Project Overview

This project automates the search functionality validation on the Selenium Playground Table Search Demo. 
Using Selenium WebDriver and pytest, it ensures that searching for 'New York' returns the correct results.

 Key Features

Automated Search Validation: Ensures the search feature works as expected.

Cross-Browser Compatibility: Supports Chrome (ChromeDriver) and can be extended for Firefox.

Robust Assertions: Validates the correctness of search results.

Efficient Test Execution: Uses pytest fixtures for optimized setup and teardown.

PEP8 Compliance: Follows best practices for clean, maintainable code.

No Hardcoded Waits: Implements implicit waits for dynamic content handling.

Test Scenario: Search Functionality

Objective:

Validate that searching for "New York" in the Table Search Demo correctly filters the results to show exactly 5 entries.

 Steps Executed:

Open the Selenium Playground Table Search Demo.

Locate the search box.

Enter "New York" into the search input field.

Wait for results to populate dynamically.

Validate that exactly 5 rows are displayed.

Verify that all displayed rows contain "New York".

Assert test success if conditions are met, otherwise fail.

Best Practices

Follow PEP8 Guidelines: Ensure code readability and maintainability.

Use Explicit Waits Instead of sleep(): Avoids unnecessary delays and improves efficiency.

Use Fixtures for Setup and Teardown: Helps manage WebDriver sessions efficiently.

Implement Assertions for Robust Validation: Ensures test reliability.

Keep Test Data Externalized: Allows easy modifications and scalability.

Use Headless Mode for CI/CD: Enables seamless integration in automation pipelines.

Regularly Update Dependencies: Keeps WebDriver and browser versions compatible.

Tech Stack

Programming Language: Python (3.8+ recommended)

Automation Framework: Selenium WebDriver

Testing Framework: pytest

Browser Driver: ChromeDriver (Chrome), extendable for Firefox

 Project Structure

📦 project

 ┣ qa_selenium_test.py   
 ┣  README.md            
 ┗ requirements.txt     

Prerequisites

Ensure the following are installed on your system:

Python 3.8+

pip (Python package manager)

ChromeDriver(for Chrome)

Installation & Setup

Clone the Repository:

git clone https://github.com/pallavi-narsing/selenium-search-validation.git
cd selenium-search-validation

Install Required Dependencies:

pip install -r requirements.txt

Download & Install ChromeDriver:

Place it in a directory included in your system PATH.

Verify Installation:

chromedriver --version

Running the Test

To execute the test script, navigate to the project directory and run:

pytest qa_selenium_test.py

Expected Output

The script will open the Selenium Playground Table Search Demo.

It will search for "New York" and validate the results.

The test will pass if exactly 5 results are displayed, each containing "New York".

Troubleshooting

WebDriver Exception: Ensure ChromeDriver is correctly installed and added to PATH.

Test Fails Due to Element Not Found: Verify that the website structure hasn’t changed.

Browser Not Opening: Ensure Selenium and WebDriver versions are compatible.

Future Enhancements

Add support for Firefox WebDriver.

Implement data-driven testing using external test data.

Integrate CI/CD pipelines for automated execution.

Author
Pallavi 

