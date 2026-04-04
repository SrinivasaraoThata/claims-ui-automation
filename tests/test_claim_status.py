"""Test suite for validating Healthcare Member claim status visibility."""

from pages.ClaimsOverviewPage import ClaimsOverviewPage


def test_adjudication_status_req_clm_02(authenticated_browser):
    """Validates REQ-CLM-02: Real-time Adjudication Status Updates."""
    claims_page = ClaimsOverviewPage(authenticated_browser)

    # 1. Verify Claims Overview is available in the authenticated session
    assert claims_page.is_claims_overview_displayed(), (
        "Claims Overview page is not visible after login."
    )

    # 2. Assert that a 'Claim ID' is visible and has a 'Status'
    claim_id = claims_page.get_first_claim_id()
    claim_status = claims_page.get_first_claim_status()

    assert claim_id is not None and claim_id.strip() != "", (
        "Claim ID should be visible to the Member."
    )
    assert claim_status is not None and claim_status.strip() != "", (
        f"Claim ID {claim_id} should have a corresponding Status."
    )

    claims_page.logger.info(
        "Successfully validated Claim ID: %s with Status: %s",
        claim_id, claim_status
    )
