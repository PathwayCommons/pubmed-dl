import json
from pubmed_dl.ncbi import get_list_pmid, uids_to_docs
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseSettings
import time
import typer


dot_env_filepath = Path(__file__).absolute().parent.parent / ".env"
load_dotenv(dot_env_filepath)


class Settings(BaseSettings):
    loglevel: str = os.getenv("LOGLEVEL", "INFO")


settings = Settings()
logging.basicConfig(level=settings.loglevel)


def main(start: str, end: str):
    start_time = time.time()
    start_date = start
    end_date = end
    val = get_list_pmid(start_date, end_date)
    with open("test.json", "w") as f:
        for batch in uids_to_docs(val):
            for doc in batch:
                f.write(f"{json.dumps(doc)}\n")
    logging.info(f"Done writing data from {start_date} to {end_date} onto file named: test.json")
    duration = time.time() - start_time
    logging.info(f"Total run time for {len(val)} docs: {duration}s")


if __name__ == "__main__":
    typer.run(main)
