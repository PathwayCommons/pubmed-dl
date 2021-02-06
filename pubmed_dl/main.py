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


def main(start_date: str, end_date: str, request_file: str):
    """
    Main requires 3 arguments. 
    
    The first one is start date (eg: YYYY/MM/DD).

    The second one is end date (eg: 2021/02/05).
    
    The third one is the filename where the data needs to be written to.

    """
    start_time = time.time()
    output_filepath: Path = Path(request_file)
    output_filepath.parents[0].mkdir(parents=True, exist_ok=True)
    pmids = get_list_pmid(start_date, end_date)
    with open(output_filepath, "w") as f:
        for batch in uids_to_docs(pmids):
            for doc in batch:
                f.write(f"{json.dumps(doc)}\n")
    logging.info(f"Done writing data from {start_date} to {end_date} onto file named: {output_filepath}")
    duration = time.time() - start_time
    logging.info(f"Total run time for {len(pmids)} docs: {duration}s")


if __name__ == "__main__":
    typer.run(main)

