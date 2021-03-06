![build](https://github.com/PathwayCommons/pubmed-dl/workflows/build/badge.svg)

# pubmed-dl

A program developed for the easy retrieval of Pubmed record data (PMID, Title, Abstract) over a given time. Can be run from command line using user inputted dates.

## Installation

This repository requires Python 3.8 or later.

### Setting up a virtual environment

Before installing, you should create and activate a Python virtual environment. See [here](https://github.com/allenai/allennlp#installing-via-pip) for detailed instructions.

### Installing the library and dependencies

If you _don't_ plan on modifying the source code, install from `git` using `pip`

```
pip install git+https://github.com/PathwayCommons/pubmed-dl
```

Otherwise, clone the repository locally and then install

```bash
git clone https://github.com/PathwayCommons/pubmed-dl
cd pubmed-dl
pip install --editable .
```

## Usage

The example and explanations below are based on the script's behaviour on Python 3.8

Use an API key provided to you from NCBI in the `.env` file for the expected workings of this program.

### Public methods

*uids_to_docs*

Works by taking in a list of PMID's and returns all their data as a JSON dictionary. Outputs in the format of 

```json
{"uid": "PMID here", "text": "Title and Abstract joined here"}
```
Uses batches of 10,000 PMID's from the list passed to it for each iteration, until the list is completely read. Method also throws exceptions with detailed information of the cause of the exception.

*get_list_pmid*

Works by taking in two strings that consist of the start and end date (publication dates) respectively in the YYYY/MM/DD format (ex: "2020/01/10"). This method outputs the URL's for each batch of 100,000 records in the format of

```bash
URL 1: "Link for the data of records from 0 - 100,000"
URL 2: "Link for the data of records from 100,000 - 200,000"
```

This method also returns a list of all PMID's that were uploaded in the requested time frame. It uses the PubMed EUTILS URL's to send a request using the start and end dates, with extra filters for only Journal Articles (Publication type) and English for the language. It uses the NCBI EUTILS history server to retrieve all the PMID's in the requested time frame, then stores them all in a single list. The list where all the PMID's are retrieved and kept is named 'store' in this method. This list is returned by the method once all the data (PMID's) from the server has been read and stored.

#### Example

An example usage is by getting the list of PMID's from `get_list_pmid` and then passing that list to the `uids_to_docs` for the data of all the PMID's in the given time frame.

### Command line

Can be run on Command line. Call the below command for usage details

```bash
pubmed-dl --help
```

Program requires three arguments to be inputted by the user. 
The first one is the start date in the `YYYY/MM/DD` format (e.g.: `2021/02/04`). 
The second one is the end date in the `YYYY/MM/DD` format (e.g.: `2021/02/05`). 
The third one is the filename where the data needs to be written to (e.g.: `test.json`).

An example input to retrieve the data from `2021/02/04` to `2021/02/05` and store the data to a file named `test.json` would look like:

```bash
pubmed-dl 2021/02/04 2021/02/05 test.json
```

The Program then runs and outputs the total records and an URL for every 10,000 records, until all records have been downloaded. Immediately after this the program grabs the PMID's of all the records and then passes the list of PMID's to the `uids_to_docs` method, which then gets all the data (Title, Abstract) and writes it to a file named `test.json`.

After the Program is finished running, it will output a statement.

```bash
Done writing data from "start date" to "end date" onto file named: `your file name`
```
