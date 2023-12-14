from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_behance(browser):
    browser.get("https://www.behance.net/gallery/18988225/B-Yoga-Website")
    WebDriverWait(browser, 10).until(EC.title_contains("B Yoga Website"))
    assert "B Yoga Website" in browser.title
    assert browser.find_element(By.ID, "primary-project-content").is_displayed()
