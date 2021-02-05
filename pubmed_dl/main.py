import json
import typer
from pubmed_dl.ncbi import get_list_pmid, uids_to_docs

def main(start: str, end: str):
    start_date = start
    end_date = end
    val = get_list_pmid(start_date,end_date)
    with open("test.json", "w") as f:
        for batch in uids_to_docs(val):
            for doc in batch:
                f.write(f"{json.dumps(doc)}\n")
    print(f"Done writing data from {start_date} to {end_date} onto file named: test.json")

if __name__ == "__main__":
    typer.run(main)
