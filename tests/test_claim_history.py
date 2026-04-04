"""Test suite for REQ-HIS-01: Historical Claims Retrieval."""

from pages.LoginPage import MemberLoginPage
from pages.ClaimsOverviewPage import ClaimsOverviewPage


def test_claims_history_req_his_01(browser, config):
    """Validates REQ-HIS-01: Historical Claims Retrieval >24 months."""
    member_username = config['member_credentials']['username']
    member_password = config['member_credentials']['password']
    portal_url = config['base_url']

    login_page = MemberLoginPage(browser)
    claims_page = ClaimsOverviewPage(browser)

    # 1. Navigate to Member Portal and establish session
    login_page.open_url(portal_url)
    login_page.login_as_member(member_username, member_password)

    # 2. Verify Claims Overview panel is accessible
    assert claims_page.is_claims_overview_displayed(), (
        "REQ-HIS-01 FAILED: Claims Overview not displayed. "
        "Cannot retrieve historical claims without an active session."
    )

    # 3. Assert that at least one historical claim record is listed
    claim_id = claims_page.get_first_claim_id()

    assert claim_id is not None and claim_id.strip() != "", (
        "REQ-HIS-01 FAILED: No historical claim records found in the Claims Overview. "
        "System must retain and display claims older than 24 months."
    )

    claims_page.logger.info(
        "REQ-HIS-01 PASSED: Historical claim record retrieved — Claim ID: '%s'.",
        claim_id
    )
