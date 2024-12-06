from selenium_base import SeleniumBase
from locators import ProblemPage
from locators import ProblemRow
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv

class MainPageScraper(SeleniumBase):
    def __init__(self, waitTime=15):
        super().__init__(waitTime)
        self.csv_path = "data/problem_data.csv"
        
        # Load the page
        self.driver.get(ProblemPage.URL)
        self.wait.until(EC.title_is(ProblemPage.TITLE))
        time.sleep(2) # scuffed wait for load

    def write_to_csv(self, row):
        with open(self.csv_path, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)
    
    def parse_problem_div(self, div):
        title_element = div.find_element(By.XPATH, ProblemRow.TITLE_ELEMENT)
        number, name = title_element.text.split('. ')
        link = title_element.get_attribute('href')

        premium = div.find_elements(By.XPATH, ProblemRow.PREMIUM)
        isPremium = len(premium) > 0

        acceptanceRate = div.find_element(By.XPATH, ProblemRow.ACCEPTANCE_RATE).text
        difficulty = div.find_element(By.XPATH, ProblemRow.DIFFICULTY).text

        return [number, name, link, isPremium, acceptanceRate, difficulty]
    
    # Prints all the problems on the main problem's page
    def get_problems_on_page(self):
        rowgroup = self.get_by_xpath(ProblemPage.ROWGROUP)

        # loop through each problem row
        for row in rowgroup.find_elements(By.XPATH, './div'):
            parsed_row = self.parse_problem_div(row)
            self.write_to_csv(parsed_row)
    
    def next_page(self):
        self.driver.find_element(By.XPATH, ProblemPage.NEXT_BUTTON_XPATH).click()
        time.sleep(2) #scuffed wait for load