"""Base page abstraction layer for all Selenium page interactions."""

import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Base abstraction layer for Selenium interactions."""

    def __init__(self, driver):
        """Initialize BasePage with a WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.logger = logging.getLogger(__name__)

    def verify_session_is_active(self, logout_link_locator):
        """
        Health Check: Ensures the session is still active by checking for the logout link.
        This prevents cascading failures if ParaBank times out.
        """
        self.logger.info("Verifying active session via locator: %s", logout_link_locator)
        if not self.is_visible(logout_link_locator):
            self.logger.warning("Session lost! Redirecting to login or raising exception.")
            return False
        return True

    def open_url(self, url):
        """Navigate the browser to the specified URL."""
        self.logger.info("Navigating to: %s", url)
        self.driver.get(url)

    def find_element(self, locator):
        """Wait for and return the element matching the locator."""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            self.logger.error(
                "Element not found within timeout: %s", locator
            )
            raise

    def click_element(self, locator):
        """Wait for element to be clickable then click it."""
        self.logger.info("Clicking element: %s", locator)
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Clear the element and type the given text into it."""
        self.logger.info("Entering text into: %s", locator)
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return the visible text of the element."""
        return self.find_element(locator).text

    def is_visible(self, locator):
        """Return True if the element is visible, False otherwise."""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
