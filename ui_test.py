import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.90min.com")
    yield driver
    driver.quit()

@pytest.fixture
def header_links(driver):
    ul_element = driver.find_element(By.CLASS_NAME, "fixedUl_ka6l4t")
    li_elements = ul_element.find_elements(By.CLASS_NAME, "li_8cxs15")
    links = [li.text for li in li_elements]
    return links



@pytest.mark.parametrize("category", ["Premier League", "Transfers", "Champions League", "FanVoice", "The Switch",
                                      "EFL", "La Liga", "Serie A", "More"])
def test_header_links(header_links, category):
    assert category in header_links, f"{category} link is missing in the header"
