import requests
import json

#getting start and end dates to get data from
start = input("Enter start date in (YYYY/MM/DD) format: ")
end = input("Enter end date in (YYYY/MM/DD) format: ")
#using the esearch eutil to grab the 'Webenv' and 'total record' values to then send to efetch
search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&mindate="+start+"&maxdate="+end+"&usehistory=y&retmode=json"
search_r = requests.post(search_url)
data = search_r.json()
webenv = data["esearchresult"]['webenv']
total = int(data["esearchresult"]['count'])
#using the efetch eutil with the 'Webenv' from esearch to grab all the data
fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmax=9999&query_key=1&WebEnv="+webenv
#Total records found in requested time frame
print("Total records :"+str(total))
#count used for URL number
count = 1

#First loop to grab all the data and write it to .json files, each file only has 10,000 records
for i in range(0, total, 10000):
    #changes the retstart value by 10,000 every iteration so we don't print the same records over again
    this_fetch = fetch_url+"&retstart="+str(i)
    #URL that can be used in browser for data viewing
    print("URL "+str(count)+": "+this_fetch)
    count += 1
    fetch_r = requests.post(this_fetch)
    #Writing all the data to .json files (1 file per 10,000 records)
    f = open('Pubmed_data/pubmed_batch_'+str(i)+'_to_'+str(i+9999)+".json", 'w')
    f.write(fetch_r.text)
    f.close()

#Second loop to go through each .json file made and retrieve the PMID and abstract for every record
for i in range(0, total, 10000):
    f = open('Pubmed_data/pubmed_batch_'+str(i)+'_to_'+str(i+9999)+".json", 'r')
    ab = open('Pubmed_data/pubmed_batch_'+str(i)+'_to_'+str(i+9999)+"_abstracts.txt", 'w')
    data_file = f.read()
    store = []
    flag = False
    p_flag = False
    for word in data_file.split():
        if word == 'pmid':
            p_flag = True
        elif p_flag == True:
            p_flag = False
            pmid_curr = word
        if word=='abstract':
            flag = True
        elif flag == True:
            store.append(word)
            try:
                if word[-1]=="," and word[-2]=='\"': 
                    flag = False
                    ab.write(pmid_curr)
                    ab.write(' '.join(store))
                    ab.write("\n")
                    store.clear()
            except:
                continue
    f.close()
    ab.close()