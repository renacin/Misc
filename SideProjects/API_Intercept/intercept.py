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
        "authority": "www.latlong.net",
        "method": "POST",
        "path": "/",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-length": "591",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "PHPSESSID=976otjtrmadlb1clbu4r93tiv4",
        "origin": "https://www.latlong.net",
        "referer": "https://www.latlong.net/",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }

    url_api = "https://www.latlong.net/"

    place = "80 Binder Twine Trail"
    lltoken = "94a783bea0155c548fa47da86871f8c3ddfb566a21bd321cdc9c7762cc3b1aae"
    llcd = 0
    g_recaptcha_response = "03AGdBq27hrnbQTkXOLLKP-j5DgAiHdCNXoo7qRe9K1g5SG3t46FLG78bomiNxZilKqYHRdSlO9kpS3UNg5iPdKXhB4zIZuYXJdXYgnk1z0yTYISAfu3fKDHedvFVemK0Dm5lfpvLmt3vRHuFk-bu2C_yGBiXNqZunhkzN5LFitGr_dx_amQuP-5svjxfb__1vf2I4-C81uX7pXP8NTFq9qjlQoR8S4DIGFvgvVC9LKaOqFChUtBWkr-PAKl1pQjPdMxDe7AkLiJhGyJAHJEiDZ1TfIXZgKOaoYa4roeXA_aKRvL_zrqTXVSXi5HRDidP7g3cAJvUiOSmNEr7L1faNViPuEhrCNC8TM4aKQwzDsFl0YATPyNtOmdGPe03Xvva7xwAUynA8mCA3QQvpWqHrypDyfttOPpu5Lmr9ZFB-zt3mzOxeEfmYrl_HQ0zTlNkl8IKWO9vqO_Nb"

    form = {"place": place, "lltoken": lltoken, "llcd": llcd, "g-recaptcha-response": g_recaptcha_response}

    response = requests.post(url=url_api, headers=headers, data=form)
    data = response.text

    soup = BeautifulSoup(data,'html.parser')
    print(soup)

# ----------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
