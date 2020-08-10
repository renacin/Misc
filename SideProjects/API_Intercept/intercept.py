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

    # Look For The Request Tied To The XHR Req | Known as a Ajax Request, Contains Json Data
    url_link = "https://www.latlong.net/_spm4.php"
    headers_dictionary = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

    params_dic = {}
    params_dic["c1"] = "80 binder twine trail"
    params_dic["action"] = "80 binder twine trail"
    params_dic["cp"] = ""


    response = requests.post(url=url_link, data=params_dic)
    print(response.text)
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
