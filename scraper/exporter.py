import logging
import os

import pandas as pd


def save_to_csv(data: list[dict], filename: str = "amazon_items.csv", folder: str = "data") -> None:
    """Saves the items to CSV file."""
    if not data:
        logging.warning("⚠️ Empty data list — the file will not be saved.")
        return

    try:
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, filename)
        df = pd.DataFrame(data)
        df.to_csv(path, index=False, encoding="utf-8")
        logging.info(f"✅ Saved {len(df)} jobs to '{path}'")
    except Exception as e:
        logging.exception("❌ Error saving CSV file")
