# Name:                                            Renacin Matadeen
# Date:                                               08/09/2020
# Title                               API Intercept: Making Web-Scraping A Lot Easier
#
# ----------------------------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
# ----------------------------------------------------------------------------------------------------------------------
"""
References:
    + https://www.youtube.com/watch?v=LPU08ZfP-II&list=PLL2hlSFBmWwwvFk4bBqaPRV4GP19CgZug&index=1

Notes:
    + How do I scrape data in a more effective way?
        - Intercept an API?
        -
"""


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

    url_api_key = "https://www.latlong.net/"

    place = "80 Binder Twine Trail"
    lltoken ="01d28d2a5356a393450cd973392d68280fe4df79cfc51b7a66f3dd6469746d23"
    llcd = 0
    g_recaptcha_response = "03AGdBq25IYKiAiJZYx0FA7ALENF2mA3zEjcxMl3Z1jf43hjRBnQEHXEnpsLeS3uJxZVARKEBt12Y6Stg_IzgWo-PoOwXNxAVRD-ed0mU2fe2DWK4EmcA_q3rJIcwmzeZkeTLCOQXZUen-HEFt0cKeN78l998PNhkuh_LZw_YYPULjtjOd1Zk-F0Vn79n_Und4JI2jRIa8zPPVshAqH4TFt0jyA7ZiNd7CHsjyzfIwqbMHMxxXIYRiS4dfRf-mwgEdbAhbG20Q6aAbBnd9GW-9wOHAcmcSohqx6qEuoPBc7aerdwwmds4WPyQxpwXzBA97NlGgTXtpOR9OyWftQ2EV0EPev5ZOSo4R-cti6GX3w1FVdRgAxmNjBgEPf4WcaBdmhrwkXg5CWmfi6QCijyW0Uqcxcg2KrCF9UePocjwdjq_slgSxxSYy3m3KXYIoC8ZKQpW8-rTDoZby"

    form={'place':place, 'lltoken':lltoken, 'llcd':llcd, "g-recaptcha-response":g_recaptcha_response}

    response = requests.post(url=url_api_key, headers=headers, data=form)
    data = response.text

    soup = BeautifulSoup(data,'html.parser')
    print(soup)

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
