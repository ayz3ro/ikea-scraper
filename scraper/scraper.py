import logging
from time import sleep
from typing import List, Dict

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def scrape_products(query: str, pages: int = 1) -> List[Dict[str, str]]:
    """Search for products on the IKEA website by keyword (e.g., 'stuhl') and number of pages."""

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    except WebDriverException:
        logging.exception("Unable to launch Chrome WebDriver")
        return []

    base_url = f"https://www.ikea.com/de/de/search/products/?q={query}"
    results = []

    try:
        for page in range(pages):
            page_url = f"{base_url}&page={page + 1}"
            logging.info(f"[{page + 1}/{pages}] Loading: {page_url}")
            driver.get(page_url)
            sleep(6)

            products = driver.find_elements(By.CSS_SELECTOR, "div.plp-fragment-wrapper")
            if not products:
                logging.warning(f"No products on the page {page + 1}")

            for product in products:
                try:
                    link_element = product.find_element(By.CSS_SELECTOR, "a.plp-product__image-link")
                    link = link_element.get_attribute("href").strip()

                    title = product.find_element(By.CSS_SELECTOR, "span.plp-price-module__product-name").text.strip()
                    description = product.find_element(By.CSS_SELECTOR,
                                                       "span.plp-price-module__description").text.strip()

                    price_int = product.find_element(By.CSS_SELECTOR, "span.plp-price__integer").text.strip()
                    price_decimal = product.find_element(By.CSS_SELECTOR, "span.plp-price__decimal").text.strip()
                    currency = product.find_element(By.CSS_SELECTOR, "span.plp-price__currency").text.strip()
                    price = f"{price_int}{price_decimal} {currency}"

                    full_title = f"{title} {description}"

                    results.append({"title": full_title, "price": price, "link": link})
                except Exception as e:
                    logging.warning(f"Error parsing product: {e}")
                    continue

    except Exception:
        logging.exception("Error parsing products")
    finally:
        driver.quit()

    return results
