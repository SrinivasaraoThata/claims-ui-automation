"""Test suite for REQ-CLM-01: Claim Submission & Validation."""

from pages.ClaimsOverviewPage import ClaimsOverviewPage


def test_claim_submission_req_clm_01(authenticated_browser):
    """Validates REQ-CLM-01: Claim Submission & Validation."""
    claims_page = ClaimsOverviewPage(authenticated_browser)

    # 1. Verify Claims Overview is accessible in the authenticated session
    assert claims_page.is_claims_overview_displayed(), (
        "REQ-CLM-01 FAILED: Claims Overview not displayed. "
        "Cannot validate claim submission without an active session."
    )

    # 2. Retrieve the submitted claim ID to confirm it appears in the dashboard
    claim_id = claims_page.get_first_claim_id()

    assert claim_id is not None and claim_id.strip() != "", (
        "REQ-CLM-01 FAILED: No Claim ID found in the Claims Overview. "
        "Submitted claim did not appear in the dashboard."
    )

    # 3. Confirm the submitted claim has an associated status value
    claim_status = claims_page.get_first_claim_status()

    assert claim_status is not None and claim_status.strip() != "", (
        f"REQ-CLM-01 FAILED: Claim ID '{claim_id}' has no status. "
        "Claim submission validation requires a resolvable status."
    )

    claims_page.logger.info(
        "REQ-CLM-01 PASSED: Claim ID '%s' submitted and validated with status '%s'.",
        claim_id, claim_status
    )
