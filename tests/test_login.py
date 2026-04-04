"""Test suite for REQ-LOG-01: Secure Member Authentication."""

from pages.ClaimsOverviewPage import ClaimsOverviewPage


def test_valid_login_req_log_01(authenticated_browser):
    """Validates REQ-LOG-01: Secure Member Authentication."""
    claims_page = ClaimsOverviewPage(authenticated_browser)

    # Assert the shared session landed on Claims Overview —
    # confirms the member was authenticated successfully
    assert claims_page.is_claims_overview_displayed(), (
        "REQ-LOG-01 FAILED: Claims Overview page not displayed after login. "
        "Member session was not authenticated successfully."
    )

    claims_page.logger.info(
        "REQ-LOG-01 PASSED: Member authenticated and session established."
    )
