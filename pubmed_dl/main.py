#!/usr/bin/env python
import json
import requests
import os
import sys
from pubmed_dl.ncbi import get_list_pmid, 

def main():
    ab = open("test.json", 'w')
    start = input("Enter start date (YYYY/MM/DD): ")
    end = input("Enter end date (YYYY/MM/DD): ")
    val = get_list_pmid(start,end)
    here = uids_to_docs(val)
    for item in here:
        ab.write(json.dumps(item))
        ab.write("\n")
    print(f"Done writing data from {start} to {end} onto file named: test.json")
    ab.close()

if __name__ == "__main__":
    main()
