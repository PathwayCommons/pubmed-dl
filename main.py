import json
import requests
import os
import sys
from ncbi import uids_to_docs , get_list_pmid

def main():
    ab = open("test.json", 'w')
    start = input("Enter start date (YYYY/MM/DD): ")
    end = input("Enter end date (YYYY/MM/DD): ")
    here = uids_to_docs(get_list_pmid(start,end))
    for item in here:
        ab.write(json.dumps(item))
        ab.write("\n")
    print("Done writing data from "+start+" to "+end+" onto file named: test.json")
    ab.close()

if __name__ == "__main__":
    main()
