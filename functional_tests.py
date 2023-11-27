from selenium import webdriver
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
        self.fail('Finish the test!')
        
        # User is invated to insert a task item immediately

        # User inserts "Buy peacock feathers" in an textbox

        # When the user press Enter, the page is refreshed,
        # and the page lists "1:Buy peacock feathers" as an item in a to-do list.

        # The page still keeps having a text box invating to insert another item.
        # The User inserts "User peacock feathers to make a fly"

        # The pagme is refreshed again e shows both items in your list

        # The website generates a unique URL for the User and a small explanatory text for that.

        # The User access the URL and the to-do list is there.
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')