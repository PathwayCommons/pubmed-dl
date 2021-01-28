**Usage**

A program developed for the easy retrieval of Pubmed records over a given time. Can be run from command line using user inputted dates.

**Public methods**

*uids_to_docs*

Works by taking in a list of PMID's and returns all their data as a JSON dictionary. Outputs in the format of {"uid": 'PMID here', "text": "Title and Abstract joined here"}

*get_list_pmid*

Works by taking in two strings that consist of the start and end date respectively in the YYYY/MM/DD format (ex: "2020/01/10"). This program returns a list of all PMID's that were uploaded in the requested time frame. It uses the PubMed EUTILS URL's to send a request using the start and end dates, with extra filters for only Journal Articles (Publication type) and English for the language. It creates a .json file (for every 10,000 records) with the URL request then reads through it and stores all the PMID's in a list. If there are more than 10,000 records (which would mean there is more than 1 file) then the method goes through all the files and grabs all the PMID's and stores it in a list called 'store'. This list is returned by the method once all the files are read then deleted.

**Example**

An example usage is by getting the list of PMID's from get_list_pmid and then passing that list to the uids_to_docs for the data of all the PMID's in the given time frame.

Can be run on Command line with basic python run command
```
py main.py
```

Program requires two dates to be inputted for start and end
```
Enter start date (YYYY/MM/DD): "Enter your start date here"
Enter end date (YYYY/MM/DD): "Enter your end date here"
```

The Program then runs and outputs the total records and an URL for every 10,000 records, until all records have been downloaded. Immediately after this the program grabs the PMID's of all the records and then passes the list of PMID's to the ```uids_to_docs``` method, which then gets all the data (Title, Abstract) and writes it to a file named test.json.

After the Program is finished running, it will output a statement.
```
Done writing data from "start date" to "end date" onto file named: test.json
```
