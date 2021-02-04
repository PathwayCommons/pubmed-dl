#!/usr/bin/env python
import json
from pubmed_dl.ncbi import get_list_pmid, uids_to_docs

def main():
    ab = open("test.json", 'w')
    start = input("Enter start date (YYYY/MM/DD): ")
    end = input("Enter end date (YYYY/MM/DD): ")
    val = get_list_pmid(start,end)
    for batch in uids_to_docs(val):
        ab.write("\n".join([json.dumps(doc) for doc in batch]))  
    print(f"Done writing data from {start} to {end} onto file named: test.json")
    ab.close()

if __name__ == "__main__":
    main()
