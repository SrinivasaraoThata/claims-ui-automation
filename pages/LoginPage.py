"""Login page object for the Healthcare Member Portal."""

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class MemberLoginPage(BasePage):
    """Page object for the Healthcare Member Portal login screen."""

    # Locators
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//input[@value="Log In"]')

    def login_as_member(self, username, password):
        """Enter credentials and submit the login form."""
        self.logger.info("Attempting login for member: %s", username)
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
