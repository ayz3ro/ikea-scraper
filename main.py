import logging
from time import strftime

from scraper.exporter import save_to_csv
from scraper.scraper import scrape_products


def get_user_input() -> tuple[str, int]:
    """Receiving and verifying user input."""
    query = input("🔍 Enter your search query (e.g., stuhl): ").strip()

    while True:
        try:
            pages = int(input("📄 How many pages should be parsed? "))
            if pages <= 0:
                raise ValueError
            break
        except ValueError:
            print("Enter a positive number.")

    return query, pages


def generate_filename(query: str) -> str:
    """Creating a CSV file name based on the date and request."""
    date_str = strftime('%Y-%m-%d')
    return f"{query}_ikea_{date_str}.csv".replace(" ", "_")


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    query, pages = get_user_input()
    logging.info(f"🔍 Launching the IKEA parser: request='{query}', pages={pages}")

    try:
        products = scrape_products(query, pages)
        if not products:
            logging.warning("No products found.")
        filename = generate_filename(query)
        save_to_csv(products, filename)
        logging.info(f"Data stored in {filename}")
    except Exception as e:
        logging.exception("Error during parsing or saving.")


if __name__ == '__main__':
    main()
