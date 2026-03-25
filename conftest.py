# Author: Srinivasa Rao Thata
# Year: 2026
"""Session-scoped browser fixture for Healthcare Claims UI automation."""

import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Basic logging configuration for the Healthcare Claims Automation
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def browser():
    """
    Setup WebDriver for Member Portal automation.
    Yields the driver and tears it down after the session.
    """
    logger.info("Initializing Member Portal Browser Session...")
    options = Options()
    # options.add_argument("--headless") # Useful for CI/CD pipelines
    options.add_argument("--window-size=1920,1080")

    # Initialize Chrome WebDriver (Selenium 4 natively manages drivers)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver

    logger.info("Closing Member Portal Browser Session...")
    driver.quit()
