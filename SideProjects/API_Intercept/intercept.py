# Name:                                            Renacin Matadeen
# Date:                                               08/09/2020
# Title                               API Intercept: Making Web-Scraping A Lot Easier
#
# ----------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------------------------------------------------



# MAIN FUNCTION WILL STORE TESTING
def main():


    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive',
    }



    url_api_key = "https://api.waqi.info/api/feed/@7389/obs.en.json"
    url="https://aqicn.org/city/usa/connecticu..."

    key = "_2Y2EvVx92AVkcDS8OSzJWXmpjZEQ EydQFmgdIA=="
    token ="LFIGY3TT6X7VQI4YMJAQE7CJMVP74YRQHJGCC6QGAEAAA==="
    rqc = 4

    form={'key':key,'token':token, 'rqc':rqc}

    response = requests.post(url=url_api_key, headers=headers, data=form)
    data = response.text


    soup = BeautifulSoup(data,'html.parser')
    print(soup)

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
