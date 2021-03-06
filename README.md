# secdata : All Data reported to the Securities and Exchange Commission

## About
A module to easily **Download Financial Data** reported to the Securities and Exchange Commision (SEC).

It deploys SEC's RESTful APIs, which delivers JSON-formatted data without requiring authentication or API keys.

Currently included in the APIs are the submissions history by filer and the XBRL data from financial statements (forms 10-Q, 10-K,8-K, 20-F, 40-F, 6-K, and their variants).

The JSON structures are updated throughout the day, in real time, as submissions are disseminated.

More info about the APIs can be found [here](https://www.sec.gov/edgar/sec-api-documentation)

## Installation

Binary installers are available at [PyPI (Python Package Index)](https://pypi.org/project/secdata/) .

```sh
pip install secdata
```

For a manual installation, source code is [hosted on Github](https://github.com/voulkon/secdata).

## Methods

* fetch_companies_info(return_dataframe = False , file_if_info_already_downloaded = "companiesinfo.csv") : 
	
	Sets the sec_companies_info property, 
	Which is a table containing: 
	* CIK (Central Index Key) 
	* Ticker (AAPL, MSFT, TSLA, etc.) and 
	* Name (Apple Inc., MICROSOFT CORP, Tesla, etc) .
	
	for each company reporting to the SEC
	
	From that table one can find CIKs of interest in order to use them in the fetch_facts() method
	

* fetch_facts(ciks) :
	All Sec Facts (e.g. Assets, Depreciation, Net Income, Number of Shares) available
	for the companies of which the ciks are provided
	

## Example
```
#Import Class
from secdata import SecFactsDownloader

#Initiate Downloader
my_downloader = SecFactsDownloader("my_email@my_domain.com")

#Download Central Index Key per company
#To find CIKs of interest
my_downloader.fetch_companies_info()


#320193 for Apple, 789019 for Microsoft, 1652044 for Google
df_1 = my_downloader.fetch_facts([320193, 789019, 1652044])

#1318605 for Tesla, 37996 for Ford
df_2 = my_downloader.fetch_facts([1318605, 37996])

```

