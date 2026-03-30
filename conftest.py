import os
import logging
import yaml
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Basic logging configuration for the Healthcare Claims Automation
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def config():
    """Load project configuration from config/config.yaml."""
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def browser(config):
    """
    Setup WebDriver for Member Portal automation.
    Supports toggling headless mode via config/config.yaml.
    """
    logger.info("Initializing Member Portal Browser Session...")
    
    browser_cfg = config.get("browser", {})
    options = Options()
    
    if browser_cfg.get("headless", True):
        logger.info("Running in Headless Mode (CI/CD Optimization)")
        options.add_argument("--headless=new")
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    
    # We set implicit wait to 0 to rely entirely on Explicit Waits (WebDriverWait)
    # as defined in our BasePage strategy for better stability.
    driver.implicitly_wait(browser_cfg.get("implicit_wait", 0))

    yield driver

    logger.info("Closing Member Portal Browser Session...")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture a screenshot on test failure for Root Cause Analysis (RCA).
    Saves it to the screenshots/ directory.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("browser")
        if driver:
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"screenshots/fail_{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            logger.error("Test failed! Screenshot saved to: %s", screenshot_path)
