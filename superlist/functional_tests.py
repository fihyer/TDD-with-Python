from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")

        # Set path to chromedirver as per your configuration
        webdriver_service = Service('/home/fihyer//chromedriver/stable/chromedriver')

        # Choose Chrome Browser
        self.browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # ? Edith has heard about a cool new online to-do app.
        # ? She goes to check out its homepage: 127.0.0.1:8000 
        self.browser.get('http://localhost:8000')

        # ? She notices the page title and header mention to-do lists
        # assert "To-Do" in browser.title
        self.assertIn("To-Do", self.browser.title)
        self.fail('finish the test!')

        # ? She is invited to enter a to-do item straight away

        # ? She types "Buy peacock feathers" into a text box (Edith's hobby is tying
        # ? fly-fishing lures)


        # ? When she hits enter, the page updates, and now the page lists 
        # ? "1. Buy peacock feathers" as an item in a to-do list

        # ? There is still a text box inviting her to add another item. She
        # ? enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # ? The page updates again, and now shows both items on her list

        # ? Edith wonders whether the site will remember her list. Then she sees
        # ? that the site has generated a unique URL for her -- there is some
        # ? explanatory text to that effect.

        # ? She visits that URL - her to-do list is still there.

        # ? Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main(warnings='ignore')