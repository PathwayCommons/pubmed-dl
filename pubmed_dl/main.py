import json
import requests
import os
import sys
from ncbi import uids_to_docs , get_list_pmid

def main():
    ab = open("test.json", 'w')
    #start = input("Enter start date (YYYY/MM/DD): ")
    #end = input("Enter end date (YYYY/MM/DD): ")
    start = "2020/12/04"
    end = "2020/12/07"
    val = get_list_pmid(start,end)
    for batch in uids_to_docs(val):
        ab.write("\n".join([json.dumps(doc) for doc in batch]))  
    print(f"Done writing data from {start} to {end} onto file named: test.json")
    ab.close()

if __name__ == "__main__":
    main()