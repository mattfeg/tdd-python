from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_retrieve_it_later(self):
        # User opens browser
        self.browser.get('http://localhost:8000')

        # User realize the page title and headline are a to-do list.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # User is invated to insert a task item immediately
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a To-Do item'
        )
        
        # User inserts "Buy peacock feathers" in an textbox
        inputbox.send_keys('Buy peacock feathers')
        
        # When the user press Enter, the page is refreshed,
        # and the page lists "1:Buy peacock feathers" as an item in a to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # The page still keeps having a text box invating to insert another item.
        # The User inserts "User peacock feathers to make a fly"
        self.fail('Finish the test!')
        
        # The page is refreshed again e shows both items in your list

        # The website generates a unique URL for the User and a small explanatory text for that.

        # The User access the URL and the to-do list is there.
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')