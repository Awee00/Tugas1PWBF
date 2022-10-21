from .test_base import BaseTests


class SecondTests(BaseTests):
    def test_blogs(self):
        response = self.client.get('/blogs/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blog1')
        self.assertContains(response, 'blog2')

