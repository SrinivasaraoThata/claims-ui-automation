"""Claims Overview page object mapped to ParaBank Accounts Overview."""

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ClaimsOverviewPage(BasePage):
    """Page object for the Healthcare Claims Overview screen."""

    # Mapping "Account" elements to "Claim" semantics
    CLAIMS_OVERVIEW_HEADER = (
        By.XPATH, '//h1[contains(text(), "Accounts Overview")]'
    )
    FIRST_CLAIM_LINK = (
        By.XPATH, '//table[@id="accountTable"]/tbody/tr[1]/td[1]/a'
    )
    # Using the balance column to represent the status of the claim
    FIRST_CLAIM_STATUS = (
        By.XPATH, '//table[@id="accountTable"]/tbody/tr[1]/td[2]'
    )

    def is_claims_overview_displayed(self):
        """Return True if the Claims Overview header is visible."""
        self.logger.info("Checking if Claims Overview is displayed.")
        return self.is_visible(self.CLAIMS_OVERVIEW_HEADER)

    def get_first_claim_id(self):
        """Return the text of the first Claim ID link."""
        self.logger.info("Retrieving first Claim ID.")
        return self.get_text(self.FIRST_CLAIM_LINK)

    def get_first_claim_status(self):
        """Return the status text for the first Claim."""
        self.logger.info("Retrieving Status for the first Claim.")
        return self.get_text(self.FIRST_CLAIM_STATUS)
