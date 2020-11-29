# Name:                                            Renacin Matadeen
# Date:                                               11/29/2020
# Title                                 Toronto Police Auctions - Website Parsing
#
# ----------------------------------------------------------------------------------------------------------------------
import time
from selenium import webdriver
# ----------------------------------------------------------------------------------------------------------------------


# A Function That Will Help The User Create An Associated Url Based On Thier Choice
def choose_url(choice):
    base_url = "https://www.policeauctionscanada.com/Browse/"
    cat_dict = {"Jewellery": "C160535", "Coins&Currency": "C6245132", "Electronics":"C161063"}

    # Return The First Page Of The Category
    return base_url + cat_dict[choice] + "?page=0"


# A Function That Will Use A ChromeDriver To Navigate To The Site Chosen
def visit_site(url):
    # Setup Chrome Driver
    path = r"C:\Users\renac\Documents\Programming\Python\Selenium\chromedriver.exe"
    chrome = webdriver.Chrome(executable_path=path)

    # Visit Site | Get Source HTML
    chrome.get(url)
    time.sleep(2)

    # Close Web Driver
    chrome.quit()

# ----------------------------------------------------------------------------------------------------------------------


# Main Function That Will Do Everything
def main():
    url = choose_url("Jewellery")
    visit_site(url)

# ----------------------------------------------------------------------------------------------------------------------

# Main Entry Point Into Python Code
if __name__ == "__main__":
    main()
