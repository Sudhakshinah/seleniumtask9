from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class Sudha:
    username = "standard_user"
    password = "secret_sauce"

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# logging into the webpage

    def login(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(4)
        self.driver.find_element(By.ID, "user-name").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

#  method to Fetch the title of the page
    def fetch_tile(self):
        return self.driver.title

# method to get the current url of the page

    def current_url(self):
        return self.driver.current_url

# This function extracts the contents of the page and store in a list
    def contents(self):
        contents = self.driver.find_elements(By.XPATH,"//div[@class='inventory_list']/div[@class='inventory_item']")
        print(len(contents))

# Looping through the list and extract each content in the page

        for content in contents:
            text = content.text


# writing the  extracted content in  a text file

            with open("Webpage_task11.txt", "a")as f:
                f.write(text)


url = "https://www.saucedemo.com/"
sudha = Sudha(url)
sudha.login()
sudha.contents()
print(sudha.current_url())
print(sudha.fetch_tile())






