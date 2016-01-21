from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		# initialization
		self.browser = webdriver.Firefox()

	def tearDown(self):
		# destory after test
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		self.browser.get('someURL')
		# Many assertion syntax like:
		# assertEqual, assertTrue, assertFalse,
		# see document online

		self.assertIn('someText',self.browser.title)

		# He found thesre is a 'To-Do' in title and header:
		header_text = self.browser.find_element_by_tag_name('h1').text 
		self.assertIn('To-Do',header_text)

		# The application asked him to add a to-do entry:
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        
		# He entered "Buy peacock features"
		# 
		inputbox.send_keys('Buy peacock features') 

		# press Enter, refresh page and see "1: Buy peacock feathers"
		inputbox.send_keys(Keys.ENTER) #Remember to import Keys 
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')

		self.assertTrue(any(row.text == '1:Buy peacock features' for row in rows))

		# Another textbox is in the page, 
		# He input Use peacock features to make a fly


		self.fail('Finish the test!')

