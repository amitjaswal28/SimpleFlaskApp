import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Set up test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_login_form(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter Name:', response.data)

    def test_post_login_redirect(self):
        response = self.app.post('/login', data={'nm': 'Alice'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'welcome Alice', response.data)

    def test_get_login_with_name_redirect(self):
        response = self.app.get('/login?nm=Bob', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'welcome Bob', response.data)

    def test_success_route_direct(self):
        response = self.app.get('/success/Charlie')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'welcome Charlie', response.data)

if __name__ == '__main__':
    unittest.main()
