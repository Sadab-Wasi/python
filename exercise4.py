import time
from selenium import webdriver

def countFollowers(link):
    if (link==""):
        link = "https://twitter.com/KMbappe";
     
    driver = webdriver.Chrome("chrome_driver\chromedriver.exe")
    driver.get(link)
    time.sleep(5)

    count_followers = driver.find_element_by_partial_link_text("Followers").text

    driver.quit()

    return count_followers

try:
    x = input("Enter your Twitter link:")
    y = countFollowers(x)

    print()
    print("The total number of followers is : ", y.split(" ")[0])

except ValueError:
    print("Please try again ...")