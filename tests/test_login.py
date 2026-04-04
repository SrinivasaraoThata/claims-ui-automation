"""Test suite for REQ-LOG-01: Secure Member Authentication."""

from pages.LoginPage import MemberLoginPage
from pages.ClaimsOverviewPage import ClaimsOverviewPage


def test_valid_login_req_log_01(browser, config):
    """Validates REQ-LOG-01: Secure Member Authentication."""
    member_username = config['member_credentials']['username']
    member_password = config['member_credentials']['password']
    portal_url = config['base_url']

    login_page = MemberLoginPage(browser)
    claims_page = ClaimsOverviewPage(browser)

    # 1. Navigate to Member Portal login screen
    login_page.open_url(portal_url)

    # 2. Submit valid member credentials
    login_page.login_as_member(member_username, member_password)

    # 3. Assert landing on the Claims Overview confirms authenticated session
    assert claims_page.is_claims_overview_displayed(), (
        "REQ-LOG-01 FAILED: Claims Overview page not displayed after login. "
        "Member session was not authenticated successfully."
    )

    login_page.logger.info(
        "REQ-LOG-01 PASSED: Member '%s' authenticated and session established.",
        member_username
    )
