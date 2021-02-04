import json

from pubmed_dl.ncbi import get_list_pmid, uids_to_docs


def main():
    start = input("Enter start date (YYYY/MM/DD): ")
    end = input("Enter end date (YYYY/MM/DD): ")
    val = get_list_pmid(start, end)
    with open("test.json", "w") as f:
        for batch in uids_to_docs(val):
            for doc in batch:
                f.write(f"{json.dumps(doc)}\n")
    print(f"Done writing data from {start} to {end} onto file named: test.json")

if __name__ == "__main__":
    main()
