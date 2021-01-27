import json
import requests
import os
from ncbi import uids_to_docs , get_list_pmid

def main():
    ab = open("test.json", 'w')
    store = get_list_pmid("2020/12/01","2020/12/02")
    print(len(store))
    here = uids_to_docs(store)
    for item in here:
        ab.write(json.dumps(item))
        ab.write("\n")
    ab.close()

if __name__ == "__main__":
    main()