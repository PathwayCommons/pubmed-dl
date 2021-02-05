import json
from pubmed_dl.ncbi import get_list_pmid, uids_to_docs
import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseSettings
import time
from typing import Optional


dot_env_filepath = Path(__file__).absolute().parent.parent / ".env"
load_dotenv(dot_env_filepath)


class Settings(BaseSettings):
    loglevel: str = os.getenv("LOGLEVEL", "INFO")


settings = Settings()
logging.basicConfig(level=settings.loglevel)


def main(start: str, end: str, request_file: Optional[str] = typer.Argument(None)):
    """
    Main requires 2 arguments and an optional 3rd argument. 
    
    The first one is start date (eg: YYYY/MM/DD).
    The second one is end date (eg: 2021/02/05).
    
    The third one is the filename where the data needs to be written to, 
    if not specified it will be written to 'test.json'.

    """
    start_time = time.time()
    if request_file is None:
        filename = "test.json"
    else:
        filename = request_file
    start_date = start
    end_date = end
    pmids = get_list_pmid(start_date, end_date)
    with open(filename, "w") as f:
        for batch in uids_to_docs(pmids):
            for doc in batch:
                f.write(f"{json.dumps(doc)}\n")
    logging.info(f"Done writing data from {start_date} to {end_date} onto file named: {filename}")
    duration = time.time() - start_time
    logging.info(f"Total run time for {len(pmids)} docs: {duration}s")


if __name__ == "__main__":
    typer.run(main)

