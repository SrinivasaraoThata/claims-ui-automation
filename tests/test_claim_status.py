"""Test suite for validating Healthcare Member claim status visibility."""

from pages.LoginPage import MemberLoginPage
from pages.ClaimsOverviewPage import ClaimsOverviewPage


def test_adjudication_status_req_clm_02(browser, config):
    """Validates REQ-CLM-02: Real-time Adjudication Status Updates."""
    member_username = config['member_credentials']['username']
    member_password = config['member_credentials']['password']
    portal_url = config['base_url']

    login_page = MemberLoginPage(browser)
    claims_page = ClaimsOverviewPage(browser)

    # 1. Navigate to Member Portal
    login_page.open_url(portal_url)

    # 2. Log in as a member
    login_page.login_as_member(member_username, member_password)

    # 3. Verify Claims Overview is available
    assert claims_page.is_claims_overview_displayed(), (
        "Claims Overview page is not visible after login."
    )

    # 4. Assert that a 'Claim ID' is visible and has a 'Status'
    claim_id = claims_page.get_first_claim_id()
    claim_status = claims_page.get_first_claim_status()

    assert claim_id is not None and claim_id.strip() != "", (
        "Claim ID should be visible to the Member."
    )
    assert claim_status is not None and claim_status.strip() != "", (
        f"Claim ID {claim_id} should have a corresponding Status."
    )

    login_page.logger.info(
        "Successfully validated Claim ID: %s with Status: %s",
        claim_id, claim_status
    )
