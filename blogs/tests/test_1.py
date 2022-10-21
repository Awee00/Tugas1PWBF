from .test_base import BaseTests

class FirstTests(BaseTests):
    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
    def test_blogs_index_url(self):
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code, 200)
