from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page # supposed View Function

class HomePageTest(TestCase):

	def test_root_url_resolve_to_home_page_view(self):
        # resolve url, and find it's view function.
        # check when we try to resolve url '/', we could
        # obtain the function named home_page
		found = resolve('/')
		self.assertEqual(found.func,home_page)


		# what will happen:
		# 1.  ImportError: because we do not have home_page in file: /lists/views.py 
		# 1.1 Correct: add a function in views.py . 
		#     def home_page():
		#        pass
		# 2.  ErrorChanged: a lot of trackback. Read it. 
		# 2.1 It is very hard when it comes down to a lower level: as some django internal error
		#     here the final is 
		#     raise Resolver404({'tried':tried,'path':new_path})
		#     django.core.urlresolvers.Resolver404:{'tried': [[<RegexURLResolver <RegexURLPatternList> (admin:admin) ^admin>]],'path':''}
		    
		#     It means you have to read the code. You have to know some basic or intermediate python syntax to understand these
		#     Here, it asked a dict with key 'tried' and 'path'. See WHAT HAPPENED IN THE APPLICATION CODE. (LOWER SOURCE CODE)
		#     The author for the TDD does not address this in detail. 
		#     I have to figure it out by myself most of the time by online search or think by myself. This is very hard. 
		# 2.2 Corret: I know the organization of a project, I have to do some url management.
	def test_home_page_returns_correct_html(self):

		request = HttpRequest() # You have to add from django.http import HttpRequest on the header
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))

		self.assertIn(b'<title>To-Do lists</title>',response.content)
		self.assertTrue(response.content.endswith(b'<html>'))

