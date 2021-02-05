import json
from pubmed_dl.ncbi import get_list_pmid, uids_to_docs
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseSettings
import time


dot_env_filepath = Path(__file__).absolute().parent.parent / ".env"
load_dotenv(dot_env_filepath)


class Settings(BaseSettings):
    loglevel: str = os.getenv("LOGLEVEL", "INFO")


settings = Settings()
logging.basicConfig(level=settings.loglevel)


def main():
    start_time = time.time()
    start = input("Enter start date (YYYY/MM/DD): ")
    end = input("Enter end date (YYYY/MM/DD): ")
    val = get_list_pmid(start, end)
    with open("test.json", "w") as f:
        for batch in uids_to_docs(val):
            for doc in batch:
                f.write(f"{json.dumps(doc)}\n")
    logging.info(f"Done writing data from {start} to {end} onto file named: test.json")
    duration = time.time() - start_time
    logging.info(f"Retrieved {len(val)} docs in {duration}s")


if __name__ == "__main__":
    main()
