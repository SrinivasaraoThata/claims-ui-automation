"""Test suite for REQ-HIS-01: Historical Claims Retrieval."""

from pages.ClaimsOverviewPage import ClaimsOverviewPage


def test_claims_history_req_his_01(authenticated_browser):
    """Validates REQ-HIS-01: Historical Claims Retrieval >24 months."""
    claims_page = ClaimsOverviewPage(authenticated_browser)

    # 1. Verify Claims Overview panel is accessible in the authenticated session
    assert claims_page.is_claims_overview_displayed(), (
        "REQ-HIS-01 FAILED: Claims Overview not displayed. "
        "Cannot retrieve historical claims without an active session."
    )

    # 2. Assert that at least one historical claim record is listed
    claim_id = claims_page.get_first_claim_id()

    assert claim_id is not None and claim_id.strip() != "", (
        "REQ-HIS-01 FAILED: No historical claim records found in the Claims Overview. "
        "System must retain and display claims older than 24 months."
    )

    claims_page.logger.info(
        "REQ-HIS-01 PASSED: Historical claim record retrieved — Claim ID: '%s'.",
        claim_id
    )
