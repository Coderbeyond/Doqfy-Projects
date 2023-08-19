from scraper.utils import scrape_and_store_data
import threading

if __name__ == "__main__":
    scraper_thread = threading.Thread(target=scrape_and_store_data)
    scraper_thread.start()
