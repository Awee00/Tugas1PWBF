from .test_base import BaseTests


class ThirdTests(BaseTests):
    def test_blog_entries(self):
        response = self.client.get('/blogs/entry/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blog1')
        self.assertContains(response, 'headline1')
        self.assertContains(response, 'headline2')
        self.assertNotContains(response, 'blog2')
        self.assertNotContains(response, 'headline3')
        self.assertNotContains(response, 'headline4')
